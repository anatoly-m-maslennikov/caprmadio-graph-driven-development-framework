---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Projection/Carrier"
  depends_on: []
version: 8
updated_at: 2026-09-23 04:25:00 +0400
relations:
  evaluation_for:
    - CA-R-1386
    - CA-R-1387
    - CA-M-259
    - CA-R-1076
    - CA-R-1077
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Persist one Projection without mutating authority

## Test case

Run description **and** ordinary generation **without** a destination; persist **to** one explicit valid Projection destination; repeat through one registered destination; **then** attempt an ambiguous destination, path traversal, symlink escape, **and** destinations inside Atom **and** Journal authority. Let `GRAPH_SERVER` read the valid result **and** optionally let `GRAPH_UI` present it.

## Acceptance criteria

**only** the explicit **or** unambiguous registered persistence replaces exactly one Projection Carrier atomically. Every authority **and** Journal byte remains unchanged. Invalid destinations fail **without** partial output. `GRAPH_SERVER` exposes the Projection read-only with its source lineage **and** non-authoritative status; optional `GRAPH_UI` presentation does not change that status; neither can use it as authority **or** mutate it.
