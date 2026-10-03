---
atom_id: CA-E-385
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - python-static-typing
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-231
  derived_from:
    - CA-A-053
---
# Verify changed Python with Mypy

## Claim checked

New Python passes the strict admitted Mypy profile and changed Python does not
regress below its passing baseline.

## Test case

Add one incompatible return type and one unexplained broad suppression to a
changed target in the admitted Mypy set.

## Acceptance criteria

Pass only when both defects are reported and the target is rejected.

## Failure disposition

Reject the changed target until types agree or a narrow explained suppression
is accepted.

## Sources

- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-M-231 — Use Mypy for static Python type checking](../05_method/CA-M-231-PROGRAMMATIC-CORE-METHOD--use-mypy-for-static-python-type-checking.md)
