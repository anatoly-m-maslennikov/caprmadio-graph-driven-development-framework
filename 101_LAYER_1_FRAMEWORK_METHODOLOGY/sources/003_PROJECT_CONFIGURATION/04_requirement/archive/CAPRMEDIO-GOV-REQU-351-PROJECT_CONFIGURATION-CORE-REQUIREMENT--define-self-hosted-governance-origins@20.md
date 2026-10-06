---
subjects:
  governs: "Governance Origin"
  depends_on:
    - "Project"
    - "Artifact"
    - "CAPRMEDIO Framework"
    - "Project Configuration"
version: 20
updated_at: "2026-09-17 12:44:19 +0000"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-351"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Define self-hosted Governance origins

Governance Origin for the self-hosted caprmedio Project **and** its distributed CAPRMEDIO sources follows the ownership distinction **in** CAPRMEDIO-META-REQU-127:

- within the caprmedio Project, its Project-owned Methodology authority, framework authority, **and** other Project-owned Artifacts have internal Governance Origin.
- a distributed CAPRMEDIO framework source has external Governance Origin relative **to** a consuming Project. that Project's own adaptation authority has internal Governance Origin; creating it does **not** transfer ownership of the external source **or** change that source's origin.
- graph Relations, version-control authorship, filesystem ownership, **and** byte identity do **not** replace the governing ownership distinction.
