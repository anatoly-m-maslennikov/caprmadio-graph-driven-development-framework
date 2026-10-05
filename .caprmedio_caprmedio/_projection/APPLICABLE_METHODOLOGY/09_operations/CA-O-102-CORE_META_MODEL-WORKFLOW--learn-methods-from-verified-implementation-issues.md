---
atom_id: CA-O-102
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Method Learning Workflow"
  depends_on:
    - "Workflow"
    - "Step"
    - "Workflow/Relation Kind: On Result"
    - "Workflow Run"
    - "Atom/Content Role: Method"
    - "Implementation Workflow"
version: 2
updated_at: "2026-10-04 15:15:46 +0000"
relations:
  relates_to:
    - CA-O-101
    - CA-O-098
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-102-CORE_META_MODEL-WORKFLOW--learn-methods-from-verified-implementation-issues.md
  source_atom_id: CA-O-102
  source_atom_revision: 2
  source_sha256: 9d4a9d6bfd1f57f9f4eda4b10bba75ccab1af560dde083cd44dbca19c5491c48
  original_relations_sha256: 3cf6dbadc9fea1fea16aad5572c903005fe75aa61c702ca060ae00fddc6d2117
---
# Summary

Learn Methods from verified implementation issues

## Operation

Method Learning Workflow **means** the separately invoked graph that derives **and**, **when** admitted, accepts Method lessons from verified implementation evidence.

- entry: CA-O-101.
- nodes: CA-O-101, CA-O-098.
- transitions use Workflow-scoped `ON_RESULT`; terminal results are **not** Steps.

| From Step | Result condition | Next Step **or** terminal result |
|---|---|---|
| CA-O-101 | drafted | CA-O-098 |
| CA-O-101 | already_covered | completed |
| CA-O-101 | blocked | blocked |
| CA-O-098 | accepted | completed |
| CA-O-098 | already_covered | completed |
| CA-O-098 | blocked | blocked |

the input is an explicitly admitted learning request with retained implementation issue, test, diagnosis, **and** fix evidence, **not** an automatic continuation required for implementation completion. a failed invocation, unknown result, stale evidence, **or** unmet confidence/permission gate terminates `blocked` with actual partial results. a blocked learning Run does **not** retroactively fail a verified implementation Run; a separately discovered implementation defect still requires its own disposition.

## Details
