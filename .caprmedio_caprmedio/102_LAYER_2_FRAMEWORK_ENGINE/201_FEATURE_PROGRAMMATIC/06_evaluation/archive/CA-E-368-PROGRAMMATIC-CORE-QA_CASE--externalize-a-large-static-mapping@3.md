---
atom_id: CA-E-368
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - static-mapping
  depends_on:
    continuant:
      - programmatic software
version: 3
updated_at: 2026-09-01 02:15:00 +0400
relations:
  evaluation_for:
    - CA-M-162
  derived_from:
    - CA-A-053
---
# Externalize a large static mapping

## Claim checked

One large reusable static mapping is stored outside a hand-authored Python
module while its loader retains a typed, validated boundary.

## Test case

Evaluate one changed Python module containing a static mapping above 20 entries
or 25 source lines.

## Acceptance criteria

Pass only when the mapping is moved to TOML by default, JSON for a schema or
machine-interchange need, or YAML for one declared distinct feature; its loader
must validate the expected structure without changing the mapping's meaning.

## Failure disposition

Reject the source-size claim until data and executable behavior are separated.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Python documentation: `json`](https://docs.python.org/3.14/library/json.html)
