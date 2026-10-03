---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "release"
  depends_on:
    - "Journal/Record"
    - "Artifact/Revision"
version: 14
updated_at: "2026-09-17 20:09:16 +0000"
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

use three distinct sealed release-attempt identities for the same version **and** manifest, with exact revisions, Work Journal event, **and** canonical Git identity:

- one is missing a required verification result;
- one contains **all** required passing results;
- one contains complete evidence that fails a declared required release-acceptance criterion.

## Acceptance criteria

**all** of the following conditions **must** hold:

- the incomplete attempt records no release success **and** creates **=1** Journal Record identifying the observed missing verification, binding its attempted version, exact revision, checks, **and** Work Journal event. missing verification alone **must not** produce a failed-release claim.
- the complete passing attempt produces **=1** immutable Journal Record of verified release success binding **every** required identity, revision, check, evidence, Work Journal event, **and** Git fact.
- the evidenced failed attempt produces **=1** Journal Record of a failed non-release attempt, retains its exact attempted version, Revision, failed criterion, checks, **and** Work Journal event, **and** produces no successful-release claim.

## Failure disposition

reject the realization **and** preserve **all** attempt frontiers, criteria, evidence maps, emitted Journal Records, **and** duplicate-release scan.
