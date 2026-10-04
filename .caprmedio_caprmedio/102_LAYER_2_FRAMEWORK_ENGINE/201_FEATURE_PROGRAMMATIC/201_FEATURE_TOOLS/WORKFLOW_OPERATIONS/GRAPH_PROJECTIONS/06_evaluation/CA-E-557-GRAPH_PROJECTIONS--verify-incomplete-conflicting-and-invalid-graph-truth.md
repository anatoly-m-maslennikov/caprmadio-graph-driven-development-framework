---
atom_id: CA-E-557
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:45 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Failure truth cases"
  depends_on: [Tool, Projection, Artifact, Journal]
relations:
  evaluation_for: [CA-R-1835, CA-R-1836, CA-R-1837]
---
# Summary

Verify incomplete, conflicting, and invalid graph truth

## Scope

Functional failure cases for incomplete source coverage, conflicts, cycles, malformed carriers, and self-references.

## Claim

Every invalid or incomplete fixture **must** preserve its source evidence and return a non-complete outcome; neither builder may repair authority or report `built`/`no_op`.

## Details

Exercise unreadable/malformed selected carriers, missing governing definition, stale existing output, unresolved endpoint, conflicting relation/definition evidence, Terms parent/dependency cycle, self-reference, and cardinality violation. Assert affected paths/identities/digests and diagnostics remain visible, only declared data is represented, validity/coverage/currentness dispositions fail or remain unresolved as appropriate, and the outcome is `incomplete`, `conflicting`, `stale`, `blocked`, or `failed`, never `built`/`no_op`. Assert no source edit, inferred Term/Entity/Property/Scope Unit, graph repair, retry, or fictitious Journal completion. This carrier specifies functional proof, not runtime evidence.
