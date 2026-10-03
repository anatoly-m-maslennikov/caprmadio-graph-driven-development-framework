---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Implementation Repair"
  depends_on:
    - "Action"
    - "Implementation Retry Control"
    - "Operator"
    - "Spec"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
version: 4
updated_at: "2026-09-21 00:39:50 +0000"
relations: {"child_of":["CA-O-016"],"relates_to":["CA-R-1559","CA-O-024"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Repair nonconforming Implementation

Implementation Repair **means** the Action that corrects nonconforming Implementation identified by failed Evaluations within the applicable governing permissions **and** retry allowance. correcting the implementation of an Evaluation is Implementation work; it **must not** silently change the governing Evaluation **or** other RMED authority. return the actual correction result **and** affected work for re-evaluation.

**if** a governing RMED change is needed, **then** report that need for disposition under CA-R-1559 **before** changing that authority. honor the retry decision **and** accounting under CA-O-024 **without** independently resetting **or** double-counting its allowance. that decision does **not** override confidence, approval, **or** other Operator constraints.
