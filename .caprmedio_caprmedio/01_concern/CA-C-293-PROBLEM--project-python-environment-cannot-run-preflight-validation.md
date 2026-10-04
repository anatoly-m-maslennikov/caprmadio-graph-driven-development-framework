---
atom_id: CA-C-293
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Project/verification environment"
  depends_on:
    - "Project"
    - "Implementation"
    - "Atom/Content Role: Plan"
relations:
  concern_about:
    - CA-P-1150
    - CA-P-1175
version: 1
updated_at: "2026-10-04 06:42:47 +0400"
---
# Summary

Project Python environment cannot run preflight validation

## Concern

The current Project Python environment cannot execute the intended PyYAML-based structural verification for CA-P-1150. This is an actual runtime verification failure, not missing app metadata or a failed harvest. Do not represent a narrower fallback as a full YAML/parser validation.

## Evidences

- `uv run --locked python` reported: `Project virtual environment directory .../.venv cannot be used because it is not a valid Python environment (no Python executable was found)` and a project environment-lock warning.
- Available system `/opt/homebrew/bin/python3` reported `ModuleNotFoundError: No module named 'yaml'` when checked for the parser.
- A single isolated `uv run --no-project --with pyyaml` attempt failed with cache rename `Operation not permitted (os error 1)` under `.caprmedio_tmp/cache/uv`. No additional installation, permission retry or environment repair was performed.
- App metadata listing independently succeeded: 20 recent records plus 6 pinned records, no unavailable host/source reported. This Problem does not invalidate those source IDs.

## Blast radius

The failure limits parser-backed preflight verification and may affect future Project Python checks. No implementation code, dependency declarations, environment or permissions were changed. Current disposition: nonblocking for metadata preparation because system Python standard-library checks can verify saved IDs, required headings, explicit Properties, Carrier placement and the declared completion graph. Full YAML/parser validation remains unverified. Keep this Concern Active for later separately authorized environment repair; it is not an added prerequisite to CA-P-1175's bounded metadata-only discovery. The main Agent owns any eventual Git save; no Journal/save-Tool receipt is fabricated here.
