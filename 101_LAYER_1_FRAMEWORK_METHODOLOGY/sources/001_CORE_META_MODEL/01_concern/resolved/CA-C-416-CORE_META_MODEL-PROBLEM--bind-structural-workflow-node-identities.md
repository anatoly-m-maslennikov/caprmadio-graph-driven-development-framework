---
atom_id: CA-C-416
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 2
updated_at: "2026-10-04 17:32:00 +0000"
subjects:
  governs: "Project Structure Maintenance/Step bindings"
  depends_on: [Workflow, Step, Action, Artifact/Carrier]
relations:
  concern_about: [CA-O-015, CA-P-1437]
---
# Summary

Bind structural Workflow node identities

## Concern

O015's six aliases do not supply the exact Step Atom identities required by the current Workflow graph model.

## Evidences

Independent P1437 directly read O015v6 and R1509v6/R1513v4. The source binds select/prepare/assess-candidate/authorize/apply/assess-result to Action IDs but declares no corresponding Step Atom nodes. Existing structural approval/currentness/preservation behavior is otherwise reusable.

## Blast radius

### Disposition

Done P1445 supplies six actual Step identities O139–144. Independent P1455 and P1456 passed the graph endpoints and all six Step bindings, preserving thirteen transitions and structural authorization/effect guards. This missing-identity defect is resolved. Repeated Workflow-owned bindings are a distinct C425 repair and do not reopen or erase these Step identities; source-stage and runtime acceptance remain gated.

P1445 authors exactly six reusable Step bindings and updates O015's endpoints while preserving its behavior. Separate independent review precedes source-stage acceptance. Keep one parameterized Workflow for all four structural requests; no duplicate definitions or code acceptance.
