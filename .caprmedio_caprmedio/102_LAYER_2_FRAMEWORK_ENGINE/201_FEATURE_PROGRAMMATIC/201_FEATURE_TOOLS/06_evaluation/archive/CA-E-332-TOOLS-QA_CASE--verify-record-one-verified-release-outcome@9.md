---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "release"
  depends_on: []
version: 9
updated_at: 2026-09-15 05:51:38
relations:
  evaluation_for:
    - CA-M-214
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify record one verified release outcome

## Claim checked

CA-M-214 creates a Release Record only for a fully verified successful outcome and records failed attempts only as non-release Operations evidence.

## Applicable when

Apply whenever release outcome recording or release acceptance criteria change.

## Test case

Use two distinct sealed release-attempt identities for the same version and manifest: one missing a required verification result and one containing all passing results with exact revisions, Work Journal event, and canonical Git identity.

## Acceptance criteria

The incomplete attempt produces no Release Record and creates exactly one non-release Operations evidence carrier binding its attempted version, exact revision, checks, and Work Journal event. The complete attempt produces exactly one immutable Release Record binding every required identity, revision, check, evidence, Work Journal event, and Git fact.

## Failure disposition

Reject the realization and preserve both attempt frontiers, criteria, evidence maps, emitted Operations carriers, and duplicate-release scan.
