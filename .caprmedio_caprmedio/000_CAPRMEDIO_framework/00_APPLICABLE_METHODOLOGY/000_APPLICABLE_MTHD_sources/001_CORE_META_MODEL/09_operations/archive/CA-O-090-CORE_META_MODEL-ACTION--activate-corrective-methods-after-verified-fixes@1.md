---
atom_id: CA-O-090
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
  governs: "Corrective Method Acceptance"
  depends_on:
    - "Action"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Summary"
    - "Atom/Revision/Author"
    - "Local Tier"
    - "Projection"
    - "AI Agent"
    - "Operator"
    - "Autonomous Confidence Threshold"
    - "Spec"
version: 1
updated_at: "2026-09-24 01:39:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-O-021
    - CA-O-020
    - CA-R-1559
    - CA-R-1591
    - CA-M-002
    - CA-M-262
---
# Summary

Activate corrective Methods after verified fixes

## Claim

Corrective Method Acceptance **means** the Agentic Action that promotes a verified corrective Method Draft **only** after the repaired candidate **and** its regression evidence justify that Method.

- inputs: recorded corrective Method Drafts, diagnosis, actual fix, regression **and** current-candidate Evaluation results, source/definition bindings, current applicable Method authority, selected Plan, actual Author information, **and** confidence/permission gates.
- require that the regression detects the diagnosed defect, passes after the fix, **and** the required relevant checks pass against the current candidate. stale, absent, failed, **or** incomplete evidence keeps the Method Draft non-authoritative.
- check the proposed Method against Project Principles, higher-tier authority, existing Methods, its Claim/Subject boundary, **and** the actual fix. tests are necessary evidence, **not** proof that an overbroad policy is valid. do **not** generalize the Standard Method into Core, General, **or** a broader policy during this Workflow.
- reuse existing equivalent authority rather than activate a duplicate; retain the recorded Draft's disposition. any supersession **or** governing-authority edit follows its own permission **and** history rules.
- resolve the effective confidence threshold **and** permissions, including CA-R-1559 for governing-Atom changes. obtain required Operator approval; authorship **or** a passing test never grants permission. an unresolved gate returns `blocked` with the Draft unchanged.
- **only** after verification **and** admission, promote the new Method under the current Atom identity, Status, Carrier, **and** history rules, preserving its Summary. return `accepted` with actual activated identities/Revisions **and** the governing-baseline change; return `already_covered` for a nonduplicating disposition; return `blocked` for incomplete verification **or** admission.
- refresh the active Method Projection **and** re-resolve affected work/Evaluations **before** continuation. retain compatible evidence **only** after explicit current-baseline review; do **not** report unchanged-authority reconstruction **or** reset retry allowances.
