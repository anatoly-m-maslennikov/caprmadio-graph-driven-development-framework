---
atom_id: CA-O-100
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Method Lesson Drafting"
  depends_on:
    - "Action"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Operator"
    - "AI Agent"
version: 3
updated_at: "2026-10-04 15:15:47 +0000"
relations:
  relates_to:
    - CA-O-090
    - CA-R-1559
    - CA-R-1591
    - CA-M-002
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-100-CORE_META_MODEL-ACTION--draft-methods-from-verified-implementation-issues.md
  source_atom_id: CA-O-100
  source_atom_revision: 3
  source_sha256: c2a7222371548d683f3dec7776694baa6a24b2571190336048d234a5dd72b88b
  original_relations_sha256: b2489f323a77e636b921e72f37bc2992e015b00afb6db114252392e02cf825d6
---
# Summary

Draft Methods from verified implementation issues

## Operation

Method Lesson Drafting **means** the Agentic Action that derives a bounded Standard Method Draft from a verified implementation issue **in** a separately admitted learning Run.

- inputs: an explicit learning request, bounded P/Plan work, retained admitted Evaluation-portfolio results, relevant focused-regression results, reproducible failure, diagnosis, actual fix, passing regression evidence, current governing Method/RED authority, existing related Drafts, **and** confidence/permission gates.
- require sufficient evidence that the proposed correction explains the defect **and** that relevant checks pass on the fixed candidate. an initial test failing because behavior is not implemented yet is **not** a Method lesson; uncertain **or** stale evidence returns `blocked`.
- check existing Methods **and** pending Drafts before writing. return `already_covered` with their references **when** no distinct Method is needed; repeated failures **must not** create duplicate lessons.
- **when** a missing Method is justified **and** authoring is admitted, create **or** refine the applicable Standard Draft with **=1** Claim, its precise governed Entity, correct Scope Unit, actual Author, structured content, **and** linked evidence. preserve Summary identity rules **and** keep Drafts without assigned Atom IDs.
- return `drafted` with the Draft references **and** evidence for separate acceptance by CA-O-090, **or** `blocked` with the unmet gate. this Action does **not** promote Methods **or** generalize them into broader policies.

## Details
