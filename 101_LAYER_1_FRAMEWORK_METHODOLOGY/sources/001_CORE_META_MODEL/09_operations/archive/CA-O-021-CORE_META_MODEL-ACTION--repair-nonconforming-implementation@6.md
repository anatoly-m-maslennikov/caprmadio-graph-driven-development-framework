---
atom_id: CA-O-021
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Implementation Repair"
  depends_on:
    - "Action"
    - "Implementation Failure Diagnosis"
    - "Implementation Retry Control"
    - "Operator"
    - "AI Agent"
    - "Spec"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Revision/Author"
    - "Local Tier"
version: 6
updated_at: "2026-09-24 17:18:07 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-R-1559
    - CA-O-024
    - CA-O-089
    - CA-M-002
---
# Summary

Repair nonconforming Implementation

## Claim

Implementation Repair **means** the Agentic Action that repairs a diagnosed code defect within the admitted work boundary **and** retry allowance, preserving the issue **and** verification evidence.

- inputs: the diagnosed implementation **or** test-implementation defect, failed candidate, governing R/E/D, active Method Projection, selected P/Plan item, verification commands, retained issue evidence, **and** an admitted fix-and-evaluate retry.
- require evidence sufficient **to** explain the cause **and** correction. unresolved diagnosis, conflicting authority, unmet confidence, **or** missing permission returns `blocked`; retry allowance grants no extra authority.
- reproduce the issue with an appropriate targeted test **before** the fix **when** possible. reuse an existing reproducer; add unit, integration, **or** another focused test according **to** governing Methods. distinguish the actual defect from a setup failure.
- correct the code under existing authority **and** permissions. test code is Implementation too; do **not** weaken an Evaluation, expected output, Requirement, **or** Delivery obligation **to** obtain a pass.
- return `repaired` with the changed candidate, failure evidence, diagnosis, actual correction, tests, expected outcomes, **and** replay commands for re-evaluation. passing targeted tests do **not** replace required end-to-end verification.
- do **not** create, update, **or** promote corrective M Atoms **in** this Action. retain evidence for the separate Method-learning Workflow; learning is **not** a condition for accepting a verified implementation fix.
- return `authority_change_required` **if** a governing RMED change is necessary, for disposition under CA-R-1559 **before** changing that authority. authorized baseline changes require renewed preparation; do **not** reset retry accounting.
