---
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 19
updated_at: "2026-09-17 05:10:56 +0000"
relations: {"child_of":["CA-R-1698","CA-R-1502","CAPRMEDIO-REQU-686-CORE-REQUIREMENT--separate-core-extension-and-project-configuration-authority"]}
atom_id: "CA-R-1769"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 10
---
# Select Methodology Source revisions explicitly

a Project **must** apply a Methodology Source update **or** downgrade **only** by selecting an identified source revision **and** reconciling affected Project authority; the selection **must not** silently rewrite other Methodology Sources **or** Project-owned Atoms.
