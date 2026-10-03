---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Projection/Carrier"
  depends_on: []
version: 6
updated_at: 2026-09-12 04:15:38 +0400
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

Run description **and** ordinary generation **without** a destination; persist **to** one explicit valid Projection destination; repeat through one registered destination; **then** attempt an ambiguous destination, path traversal, symlink escape, **and** destinations inside Atom **and** Journal authority. Let `GRAPH_APP` read the valid result.

## Acceptance criteria

Only the explicit **or** unambiguous registered persistence replaces exactly one Projection Carrier atomically. Every authority **and** Journal byte remains unchanged. Invalid destinations fail **without** partial output. `GRAPH_APP` exposes the Projection read-only with its source lineage **and** non-authoritative status **and** cannot use it as authority **or** mutate it.
