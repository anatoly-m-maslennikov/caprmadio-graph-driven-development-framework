---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "provenance"
  depends_on: []
version: 9
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-213
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify capture one external source

## Claim checked

CA-M-213 captures one immutable external source carrier with complete provenance **and** an explicit reproducibility result.

## Applicable when

apply whenever external-source capture **or** provenance-carrier mechanics change.

## Test case

capture one supplied external text with origin, retrieval time, attribution, **and** content digest. attempt a second capture lacking attribution **and** inspect both outcomes.

## Acceptance criteria

the valid capture creates one immutable carrier whose bytes match its digest **and** records the required provenance **and** reproducibility outcome. the incomplete capture produces no carrier **and** no invented provenance.

## Failure disposition

reject the source-capture method **and** preserve both capture inputs, carrier bytes, digest comparison, recorded provenance, reproducibility result, **and** rejection evidence.
