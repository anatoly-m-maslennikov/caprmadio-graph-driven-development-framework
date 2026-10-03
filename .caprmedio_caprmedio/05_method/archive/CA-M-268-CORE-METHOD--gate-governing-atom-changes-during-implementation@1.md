---
atom_id: CA-M-268
cce_version: "cce_1"
cce_form: "method"
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
    - "CA-M-261"
  relates_to:
    - "CA-M-130"
    - "CA-R-851"
    - "CA-R-1080"
    - "CA-M-262"
---
# Gate governing Atom changes during implementation

**to** change a governing RMED Atom during implementation, resolve its effective Author **before** the proposed change, its governing permissions, the Task Autonomous Confidence Threshold, **and** **all** additional Operator rules. obtain Operator approval **before** changing an Operator-authored Atom; request Operator disposition **before** changing an AI-authored Atom **when** confidence is below the threshold **or** an additional rule requires approval. an AI-authored Atom **may** change autonomously **only** **when** confidence is at **or** above the threshold **and** **all** applicable permissions **and** Operator rules allow it. a prohibition remains a prohibition; authorship **or** confidence **must not** create permission. a missing **or** unresolved Author **must not** be treated as proof of AI authorship; apply the Author default under CA-R-1080. an authorized RMED change establishes a new baseline under CA-M-262, **and** the applicable work **and** Evaluations **must** be resolved again against it.
