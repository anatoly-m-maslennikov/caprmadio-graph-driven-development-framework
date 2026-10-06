---
cce_version: "cce_1"
cce_form: "definition"
subjects:
  governs: "Evaluation For Relation"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Operations"
    - "Atom/Local Tier"
version: 11
updated_at: 2026-09-15 05:51:38
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Register Evaluation targets

`evaluation_for` **means** a direct relation owned by an Evaluation Atom **and** directed **to** an Atom whose Content Role is **in** (Requirement, Method, Evaluation, Delivery, Operations) **and** whose authority the Evaluation checks; a Standard Evaluation Atom **must** own **`>=1`** such target relations, while a Core **or** General Evaluation **may** state a representation-independent evaluation policy **without** an artificial list of individual targets. **every** supplied target relation **must** retain the same checked-authority qualification regardless of the Evaluation's Local Tier.
