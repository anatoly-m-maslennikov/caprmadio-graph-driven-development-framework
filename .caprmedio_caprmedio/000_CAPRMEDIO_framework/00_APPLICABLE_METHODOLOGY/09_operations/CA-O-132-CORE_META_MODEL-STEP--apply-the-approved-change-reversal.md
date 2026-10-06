---
atom_id: CA-O-132
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Approved Change Reversal Step"
  depends_on: [Step, Action, Workflow Run, Step Run, Journal, Operator]
version: 1
updated_at: "2026-10-04 16:45:06 +0000"
relations:
  relates_to: [CA-O-131, CA-R-1509, CA-R-1511, CA-R-1525]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-132-CORE_META_MODEL-STEP--apply-the-approved-change-reversal.md
  source_atom_id: CA-O-132
  source_atom_revision: 1
  source_sha256: b37744bcb2f191e04344485d440242e8f879321e66a55f01f89fb9bef7a6bfd5
  original_relations_sha256: 6f7f7cc249c91076c76d7f2d48c992dd9d3cd18f48aeaf727f6b21263d16a98b
---
# Summary

Apply the approved change reversal

## Operation

Approved Change Reversal Step **means** the Workflow node invoking **=1** Action, CA-O-131, as a Programmatic invocation.

Bind **all** inputs from the admitted Workflow request **and**, on recovery, its preserved execution evidence:

- selected accepted change/event/Revision references and original before/after evidence;
- exact target identities, admitted current Carrier/state and already-satisfied-result/no-op conditions and affected references;
- proposed ordered reversal effects, expected resulting state and applicable current identity/status/Carrier authority;
- recorded Operator decision for those exact effects and the admitted recovery/cancellation boundary;
- authorized executor permissions/capabilities, canonical Project Journal and durable evidence location;
- exact Workflow/Step/Action definition Revisions, distinct Workflow/Step/Action Run identities, parent lineage and completed/pending/uncertain effect and recording receipts.

Return the Action's actual result **and** effect/evidence account unchanged **to** CA-O-130's terminal routing. this binding neither redefines reversal behavior **nor** infers approval from dispatch.

## Details

Missing input, unsupported capability **or** unresolved exact binding blocks invocation rather than substituting guessed values. Programmatic execution requires no Agentic Integrated/Isolated context; an executor that delegates judgment **to** an AI Agent cannot silently treat that delegation as this Programmatic binding.

Retain the actual Step Run, referenced Action Run, definition Revisions, parent Workflow Run, supplied inputs, returned outcome **and** evidence references under current execution/Journal authority. a delivery attempt **or** Tool call is **not** by itself another Step Run. recording failures **and** partial effects survive the handoff; the Step does **not** rerun a completed Action **to** reconstruct missing Journal evidence.
