---
subjects:
  governs: "CAPRMEDIO Routing Tree"
  depends_on:
    - "CAPRMEDIO Main Skill"
    - "CAPRMEDIO Direct Route Skill"
    - "Project Configuration"
version: 15
updated_at: "2026-09-17 12:43:59 +0000"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-336"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Resolve skill routing precedence

Skill routes **must** resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.
