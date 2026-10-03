---
atom_id: CA-E-376
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "python-workflow-reproduction"
  depends_on:
    - "programmatic software"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-221
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
