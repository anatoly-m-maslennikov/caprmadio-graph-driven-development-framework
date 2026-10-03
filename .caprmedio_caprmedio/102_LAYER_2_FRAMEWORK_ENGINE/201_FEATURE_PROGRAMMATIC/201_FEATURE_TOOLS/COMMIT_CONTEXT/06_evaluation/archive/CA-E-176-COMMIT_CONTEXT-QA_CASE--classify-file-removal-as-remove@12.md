---
subjects:
  governs: "Governed Change/Change Class"
  depends_on:
    - "Artifact/Carrier"
    - "Journal"
    - "Artifact/Revision"
version: 12
updated_at: "2026-09-17 21:32:41 +0000"
relations:
  evaluation_for:
    - CA-R-1491
    - CA-M-087
    - CA-R-804
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Classify file removal as REMOVE

## Claim checked

removal of a governed file identity with no resulting Carrier for that file is classified as `REMOVE`. disappearance from the active address alone does **not** establish removal **when** the file moved **to** another address, including an archive.

## Test case

supply a sealed observation whose preceding graph contains the governed file **and** whose candidate result has no Carrier for that file identity. separately include an unchanged file relocated **to** an archive as a control. observe **any** existing Git index separately; context gathering **must** **not** stage **or** remove files.

## Acceptance criteria

- the removal context reports `REMOVE` **and** emits the removed-state result with filename **and** Version, **without** present-**only** path **or** Digest.
- previous_result_event refers **to** the immediate preceding present result; authored Relations are resolved from the last committed graph **without** copying redundant **before**-state fields into the result.
- the archive control is classified as `MOVE` rather than `REMOVE`. historical evidence **and** replacement IDs, **when** applicable, retain their separate registered Journal rules.
- no classification changes the Project **or** certifies conformance of the observed removal.

## Failure disposition

reject an incorrect change class, malformed tombstone, missing predecessor reference, lost observation, copied **before**-state field, mutation **or** incorrect Relation source.
