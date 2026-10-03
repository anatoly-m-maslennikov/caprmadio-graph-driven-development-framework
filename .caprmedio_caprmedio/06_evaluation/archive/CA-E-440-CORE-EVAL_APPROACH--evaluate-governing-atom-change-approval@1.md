---
atom_id: CA-E-440
cce_version: "cce_1"
cce_form: "evaluation"
subjects:
  governs:
    occurrent:
      - "Project/Implementation/authority change"
  depends_on:
    continuant:
      - "Atom/Revision/Author"
      - "Operator"
      - "AI Agent"
      - "AI Agent/Confidence"
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
      - "Spec"
version: 1
updated_at: "2026-09-05 18:40:03 +0400"
relations:
  child_of:
    - "CA-E-001"
  evaluation_for:
    - "CA-M-268"
    - "CA-M-130"
    - "CA-R-851"
    - "CA-R-1080"
---
# Evaluate governing Atom change approval

the governing-Atom change Evaluation **must** return `fail` **if** an Operator-authored Atom changes **without** Operator approval, an AI-authored Atom changes autonomously below the Task confidence threshold, a permission **or** additional Operator constraint is bypassed, the Author is changed **before** resolving the approval requirement, **or** an omitted **or** unresolved Author is assumed **to** be an AI Agent. it **must** also return `fail` **if** an authorized RMED change is reported against the old unchanged baseline **or** its affected work **and** Evaluations are **not** resolved again. AI authorship **and** sufficient confidence **must not** override an explicit prohibition.
