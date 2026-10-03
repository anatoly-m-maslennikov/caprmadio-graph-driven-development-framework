---
atom_id: CA-E-462
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Journal/Record"
  depends_on:
    - "Work Journal/Event"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
    - "Atom/Content Role: Ops"
version: 2
updated_at: "2026-09-14 06:21:07 +0400"
relations:
  evaluation_for:
    - CA-R-807
---
# Validate Atom replacement event evidence

an Atom replacement event Evaluation **must** reject missing, unresolved, duplicate, self-referencing, **or** mismatched predecessor **and** successor identities under CA-R-807. the Evaluation **must** verify that **every** named successor is already Active **before** the predecessor is archived, that the archived predecessor preserves its exact prior bytes **and** Version, **and** that **`=1`** authoritative Journal event records the same replacement.

a format check alone **must not** be reported as evidence of those state conditions. repeating the same recorded event **must not** create another authoritative record. event field names, encoding, receipt representation, **and** storage transaction mechanics remain checked against the separately selected Delivery authority; this Core Evaluation **must not** require a Git Commit **or** a particular Journal serialization.
