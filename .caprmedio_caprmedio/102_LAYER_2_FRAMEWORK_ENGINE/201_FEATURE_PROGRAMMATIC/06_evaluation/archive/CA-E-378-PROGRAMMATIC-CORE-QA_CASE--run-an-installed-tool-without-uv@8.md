---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "installed-python-runtime"
  depends_on:
    - "programmatic software"
version: 8
updated_at: 2026-09-15 03:15:32 +0400
relations:
  evaluation_for:
    - CA-M-221
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Run an installed Tool without uv

## Claim checked

one installed CAPRMEDIO Tool executes from `.caprmedio_runtime/tools` **without** uv, a
project virtual environment, **or** another dependency outside the selected
runtime release.

## Test case

invoke one installed Tool **in** a clean process **where** uv **and** the project virtual
environment are unavailable.

## Acceptance criteria

pass **only** **when** the Tool reaches its declared entry boundary using solely its
installed carrier **and** admitted host prerequisites.

## Failure disposition

reject the installed-runtime claim **until** the external workflow dependency is
removed.

## Sources

- [CA-M-221 — Use uv as the default Python workflow frontend](../05_method/CA-M-221-PROGRAMMATIC-CORE-METHOD--use-uv-as-the-default-python-workflow-frontend.md)
