---
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Step"
    - "Action"
    - "Operator"
    - "Artifact/Revision"
version: 4
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-M-304", "CA-R-1789", "CA-R-1790", "CA-R-1791", "CA-R-1792", "CA-R-1793"]}
atom_id: "CA-E-497"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-497-CORE_META_MODEL-QA_CASE--validate-self-contained-agentic-invocations.md
---
# Summary

Validate self-contained agentic invocations

## Scope

an Agentic Step invocation from its supplied context.

## Claim

the Evaluation **must** check that an Agentic Step invocation can be understood **and** resumed from its supplied context **without** remembered Workflow procedure.

## Details

- remove earlier conversation from an Integrated session: the supplied invocation still identifies the requested Action, inputs, evidence, actual effects, authority boundaries, expected result, **and** return route.
- supply the invocation **to** an Isolated context: require the same admitted responsibility **and** constraints rather than implicit access **to** the parent conversation.
- omit required context **or** make a referenced input inaccessible: require a visible missing-input result, **not** guessed execution.
- deliver the same pending invocation again: preserve its identity **and** actual effects; repeated delivery **must not** imply a new Run **or** authorization **to** replay effects.
- provide a prompt that contradicts its bound definition **or** expands permission: reject the instruction even **if** it is self-contained.
- a Step result returns **or** a Workflow hands off: the executor owns the declared routing; a returned prompt alone is **not** Step completion **or** successor completion.

check exact supplied evidence, **not** a claim that the session will remember how **to** proceed.
