---
atom_id: "CA-R-1018"
cce_version: "cce_1"
cce_form: "definition"
subjects:
  governs:
    continuant:
      - "Evaluation For Relation"
  depends_on:
    continuant:
      - "Atom/Content Role: Evaluation"
      - "Atom/Content Role: Requirement"
      - "Atom/Content Role: Method"
      - "Atom/Content Role: Delivery"
      - "Atom/Local Tier"
version: 8
updated_at: "2026-09-10 02:19:47 +0400"
relations: {}
---
# Register Evaluation targets

`evaluation_for` **means** a direct relation owned by an Evaluation Atom **and** directed **to** an Atom whose Content Role is **in** (Requirement, Method, Delivery) **and** whose authority the Evaluation checks; a Standard Evaluation Atom **must** own **`>=1`** such target relations, while a Core **or** General Evaluation **may** state a representation-independent evaluation policy **without** an artificial list of individual targets. **every** supplied target relation **must** retain the same checked-authority qualification regardless of the Evaluation's Local Tier.
