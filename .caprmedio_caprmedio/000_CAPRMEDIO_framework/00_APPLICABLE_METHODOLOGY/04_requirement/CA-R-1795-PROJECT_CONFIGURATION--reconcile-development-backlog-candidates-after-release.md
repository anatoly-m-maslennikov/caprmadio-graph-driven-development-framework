---
subjects:
  governs: "development-flow"
  depends_on: []
version: 1
updated_at: "2026-09-30 15:04:20 +0400"
relations: {"depends_on": ["CA-O-058", "CA-R-1702"]}
atom_id: "CA-R-1795"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1795-PROJECT_CONFIGURATION--reconcile-development-backlog-candidates-after-release.md
---
# Summary
Reconcile Development Backlog candidates **after** release

## Scope
Development Backlog candidates **after** a Release Record is accepted.

## Claim

CAPRMEDIO **must** reconcile the Development Backlog against its exact released manifest as follows:

- remove a candidate whose promoted Atoms were fully delivered **in** that release.
- **every** candidate that is unfinished, partially delivered, excluded, **or** newly deferred **must** remain unscheduled **or** move **to** another target version.
- a candidate **must not** be removed as shipped **unless** the released manifest accounts for its promoted Atoms.

## Details
