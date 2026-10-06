---
subjects:
  governs: "Screen Short Names"
  depends_on:
    - "Action"
    - "Operator"
    - "Project"
version: 5
updated_at: "2026-10-04 15:08:22 +0000"
relations: {"child_of":["CA-M-005"],"relates_to":["CA-R-1057"]}
atom_id: "CA-O-065"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
---
# Summary

Screen short names for unintended readings

## Operation

Screen Short Names **means** the Action that screens a proposed short name, abbreviation, **or** prefix **before** admission:

- inspect the candidate's case-insensitive tokens **and** joined form for unintended obscene, insulting, deceptive, **or** distracting readings **in** the Operator's languages.
- **if** such a reading is found, **then** present a concise warning that explains it **and** offers readable alternatives preserving the canonical meaning, preferring the shortest suitable alternative.
- do **not** automatically reject the candidate on that basis; allow the Operator **to** accept the warned name explicitly.

this Action defines screening behavior; it does **not** record a particular execution **or** automatically change a registered name.

## Details
