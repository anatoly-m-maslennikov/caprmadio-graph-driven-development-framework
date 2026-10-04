---
atom_id: CA-R-1821
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:03:24 +0400"
subjects:
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/source admission"
  depends_on: [Workflow, Action, Operator, Initiative, Journal, Tool, Implementation]
relations:
  relates_to: [CA-R-1094, CA-R-1525, CA-R-1720]
---
# Summary

Admit only current authorized selected-operation Runs

## Scope

The shared RUN_SUPPORT caller boundary for the thirteen selected CA-P-1117
requests. It is not a Workflow, source-discovery capability, or autonomous
dispatcher.

## Claim

RUN_SUPPORT **must** start an actual selected Workflow, Step, or Action Run
only from one explicit current selected-operation request and one current
Operator authorization in its sealed Initiative context.

## Details

- The request supplies exactly one closed selected operation route, a stable
  caller-supplied `request_id`, typed parameters, target frontier, requested
  effects, and a reference plus digest for the closed definition manifest. The
  manifest is the reviewed route projection and lists the complete admitted
  Workflow/Step/Action bindings; RUN_SUPPORT validates and consumes that
  projection but neither abbreviates it nor defines route semantics. Optional
  expected definition revisions (Atom ID, kind, Version, safe
  repository-relative path, and sealed digest) must exactly agree with the
  manifest when supplied. Unknown fields, a missing/unstable `request_id`, or
  an attempt to reuse one `request_id` with different canonical request bytes
  are rejected before dispatch.
- `source_freshness` declares the exact selected-source registry reference,
  registry version and digest, selected binding reference and digest, and the
  expected definition-manifest reference and digest. RUN_SUPPORT resolves only
  that declared route through the current selected-source registry, records the
  exact observed bindings/currentness comparison, and does not infer a route
  from a Tool name, directory, prompt, or earlier result.
- The selected source must be one of CA-P-1117's thirteen requested routes or
  an actual Action bound by one of those routes. A generic Rebuild Projections
  route remains a shortcut to its selected builders, not a fourteenth Run.
- Every actual Run carries the one sealed Initiative required by CA-R-1094,
  including its stable identity, human-instruction summary, and safe reference
  when one exists. `mode` defaults to `preview`; only literal `execute` can
  start work. A preview is read-only and returns a sealed proposal receipt
  containing the request ID, route, Initiative reference, declared and observed
  source-freshness references, and the canonical digests for parameters, target
  frontier, effects, and definition manifest. It creates neither a
  Workflow/Step/Action Run nor a Journal Event.
- An execute request must carry that exact proposal receipt and digest, the
  assigned stable Action identity and requested Run identity, and explicit
  sealed Operator authorization. That authorization must bind the same request
  ID, route, proposal-receipt digest, parameters digest, target-frontier digest,
  effects digest, definition-manifest reference/digest, and current source
  freshness. A worker, session, queue, MCP call, or Journal partition is not a
  substitute Initiative or authorization.
- Before dispatch, compare the preview receipt and authorization with the
  supplied canonical request, re-resolve each declared current source reference,
  and re-check mutable input/target freshness. A changed, withdrawn,
  unavailable, unauthorized, or stale binding pauses the request for recorded
  revalidation; it must not substitute the newest definition, retain a stale
  preview, or reuse old approval. Recording-only recovery under CA-R-1824 does
  not re-dispatch or consume a replacement authorization.
- Refusal and a request denied before execution return an explicit non-start
  disposition. Receipt observation, status polling, recovery, an MCP call, or
  any mode other than literal `execute` do not start another Run.
