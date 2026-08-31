/**
 * blockchain_bridge.js — Thin client for blockchain/identity over the PGC transport boundary.
 *
 * Descended from RI-0's pgs_bridge.js, which described itself as "zero schema awareness, zero
 * workflow branching, zero validation". That is still the whole design; what changed is what it
 * says on the wire. RI-0 POSTed a WORKFLOW identity to /api/run. This speaks only public Operation
 * Identities (blockchain.register_actor, blockchain.accept_actor, blockchain.reject_actor) and
 * never names a workflow — an operation identity is not a workflow identity, and the workflow an
 * operation reaches may be re-pointed without this file changing.
 *
 * It renders the Canonical Transport Response (TRANSPORT_RESPONSE_V0):
 *   { request_id, outcome, result_class, result, evidence, errors }
 *
 * DELIBERATELY ABSENT: validation. The page does not check whether details are present or
 * well-formed — the platform does, and says which field was at fault. A page that checked would be
 * a second opinion the business never approved, and the two would eventually disagree.
 */

// The one route the adapter binds to the blockchain namespace. Every act shares it; the act is
// named in the body, never by where the request is sent.
const OPERATION_ROUTE = '/blockchain';

// The only thing carried between pages: what the person just typed, so they need not type it twice.
// Not a record — the business never reads it back, and no act depends on it being here.
const CARRIED_ADDRESS = 'pgc_contact_address';

async function submitOperation(formId) {
    const form = document.getElementById(formId);
    const resultDiv = document.getElementById('result');
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;

    // Harvest every data-field into params, exactly as RI-0 did. An empty control is omitted
    // rather than sent blank, so "not supplied" reaches the boundary as absence — which is what an
    // optional field means and what a required one is refused for.
    const params = {};
    form.querySelectorAll('[data-field]').forEach(function (input) {
        const raw = input.value;
        if (raw !== '') {
            setDeep(params, input.getAttribute('data-field'), raw);
        }
    });

    // Which act this is. A control may carry the identity itself (accept and reject are two acts,
    // not one act with an outcome field) — the markup names them; this file maps nothing.
    const selector = form.querySelector('[data-operation-select]');
    const operation = selector ? selector.value : form.getAttribute('data-operation');

    submitBtn.disabled = true;
    submitBtn.textContent = 'Submitting...';
    resultDiv.className = 'result-panel';
    resultDiv.style.display = 'none';
    resultDiv.innerHTML = '';

    try {
        const response = await fetch(OPERATION_ROUTE, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ operation: operation, params: params })
        });
        const envelope = await response.json();
        rememberAddress(params.contact_address);
        renderResult(resultDiv, envelope, operation);
    } catch (e) {
        renderError(resultDiv, e.message);
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    }
}

function renderResult(el, envelope, operation) {
    const cls = envelope.result_class || 'ERROR';
    const isSuccess = cls === 'SUCCESS';
    el.className = 'result-panel visible ' + (isSuccess ? 'success' : 'error');
    el.style.display = '';

    let html = '<span class="status-badge">' + escapeHtml(cls) + '</span>';
    html += '<div class="result-field"><span class="label">Operation</span> '
         +  '<span class="value">' + escapeHtml(operation) + '</span></div>';

    // What the business turned away, and why. The boundary names the field at fault; an act that
    // ran and refused reports its own status. Both arrive as VIOLATION — the governed set has no
    // kind for "ran and refused" — so the detail is where the two are told apart.
    if (Array.isArray(envelope.errors) && envelope.errors.length) {
        for (const err of envelope.errors) {
            html += '<div class="result-field"><span class="label">' + escapeHtml(err.code || 'ERROR') + '</span> '
                 +  '<span class="value">' + escapeHtml(err.message || '') + '</span></div>';
        }
    }

    // What was recorded. Rendered generically from whatever the egress contract exposes — this file
    // knows no field names, so a contract that exposes another one needs no change here.
    if (isSuccess && envelope.result) {
        for (const [field, value] of Object.entries(envelope.result)) {
            html += '<div class="result-field"><span class="label">' + escapeHtml(field) + '</span> '
                 +  '<span class="value">' + escapeHtml(value === null ? '—' : value) + '</span></div>';
        }
    }

    // Evidence is exposed by reference only. A "trace:<path>" reference resolves under the /traces
    // mount, so the record of what happened is one click from the answer.
    if (Array.isArray(envelope.evidence) && envelope.evidence.length) {
        const items = envelope.evidence.map(function (ev) {
            if (typeof ev === 'string' && ev.indexOf('trace:') === 0) {
                const ref = ev.slice('trace:'.length);
                const id = ref.replace(/\.jsonl$/, '').split('/').pop();
                return '<a href="/' + encodeURI(ref) + '" target="_blank" rel="noopener">trace:'
                     + escapeHtml(id) + '</a>';
            }
            return escapeHtml(String(ev));
        }).join(', ');
        html += '<div class="result-field"><span class="label">Evidence</span> '
             +  '<span class="value">' + items + '</span></div>';
    }

    html += '<details style="margin-top:12px;">'
         +  '<summary style="font-size:12px;color:#64748b;cursor:pointer;padding:4px 0;">Canonical Transport Response</summary>'
         +  '<div class="result-json">' + escapeHtml(JSON.stringify(envelope, null, 2)) + '</div>'
         +  '</details>';

    el.innerHTML = html;
}

function renderError(el, msg) {
    el.className = 'result-panel visible error';
    el.style.display = '';
    el.innerHTML = '<span class="status-badge">UNREACHABLE</span>'
        + '<div class="result-field"><span class="label">Message</span> '
        + '<span class="value">' + escapeHtml(msg) + '</span></div>'
        + '<div class="result-field"><span class="label">Note</span> '
        + '<span class="value">The business was not reached, so nothing was recorded.</span></div>';
}

function setDeep(obj, path, value) {
    const parts = path.split('.');
    let current = obj;
    for (let i = 0; i < parts.length - 1; i++) {
        if (!current[parts[i]]) current[parts[i]] = {};
        current = current[parts[i]];
    }
    current[parts[parts.length - 1]] = value;
}

function escapeHtml(str) {
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function rememberAddress(address) {
    if (address) sessionStorage.setItem(CARRIED_ADDRESS, address);
}

// Fill in the address the person just typed, if they typed one on an earlier page. A page that
// lost it still works — they simply retype.
document.addEventListener('DOMContentLoaded', function () {
    const field = document.getElementById('contact_address');
    if (field && !field.value) {
        const carried = sessionStorage.getItem(CARRIED_ADDRESS);
        if (carried) field.value = carried;
    }
});
