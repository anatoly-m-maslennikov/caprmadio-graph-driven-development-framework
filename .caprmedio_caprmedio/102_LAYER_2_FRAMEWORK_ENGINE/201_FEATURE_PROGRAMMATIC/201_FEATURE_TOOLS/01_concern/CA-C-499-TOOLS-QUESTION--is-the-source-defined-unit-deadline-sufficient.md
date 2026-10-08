---
atom_id: CA-C-499
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 14:06:13 +0000"
subjects:
  governs: "Release Unit deadline sufficiency"
  depends_on: [Framework Instance Settings, Test Suite, Source Carrier, Evaluation, Workflow Run]
relations:
  concern_about: [CA-P-1792, CA-P-1782, CA-D-579, CA-D-580]
---
# Summary

Is the source-defined Unit deadline sufficient

## Concern

does a source-sealed default of 3600 seconds, bounded by 7200 seconds and configurable through the Framework Instance, permit the complete Unit partition to finish without omitting tests or weakening timeout and currentness gates?

## Evidences

- N10 actual receipt outcome is timed_out after 934.4613934169975 seconds under the existing code-only 900-second ceiling. there is no complete JUnit/coverage report; its zero validated count does not mean zero execution.
- the full local image fixture module alone passed 53 tests in 862.154 seconds.
- actual N10 interruption receipts exist for Action, Step and Workflow. no candidate image, promotion or retirement occurred; installed N remains unchanged.

## Blast radius

only the source-owned Unit deadline, its exact existing settings carriers, private reference closure, resolver and bounded executor. preserve all Unit modules, the three separate Candidate E2E harnesses, public schemas and historical events.

## Details

choose the provisional finite default under the Operator's autonomous best-option authorization, implement it source-first with independent review, and require actual complete fresh-gate evidence. do not claim sufficiency from the number alone or replay failed N10.
