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
version: 5
updated_at: "2026-09-24 01:39:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-R-1559
    - CA-O-024
    - CA-O-089
    - CA-O-090
    - CA-M-002
---
# Summary

Repair nonconforming Implementation

## Claim

Implementation Repair **means** the Agentic Action that repairs a diagnosed code defect within the admitted work boundary **and** retry allowance, retaining a provisional Method lesson **when** one is missing.

### Inputs and diagnosis

- receive the diagnosed implementation **or** test-implementation defect, failed candidate, governing R/E/D, active Method Projection, selected P/Plan item, verification commands, pending Drafts, **and** an admitted fix-and-evaluate retry.
- require evidence sufficient **to** explain the cause **and** the intended correction. unresolved diagnosis, conflicting authority, unmet confidence, **or** missing permission returns `blocked`; a retry allowance grants no extra authority.

### Corrective Method and repair

- check existing Method authority **and** pending Drafts first. reuse an existing applicable Method **or** refine the same permitted Draft for the same lesson; do **not** create duplicate Method Atoms on repeated failures.
- **if** the diagnosed coding mistake exposes a missing Method, create a Standard-tier M Draft explaining **how** **to** make the bounded correction **or** avoid that mistake. keep **=1** Claim, its precise governed Subject, applicable Scope Unit, actual Author, structured body, **and** evidence context. obey Draft identity rules; do **not** assign an active Atom ID **or** include the Draft **in** the active Method Projection.
- the Draft is a proposed correction, **not** new governing authority. add **or** strengthen a regression test **before** the fix **when** the defect can be reproduced; establish that it detects the defect rather than merely failing because of an unrelated setup error.
- correct the code under existing governing authority **and** admitted permissions. test code is Implementation too; repairing it **must not** silently weaken an Evaluation, expected outcome, Requirement, **or** Delivery obligation.
- return `repaired` with changed candidate, actual correction, affected work, regression evidence, **and** retained Draft references for re-evaluation. do **not** activate a Method, report passing tests, **or** reset retry accounting from this Action.
- **if** a governing RMED change is necessary, return `authority_change_required` for disposition under CA-R-1559 **before** changing that authority. an authorized change requires renewed preparation against the new baseline.
