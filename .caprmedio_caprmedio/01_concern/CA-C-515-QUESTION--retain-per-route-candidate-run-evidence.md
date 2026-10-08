---
atom_id: CA-C-515
content_role: Concern
type: Question
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 20:24:00 +0000"
subjects:
  governs: "Per-route candidate Run evidence retention"
  depends_on: [Workflow, Action, Journal, Source Carrier, Evaluation]
relations:
  concern_about: [CA-P-1816, CA-P-1124]
---
# Summary

Retain per-route candidate Run evidence

## Concern

how should the final matrix retain exact per-route native Run and Journal evidence when the accepted harness cleans up disposable fixtures?

## Evidences

the current three-harness receipt retains aggregate/JUnit evidence but not native per-route IDs and result carriers. the harness checks those carriers before normal fixture cleanup.

## Blast radius

final traceability only; this does not alter the candidate, source model, execution or acceptance predicates.

## Decision

choose a bounded read-only capture of completed fixture evidence before cleanup under the existing Epic autonomy envelope. retain exact bytes, provenance and definition identities; collect no request/environment/source tree or secret. require independent collector review and actual captures before claiming this gap resolved.
