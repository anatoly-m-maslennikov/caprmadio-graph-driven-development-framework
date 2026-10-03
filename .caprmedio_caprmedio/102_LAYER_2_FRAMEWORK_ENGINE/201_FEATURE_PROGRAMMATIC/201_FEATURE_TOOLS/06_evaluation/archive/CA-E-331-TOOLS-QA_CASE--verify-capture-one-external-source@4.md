---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - provenance
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-213
---
# Verify capture one external source

## Claim checked

CA-M-213 captures one immutable external source carrier with complete provenance and an explicit reproducibility result.

## Applicable when

Apply whenever external-source capture or provenance-carrier mechanics change.

## Test case

Capture one supplied external text with origin, retrieval time, attribution, and content digest. Attempt a second capture lacking attribution and inspect both outcomes.

## Acceptance criteria

The valid capture creates one immutable carrier whose bytes match its digest and records the required provenance and reproducibility outcome. The incomplete capture produces no carrier and no invented provenance.

## Failure disposition

Reject the source-capture method and preserve both capture inputs, carrier bytes, digest comparison, recorded provenance, reproducibility result, and rejection evidence.
