---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - programmatic-source
      - source-architecture
      - project-settings
    occurrent:
      - conformance-ratchet
version: 1
updated_at: 2026-08-25 14:18:00 +0400
autonomous_confidence_threshold: 98
relations:
  derived_from:
    - CA-A-053
    - CA-A-062
---
# Establish the PROGRAMMATIC source conformance baseline

WHEN the current shared PROGRAMMATIC Methods and their Feature specializations
are active, THE Assignee MUST measure current hand-authored source and establish
the first accepted conformance baseline without applying TOOLS-only structure
blindly to APPS or MCP.

## Scope

Current hand-authored source under `002_FRAMEWORK_ENGINE/PROGRAMMATIC`, shared
settings access, reusable non-Python assets, logging and diagnostics, typed
technical boundaries, and generated Python cache state in source locations.

## Definition of Done

THE Task is NOT DONE IF (the measured source frontier is absent OR current
violations of accepted shared or Feature-local Methods lack an explicit repair
or accepted bounded exception OR files are not ratcheted toward 200 lines OR
functions and other atomic objects are not ratcheted toward 25 lines with only
coherent 26-to-40-line exceptions OR Tool managers perform I/O or workers own
policy decisions OR reusable large dictionaries and assets remain embedded in
Python without necessity OR Tools read settings through multiple independent
control paths OR untrusted structured boundaries lack their accepted runtime
validation OR operational diagnostics lack declared levels and correlation OR
generated files are treated as distributive source OR any `__pycache__` remains
under governed source directories).

## Details

Centralize reusable Tool settings access behind one settings reader backed by
the accepted `.caprmedio` Project settings authority. Keep deterministic
transformations separate from effects and lifecycle; allow a worker to signal
one fixed next handoff when no decision is delegated, but keep branching and
policy in the manager. Apply Pydantic only at accepted untrusted structured
boundaries, preserve the standard-library-first runtime contract, and use
typing, linting, focused checks, profiling, and Evaluation evidence as a
ratchet. Do not run the suspended repository test suite merely to claim this
Task complete.
