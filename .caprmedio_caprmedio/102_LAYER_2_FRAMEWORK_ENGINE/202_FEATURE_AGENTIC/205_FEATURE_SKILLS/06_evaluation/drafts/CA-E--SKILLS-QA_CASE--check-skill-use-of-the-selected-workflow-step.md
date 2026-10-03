---
content_role: Evaluation
type: QA Case
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Skill/Step participation"
  depends_on:
    - "Action"
    - "CAPRMEDIO Main Skill"
    - "Methodology"
    - "Operator"
    - "Skill"
    - "Step"
    - "Step Run"
    - "Tool"
    - "Workflow"
version: 1
updated_at: "2026-09-23 19:41:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1529", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559"], "relates_to": ["CA-R-1522", "CA-R-1601"]}
---
# Summary

Check Skill use of the selected Workflow Step

## Claim

the Skill-participation Evaluation **must** check that the Skill uses the admitted framework response for the current Step rather than independently choosing a Workflow procedure **or** capability sequence.

### Fixture and evidence

- fix the Operator request, owning Project, active authority references, routing inputs, admitted Workflow **and** Step, Action inputs, permissions, **and** required result. expose the necessary capabilities **and** distinguishable irrelevant alternatives.
- identify the expected sufficient capability set **or** admitted equivalent alternatives for this bounded fixture. justify it from the Action **and** its bindings; do **not** assert a globally optimal minimum.
- capture the submitted request, framework response, instructions used, actual capability calls, reported results, **and** **any** continuation request.

### Acceptance

- the Skill submits the request through the declared framework interface **and** uses the returned current-Step binding; it does **not** maintain another routing dictionary **or** silently substitute another Action.
- capability calls remain necessary for the admitted Action, within authorization, **and** compatible with its required outcome. a deliberately irrelevant capability, omitted necessary input, invented source, **or** contradictory instruction yields failure.
- the Skill returns the actual result against its identified invocation. the executor selects the next Step; the Skill does **not** continue through a remembered **or** locally authored sequence.
- repeating the fixture with a changed admitted Action prompt but the same wrapper interface uses the new bound instructions **without** editing the Skill body. receiving a prompt alone is **not** completion.
- missing evidence **or** an unresolved fixture expectation yields an unresolved result, **not** a successful selection claim.
