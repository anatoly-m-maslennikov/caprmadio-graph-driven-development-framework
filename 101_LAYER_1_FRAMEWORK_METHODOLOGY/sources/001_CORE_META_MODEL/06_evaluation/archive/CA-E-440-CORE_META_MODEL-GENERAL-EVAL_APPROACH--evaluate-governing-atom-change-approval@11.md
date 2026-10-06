---
cce_version: "cce_1"
cce_form: "evaluation"
version: 11
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"child_of":["CA-E-001"],"evaluation_for":["CA-R-1559","CA-R-1591","CA-R-1552","CA-R-1080"]}
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "Atom/Revision/Author"
    - "Operator"
    - "AI Agent"
    - "AI Agent/Confidence"
    - "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold"
    - "Spec"
    - "Atom"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Project"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate governing Atom change approval

the governing-Atom change Evaluation **must** return `fail` **if** an Operator-authored Atom changes **without** Operator approval, an AI-authored Atom changes autonomously below the Plan confidence threshold, a permission **or** additional Operator constraint is bypassed, the Author is changed **before** resolving the approval requirement, **or** an omitted **or** unresolved Author is assumed **to** be an AI Agent. it **must** also return `fail` **if** an authorized RMED change is reported against the old unchanged baseline **or** its affected work **and** Evaluations are **not** resolved again. AI authorship **and** sufficient confidence **must not** override an explicit prohibition.
