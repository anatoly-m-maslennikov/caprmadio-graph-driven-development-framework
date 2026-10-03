---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on:
    - "Artifact"
    - "Artifact/Carrier"
version: 9
updated_at: "2026-09-17 21:58:14 +0000"
relations:
  evaluation_for:
    - CA-M-207
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify read generic Artifact metadata

## Claim checked

CA-M-207 returns attributable body-free metadata **and** derived identity for **=1** generic Artifact under its admitted Carrier schema, **without** hiding absent fields **or** malformed input.

## Applicable when

apply **when** generic metadata extraction **or** Carrier-identity derivation changes.

## Test cases

- select an admitted Artifact Carrier with a known body-only sentinel, one present requested field **and** one absent requested field. independently establish its full-source digest.
- read the selected metadata **and** derived identity; repeat with malformed frontmatter **and** ambiguous Carrier identity.

## Acceptance criteria

- the valid result includes the requested present field, an explicit absent-field result, correct derived identity **and** the source digest required by CA-M-207.
- body bytes **may** be streamed **to** compute **or** verify that digest. the body is **not** parsed as metadata, materialized as the returned body, **or** used **to** fill an absent field; the sentinel is **not** returned as content. digest inclusion is **not** body disclosure.
- malformed frontmatter **and** ambiguous identity produce explicit results **without** changing the Carrier **or** other Project state.

## Failure disposition

reject incorrect metadata, hidden absence **or** errors, a mismatched source digest, body-content leakage **or** mutation. preserve the Carrier identity, requested fields, expected metadata, independent digest, diagnostics **and** returned payload evidence.
