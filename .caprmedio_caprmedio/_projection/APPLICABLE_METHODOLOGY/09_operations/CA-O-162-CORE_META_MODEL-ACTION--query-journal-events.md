---
atom_id: CA-O-162
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 01:20:00 +0400"
subjects:
  governs: "Journal Event query"
  depends_on: [Journal, Event, Tool, Action Run]
relations:
  relates_to: [CA-O-161, CA-O-163, CA-R-1850, CA-R-1861, CA-R-1862, CA-R-1863, CA-R-1864, CA-R-1865, CA-R-1866, CA-R-1867, CA-R-1868, CA-R-1869, CA-R-1870, CA-R-1871, CA-R-1872, CA-M-334, CA-M-335, CA-M-336, CA-M-337, CA-E-575, CA-E-576, CA-E-577, CA-E-578, CA-E-579, CA-E-580, CA-D-555, CA-D-556, CA-D-557, CA-D-558]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-162-CORE_META_MODEL-ACTION--query-journal-events.md
  source_atom_id: CA-O-162
  source_atom_revision: 2
  source_sha256: 71301ecf9531c70adeba03d6cf7f39761a237a081cee43eb0f9f7ce40e12f9fe
  original_relations_sha256: 5e7db52619c9d61f26949bc8416eeb3832b24568764946912fcba9ad333f3e07
---
# Summary

Query Journal Events

## Operation

The Journal Event query Action **must** read one stable snapshot of the selected Project's canonical Events Journal, evaluate only its bounded literal filter grammar, and return Event IDs by default or only caller-selected Event fields or full Events on request.

## Details

The Action consumes the exact pre-dispatch sealed byte-prefix frontier. A
standalone Action captures that frontier before its own Run evidence.

The Action reuses CA-R-1850's one shared literal filter grammar. It neither writes Events nor creates a competing Journal, Projection, SQL interpreter, arbitrary-code evaluator, credential reader, mutation authority, or invented Run. It reports exact malformed, missing, duplicate, incomplete, changed-source, coverage, pagination, and filter diagnostics rather than skipping or passing them.
