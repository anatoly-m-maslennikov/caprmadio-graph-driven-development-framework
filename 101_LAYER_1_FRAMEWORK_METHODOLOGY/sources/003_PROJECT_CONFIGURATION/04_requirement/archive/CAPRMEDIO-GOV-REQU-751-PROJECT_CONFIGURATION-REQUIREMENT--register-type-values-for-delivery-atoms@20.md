---
subjects:
  governs: "Atom/Content Role: Delivery/Type"
  depends_on: []
project_graph_state:
  artifacts:
    enabled_types:
      - delivery:release_definition
      - delivery:environment_definition
version: 20
updated_at: "2026-09-11 23:47:49 +0400"
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
atom_id: "CAPRMEDIO-GOV-REQU-751"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
type: "Requirement"
---
# Register Type Values for Delivery Atoms

Release Definition **and** Environment Definition **must** be registered as internal values of `Atom/Content Role: Delivery/Type`.
