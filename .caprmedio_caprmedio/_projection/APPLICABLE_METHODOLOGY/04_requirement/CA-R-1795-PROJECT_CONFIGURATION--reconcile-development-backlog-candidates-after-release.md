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
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1795-PROJECT_CONFIGURATION--reconcile-development-backlog-candidates-after-release.md
  source_atom_id: CA-R-1795
  source_atom_revision: 1
  source_sha256: a0ddb8b86bcc95ff08ef92336cbc24bd71be5c9fe71710531d4c03121348d6d0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
