---
subjects:
  governs: "Atom/Content Role: Concern/Type"
  depends_on: []
project_graph_state:
  artifacts:
    enabled_types:
      - concern:question
      - concern:problem
      - concern:risk
      - concern:opportunity
version: 21
updated_at: "2026-09-11 23:47:49 +0400"
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
atom_id: "CAPRMEDIO-GOV-REQU-749"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Register Type Values for Concern Atoms

Question **and** Problem retain their canonical admission under CA-R-1231. Risk **and** Opportunity **must** be registered as additional internal values of `Atom/Content Role: Concern/Type`.
