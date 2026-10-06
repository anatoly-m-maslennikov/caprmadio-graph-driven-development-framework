---
subjects:
  governs: "Work Journal/Event/Carrier Serialization"
  depends_on:
    - "Journal/Record"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
version: 4
updated_at: "2026-09-17 02:23:47 +0000"
relations:
  evaluation_for:
    - CA-D-435
    - CA-D-339
---
# Validate replacement Event schema encoding

## Claim checked

the selected schema-version `3` replacement Event Carrier satisfies CA-D-435 **without** treating Project conformance as storage integrity.

## Cases

1. encode a completed File Carrier `MOVE` event with paired string predecessor **and** array-of-string successor fields; preserve the supplied successor order.
2. keep that envelope valid **and** vary the observed IDs: canonical, legacy, nonconforming, duplicate, self-referencing, **or** an empty successor array. also vary the result filename **or** archive placement independently of the safe Event path encoding.
3. omit **only** one paired field, supply null **or** the wrong storage type, use a schema **or** Event kind that does **not** define the pair, **or** change the payload **without** updating its digest.
4. replay an identical sealed Event; **then** submit a different payload under the same Event identity.
5. validate an ordinary historical record **without** replacement fields.

## Acceptance

- cases 1 **and** 2 remain recordable with the supplied values unchanged. case 2 **may** fail CA-E-462 independently; its conformance verdict **must not** prevent recording under CA-R-1491.
- case 3 fails the selected encoding **or** integrity check **without** changing accepted history.
- the identical replay reuses the existing receipt **without** a duplicate record; an identity collision with a different payload fails **without** overwriting history.
- case 5 retains its selected historical schema. passing this Evaluation does **not** prove active successors, exact archive preservation, valid Project identifiers, valid placement, **or** a correctly performed replacement.
