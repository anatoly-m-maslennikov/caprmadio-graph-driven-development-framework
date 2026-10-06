---
atom_id: "CA-M-265"
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Evaluation/grouping"
  depends_on:
    continuant:
      - "Atom/Content Role"
      - "Evaluation For Relation"
version: 1
updated_at: "2026-09-05 03:48:00 +0400"
relations: {}
---
# Derive evaluation groups from checked authority

**to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core Evaluation **must not** require an invented classification.
