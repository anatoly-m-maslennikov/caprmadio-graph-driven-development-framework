---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-query
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-243
---
# Verify query generic Artifacts by filters

## Claim checked

CA-M-243 returns every and only generic Artifact IDs and paths selected by composable supported filters in stable order without loading bodies.

## Applicable when

Apply whenever generic Artifact filters, canonical identity selection, or stable query ordering changes.

## Test case

Construct a bounded Artifact frontier spanning structural scopes, layers, Tiers, Features, Content roles, subject scopes, lifecycle states, and typed relations, with body-only sentinels. Apply one composable filter set with known membership, then add one unsupported filter.

## Acceptance criteria

The supported query returns only the expected canonical IDs and paths once in stable order, with no body sentinel accessed or returned. The unsupported-filter query returns an explicit diagnostic and no partial accepted result.

## Failure disposition

Reject the realization and preserve the frontier, filters, expected membership and order, body-access evidence, and unsupported-filter diagnostic.
