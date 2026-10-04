---
atom_id: CA-R-1832
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:31 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE result reporting"
  depends_on: [Tool, Scope Unit, Project Structure, Workflow Run, Journal]
relations:
  relates_to: [CA-R-1829, CA-R-1831, CA-O-144]
---
# Summary

Report structural change result and breakage

## Scope

The result boundary after CA-O-143 cutover and CA-O-144 assessment.

## Claim

The Tool **must** return exact outcome, current declaration revision, actual effects, and complete preservation/breakage disposition without representing a source definition or preview as an executed change.

## Details

- Output includes operation, requested and resulting Scope Unit identity/parent/paths, pre/post TOML revisions, authorization revision, affected and repaired references, preserved Carriers, explicit breakages, validation evidence, recovery disposition, and available Workflow/Action Run and Journal references.
- `completed` is returned only after required assessment checks accept actual effects. `rolled_back` identifies the restored set and any remaining breakage. `partial` and all blocked outcomes remain terminally truthful and machine-readable.
- The result must distinguish absent evidence, failed evidence recording, and a failed structural operation; it must not manufacture a successful no-op, rollback, or journal receipt.
