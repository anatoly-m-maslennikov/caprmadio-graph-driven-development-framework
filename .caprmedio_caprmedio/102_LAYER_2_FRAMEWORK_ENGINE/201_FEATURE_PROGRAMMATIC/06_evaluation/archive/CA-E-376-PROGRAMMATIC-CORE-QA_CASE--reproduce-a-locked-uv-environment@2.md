---
atom_id: CA-E-376
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - python-workflow-reproduction
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-221
  derived_from:
    - CA-A-053
---
# Reproduce a locked uv environment

## Claim checked

One admitted PROGRAMMATIC Python environment and governed command are
reproduced from the selected Python boundary, `pyproject.toml`, and
`uv.lock` without implicit dependency changes.

## Test case

From an empty project environment, run `uv sync --locked` and then one declared
command through `uv run --locked`.

## Acceptance criteria

Pass only when the locked sync and command complete without changing
`pyproject.toml` or `uv.lock` and use only Method-selected dependencies.

## Failure disposition

Reject the reproducibility claim when the lock is stale, resolution changes
implicitly, or a dependency lacks Method authority.

## Sources

- [CA-M-221 — Use uv as the default Python workflow frontend](../05_method/CA-M-221-PROGRAMMATIC-CORE-METHOD--use-uv-as-the-default-python-workflow-frontend.md)
