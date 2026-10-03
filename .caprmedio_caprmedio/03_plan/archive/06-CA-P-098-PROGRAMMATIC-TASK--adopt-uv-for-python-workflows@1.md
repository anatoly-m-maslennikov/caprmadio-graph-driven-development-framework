---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - python-toolchain
      - development-environment
    occurrent:
      - environment-reproduction
version: 1
updated_at: 2026-08-25 14:16:00 +0400
autonomous_confidence_threshold: 98
relations:
  derived_from:
    - CA-A-062
---
# Adopt uv for Python workflows

WHEN a governed Python workflow uses a capability provided by `uv`, THE
Assignee MUST promote the accepted draft Method and apply `uv` as the default
development, evaluation, and authorized packaging frontend.

## Scope

Python installation and selection, the project environment, dependency
declaration and locking, synchronization, command execution, isolated Tool
execution, and separately authorized build or publication workflows.

## Definition of Done

THE Task is NOT DONE IF (the current draft Method remains the only owner OR
`pyproject.toml` and a reviewed `uv.lock` cannot reproduce the admitted Python
environment with the supported `3.14.*` series OR governed commands require an
undeclared overlapping environment manager OR evidence collection can update
the environment implicitly OR an exception lacks its accepted capability and
recovery boundary OR installed CAPRMEDIO Tools require `uv`, a project virtual
environment, or another dependency outside `.caprmedio_install`).

## Details

Use `uv python`, `uv add` or `uv remove`, `uv sync --locked`, `uv run --locked`,
version-pinned `uv tool run`, and authorized `uv build` or `uv publish` only for
the capabilities each command owns. Keep Project settings, runtime state, Git
authority, and installed Tool execution outside the `uv` ownership boundary.
