---
atom_id: CA-P-1715
content_role: Plan
type: Plan
label: Task
work_sequence_number: 26
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-05 17:27:39 +0000"
subjects:
  governs: "Admitted Release manifest publication"
  depends_on: [Workflow, Action, Implementation, Evaluation, Journal, Manifest, Permission]
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1624]
---
# Summary

Publish the admitted Release manifest successor

## Objective

Deliver the source-derived additive selected-manifest publisher needed to admit Release Version as the sixteenth selected Workflow.

## Details

1. review CA-R-1882, CA-M-339, CA-E-582 and CA-D-576 before implementation; the source proposal alone is not accepted authority.
2. derive the complete Release route and admission from the current accepted source. Preserve the fifteen existing route rows, source freshness and query admissions; stop rather than infer missing graph semantics.
3. implement a non-writing plan and an explicitly authorized atomic publication with exact loader readback. Publication is Projection support, not another selected Workflow or proof of Release execution.
4. test stale input/source refusal, authorization, exact additive preservation, write/readback failure and sixteen-route discovery. Retain fixtures as the Operator requested.
5. the bounded implementation/review estimate is <=15 minutes; decompose further if actual remaining work exceeds that bound.

### Completion evidence

The focused lifecycle and publisher suite passed 27 tests. Independent source review accepted the target-specific Journal history repair: unrelated legacy Events cannot block this Carrier, while unsupported or malformed Events claiming this exact Carrier fail closed.

The authorized publication replaced the exact fifteen-route input with the source-admitted sixteen-route successor. Loader readback and independent observation confirm the sole added route is `release_version`, its serialized graph and admission match current accepted sources, and the first fifteen route identities remain unchanged. The input Carrier SHA-256 is `15859926813eed353857e3bae8dc7739f76da4afe01f852bc0805eaeea2974d6`; the output Carrier SHA-256 is `1eabfd2f1a0df45ae0df2ff4b2221ebe557ef1f520a990ef6d10f542259d6723`, with canonical manifest digest `48a03709ba64113b007893bf92886be447a57be1ce5b324056c8f18eab7854e7`.

Completed canonical Event `journal:release-manifest:81cf4fac9b9087e14d451502fa1be473c664eea1f7f4b74e1032ba1b084449a7` is sealed in `.caprmedio_caprmedio/_journal/anatoly-m-maslennikov-2026-10-05-part-1.ndjson`. Its sealed predecessor proves the observed input SHA-256; no publication pending evidence remains. This closes only manifest publication, not runtime installation, Docker, queue, or Release acceptance.

## Definition of Done

Current reviewed source authority and focused tests prove that only the exact fifteen-to-sixteen successor can be published. The canonical Project manifest is published only after the accepted full graph and explicit authorization are available. No runtime, queue or Docker acceptance is inferred from source publication.
