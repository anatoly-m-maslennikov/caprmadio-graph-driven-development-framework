---
subjects:
  governs: "Governed Change/Change Class"
  depends_on:
    - "Artifact/Carrier"
    - "Relation"
version: 11
updated_at: "2026-09-17 21:32:33 +0000"
relations:
  evaluation_for:
    - CA-R-805
    - CA-M-087
    - CA-R-804
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Classify content change as UPDATE

## Claim checked

a content change **to** one governed file identity **without** Structural relocation is classified **only** as `UPDATE`.

## Test case

supply a trigger for one identity whose governed content **and** resulting version change while its filename **and** Structural location remain unchanged.

## Acceptance criteria

the sealed context reports `UPDATE`, names the resulting version, **and** resolves upstream relations from the observed candidate result graph bound into the provisional context.

## Failure disposition

reject classification **and** report **any** added `MOVE` flag, preserved old version, **or** incorrect relation source.

## Observation boundary

the candidate result graph is a read-**only** description of the observed change, **not** an instruction **to** stage it. capture **any** existing Git index separately; do **not** assume that the final gate already staged the candidate. COMMIT_CONTEXT performs no index mutation **and** grants no Git effect permission. COMMIT_CHANGE_SET alone stages the admitted target **and** revalidates its actual complete staged set at the effect boundary under CA-R-805.
