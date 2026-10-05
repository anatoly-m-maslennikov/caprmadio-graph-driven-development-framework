---
atom_id: "CA-R-1780"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Logging Policy"
  depends_on: []
version: 1
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1780-PROJECT_CONFIGURATION--define-production-log-severity-meanings.md
  source_atom_id: CA-R-1780
  source_atom_revision: 1
  source_sha256: cdb9934a8b63b9b945a7bc8e72b3928c7510d644267575b1ea0984179364dd8a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define production log severity meanings

## Scope

Logging Policies for production-relevant components.

## Claim

a Logging Policy **must** use these four operational levels:

| Level | Required meaning |
|---|---|
| `ERROR` | an operation failed, correctness **or** availability **may** be affected, **or** explicit retry **or** intervention is required |
| `WARNING` | behavior was unexpected **or** degraded but recovered, fell back, **or** remains within an accepted tolerance |
| `INFO` | a material lifecycle, business, **or** operational milestone occurred, including start, stop, acceptance, state transition, completion, **or** summarized progress |
| `DEBUG` | sanitized internal state **or** decision detail is useful for bounded investigation but is unnecessary during normal production operation |

## Details

the four level meanings are one taxonomy **and** retain one lifecycle as a set.
