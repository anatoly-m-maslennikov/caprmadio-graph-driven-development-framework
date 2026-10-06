---
subjects:
  governs: "Governance Origin"
  depends_on:
    - "Project"
    - "Artifact"
    - "CAPRMEDIO Framework"
    - "Project Configuration"
version: 21
updated_at: "2026-10-03 01:31:08 +0400"
relations: {}
atom_id: "CA-R-1645"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1645-PROJECT_CONFIGURATION-CORE-REQUIREMENT--define-self-hosted-governance-origins.md
  source_atom_id: CA-R-1645
  source_atom_revision: 21
  source_sha256: d30360299aee4ce0444394f6f957ff28d9916f6ac0084adf9bd41dccf3ae3146
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define self-hosted Governance origins

## Scope

Governance Origin for the self-hosted caprmedio Project and its distributed CAPRMEDIO sources.

## Claim

Governance Origin for the self-hosted caprmedio Project **and** its distributed CAPRMEDIO sources follows the ownership distinction **in** CA-R-1709-CORE_META_MODEL-CORE-REQUIREMENT--define-two-governance-origins:

- within the caprmedio Project, its Project-owned Methodology authority, framework authority, **and** other Project-owned Artifacts have internal Governance Origin.
- a distributed CAPRMEDIO framework source has external Governance Origin relative **to** a consuming Project. that Project's own adaptation authority has internal Governance Origin; creating it does **not** transfer ownership of the external source **or** change that source's origin.
- graph Relations, version-control authorship, filesystem ownership, **and** byte identity do **not** replace the governing ownership distinction.

## Details
