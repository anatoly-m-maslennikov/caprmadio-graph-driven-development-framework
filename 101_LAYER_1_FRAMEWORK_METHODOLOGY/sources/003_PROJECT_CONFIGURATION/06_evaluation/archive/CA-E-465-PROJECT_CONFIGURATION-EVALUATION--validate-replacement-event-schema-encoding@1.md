---
atom_id: CA-E-465
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Work Journal/Event/Carrier Serialization"
  depends_on:
    - "Journal/Record"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
version: 1
updated_at: "2026-09-14 06:21:07 +0400"
relations:
  evaluation_for:
    - CA-D-435
    - CA-D-339
---
# Validate replacement Event schema encoding

the selected schema-version `3` replacement Event encoding **must** satisfy CA-D-435. accept a valid archive `MOVE` with paired predecessor **and** distinct successor identities; reject missing, null, malformed, duplicate, self-referencing, mismatched-predecessor, mismatched-Version, **or** wrongly placed replacement fields. a changed payload with an unchanged digest **must** fail.

ordinary historical records **without** replacement fields retain their previous validation behavior. replay of the same sealed Event **must** reuse its canonical receipt rather than append another record. passing schema validation does **not** establish CA-E-462's active-successor, exact-archive, **or** historical-evidence conditions.
