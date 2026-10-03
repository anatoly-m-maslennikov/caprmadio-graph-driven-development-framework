---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "python-idiom-adoption"
  depends_on:
    - "programmatic software"
version: 6
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  evaluation_for:
    - CA-M-280
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Require a declared benefit for one new Python idiom

## Claim checked

A runtime-dependent Python idiom is admitted **only** for a named benefit inside
the supported boundary.

## Test case

Replace an immediate trusted f-string with a t-string while providing no
interpolation processor **or** other correctness, clarity, safety, **or** measured
performance benefit.

## Acceptance criteria

pass **only** **when** the change is rejected **and** the simpler supported idiom remains.

## Failure disposition

Reject novelty alone as a benefit **and** return the selection **to** CA-M-280.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [CA-M-280 — Adopt current Python idioms only for declared benefit](../05_method/CA-M-280-PROGRAMMATIC-CORE-METHOD--adopt-current-python-idioms-only-for-declared-benefit.md)
