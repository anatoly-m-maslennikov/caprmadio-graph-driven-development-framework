---
atom_id: CA-D-435
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Work Journal/Event/Carrier Serialization"
  depends_on:
    - "Work Journal/Event"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
version: 2
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
---
# Serialize Atom replacement event references

the schema-version `3` completed File Carrier `MOVE` event that archives a replaced numbered Project-owned Atom **must** serialize the replacement references together as top-level `predecessor_atom_id` **and** `successor_atom_ids`. `predecessor_atom_id` stores **`=1`** canonical stable Atom ID; `successor_atom_ids` stores an array of **`>=1`** distinct canonical stable Atom IDs, excluding the predecessor. these fields carry assigned identities **only**, **not** paths, mutable filename components, **or** Revision suffixes; their array order does **not** establish a priority **or** execution order.

the predecessor identity **must** match the archived result filename's Atom ID, whose `@<version>.md` suffix **must** match the result Version **in** its `archive/` directory. the ordinary result **and** `previous_result_event` preserve the Carrier/Revision evidence; the replacement fields **must not** duplicate that evidence. both fields **must** be included **in** the existing Event digest. a partial pair, an empty list, a duplicate successor, a self successor, **or** a pair on a recovered, folder, non-archive, **or** non-`MOVE` event is invalid. ordinary events **and** historical records **without** these fields retain their existing schema; absence of a pair does **not** assert that a move was a replacement. the active-successor prerequisite remains governed by CA-R-807, **not** established by payload syntax alone.
