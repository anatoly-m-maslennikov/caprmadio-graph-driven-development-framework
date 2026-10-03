---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "release"
  depends_on:
    - "Journal/Record"
    - "Artifact/Revision"
version: 13
updated_at: "2026-09-17 20:06:16 +0000"
relations:
  evaluation_for:
    - CA-M-214
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify record one verified release outcome

## Claim checked

CA-M-214 records verified release success **only** for a fully verified successful outcome **and** records failed attempts **only** as Journal evidence of failed non-release attempts.

## Applicable when

apply whenever release outcome recording **or** release acceptance criteria change.

## Test case

use two distinct sealed release-attempt identities for the same version **and** manifest: one missing a required verification result **and** one containing **all** passing results with exact revisions, Work Journal event, **and** canonical Git identity.

## Acceptance criteria

the incomplete attempt records no release success **and** creates **=1** Journal Record of a failed non-release attempt binding its attempted version, exact revision, checks, **and** Work Journal event. the complete attempt produces **=1** immutable Journal Record of verified release success binding **every** required identity, revision, check, evidence, Work Journal event, **and** Git fact.

## Failure disposition

reject the realization **and** preserve both attempt frontiers, criteria, evidence maps, emitted Journal Records, **and** duplicate-release scan.
