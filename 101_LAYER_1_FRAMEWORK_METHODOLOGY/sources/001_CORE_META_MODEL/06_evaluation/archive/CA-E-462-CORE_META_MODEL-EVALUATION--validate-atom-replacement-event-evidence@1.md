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
version: 1
updated_at: "2026-09-14 01:48:45 +0400"
relations:
  evaluation_for:
    - CA-D-435
    - CA-R-807
---
# Validate Atom replacement event evidence

an Atom replacement event Evaluation **must** reject a violation of CA-D-435's paired identity encoding **or** CA-R-807's active-successor binding. format checks **must** accept a valid archive `MOVE` with distinct successor identities **and** reject missing, null, malformed, duplicate, self-referencing, mismatched-predecessor, mismatched-Version, **or** wrongly placed replacement fields; a changed payload with an unchanged digest **must** fail. ordinary historical records **without** replacement fields **must** retain their previous validation behavior, **and** replay of the same sealed Event **must** reuse its canonical receipt rather than append another record.

the replacement check **must** also verify that **every** named successor is already Active **before** the predecessor is archived, that the archived predecessor preserves its exact prior bytes **and** Version, **and** that the archiving Event names the same predecessor **and** successors. successful format validation alone **must not** be reported as evidence of those state conditions; missing **or** unresolved state evidence blocks a successful replacement result. these fixtures test the registered replacement payload **and** its authoritative binding, **not** independent replacement history **or** a second Journal.
