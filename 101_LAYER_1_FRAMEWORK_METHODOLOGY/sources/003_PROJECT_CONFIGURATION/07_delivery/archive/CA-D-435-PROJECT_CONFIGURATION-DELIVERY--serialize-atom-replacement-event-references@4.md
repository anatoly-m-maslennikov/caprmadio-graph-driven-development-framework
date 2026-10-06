---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Work Journal/Event/Carrier Serialization"
  depends_on:
    - "Work Journal/Event"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
version: 4
updated_at: "2026-09-17 02:23:47 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Atom replacement event references

a schema-version `3` completed File Carrier `MOVE` event recording an Atom replacement **must** serialize its observed replacement references as paired top-level `predecessor_atom_id` **and** `successor_atom_ids` fields.

- `predecessor_atom_id` stores the observed identity as a string; `successor_atom_ids` stores the observed successor identities as an array of strings. preserve their values **and** array order exactly through safe encoding. array order does **not** establish priority **or** execution order.
- the pair is optional on ordinary events; absence does **not** establish whether a move was a replacement. a partial pair, a null field, **or** a value with the wrong storage type fails this encoding.
- both fields participate **in** the existing Event digest. the ordinary result **and** `previous_result_event` retain Carrier **and** Revision evidence **without** duplicating it **in** replacement fields.
- legacy **or** nonconforming IDs, an empty observed successor array, duplicate **or** self-referencing identities, a filename mismatch, **and** an invalid archive placement remain recordable payload. CA-E-462 evaluates the replacement independently; failed conformance **must not** become a Journal-admission gate under CA-R-1491.
- ordinary **and** historical records **without** these fields retain their selected schema. preserved observations **must not** be rewritten **to** satisfy current Atom grammar, archive rules, **or** successor conditions. successful storage proves **only** event **and** storage integrity, **not** a valid replacement.
