---
subjects:
  governs: "CAPRMEDIO Routing Tree"
  depends_on: []
version: 5
updated_at: "2026-09-17 15:07:45 +0000"
relations: {"evaluation_for":["CA-R-1640"]}
atom_id: "CA-E-483"
content_role: "Evaluation"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation"
global_tier: 10
---
# Validate the routing tree

the Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640 **must** reject a routing tree **when** **any** of the following is present:

- an invalid schema;
- an unknown target;
- ambiguous precedence;
- a duplicate route identity;
- an authority effect that is **not** explicitly declared.
