---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-1121

---
# Reject an invalid staged governed commit

## Claim checked

The Git gate accepts a real-change boundary only when its staged target set exactly matches one sealed action and its Initiative message projection.

## Test case

Present the gate with an unresolved target, stale expected revision, a Journal carrier mixed with a real-change target, two atomic targets, an incomplete bulk target set, and one valid sealed target set.

## Acceptance criteria

Each invalid state returns one stable diagnostic before commit creation. The valid state creates only the sealed real-change target commit and does not require a Journal record or Journal carrier in the index.

## Failure disposition

Reject the delivery if an invalid boundary passes, a valid boundary fails, or preflight mutates repository state.
