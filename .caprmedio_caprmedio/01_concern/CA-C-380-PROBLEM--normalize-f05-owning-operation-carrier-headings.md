---
atom_id: CA-C-380
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: unresolved
subjects:
  governs: "F05 owning Operations Carrier Property headings"
  depends_on: [Operations, "Markdown Atom Carrier/Main Content"]
version: 1
updated_at: "2026-10-04 13:31:22 +0000"
relations:
  concern_about: [CA-O-012, CA-O-013, CA-O-014, CA-O-015, CA-O-058, CA-O-067, CA-O-077, CA-O-078]
  relates_to: [CA-P-1350, CA-A-1068, CA-D-479]
---
# Summary

Normalize F05 owning Operation Carrier headings without inventing behavior

## Concern

Eight current F05 owning Operation Carriers do not carry exactly the required D479 v6 Operations body Properties: one literal # Summary followed by ## Operation and ## Details. Legacy titles or ## Claim/Steps/Inputs/Outcomes cannot be inferred to be those registered sections. This is a nonblocking Delivery-format Problem, not a missing semantic Operation or permission to edit sources in P1350.

## Evidences

Fully read the following current authoritative sources under `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/`:

- CA-O-012 v5: `09_operations/CA-O-012-CORE_META_MODEL-ACTION--prepare-structural-change.md`.
- CA-O-013 v5: `09_operations/CA-O-013-CORE_META_MODEL-ACTION--authorize-structural-change.md`.
- CA-O-014 v5: `09_operations/CA-O-014-CORE_META_MODEL-ACTION--apply-structural-change.md`.
- CA-O-015 v6: `09_operations/CA-O-015-CORE_META_MODEL-WORKFLOW--maintain-project-structure.md`.
- CA-O-058 v6: `09_operations/CA-O-058-CORE_META_MODEL-ACTION--assess-revision-impact-through-lineage.md`.
- CA-O-067 v6: `09_operations/CA-O-067-CORE_META_MODEL-ACTION--assess-atom-update-identity.md`.
- CA-O-077 v4: `09_ops/CA-O-077-CORE_META_MODEL-ACTION--reconcile-atom-properties-and-addresses-together.md`.
- CA-O-078 v3: `09_operations/CA-O-078-CORE_META_MODEL-ACTION--reconcile-navigation-numbers-during-project-structure-migration.md`.

O012/O013/O014/O015/O058/O067 have legacy level-one titles; O015 additionally uses Steps/Transitions and O067 Inputs/Outcomes. O077 and O078 use ## Claim rather than ## Operation and have no registered ## Details. None has the complete required Operations layout. Their complete readable Claims were compared in A1068; no missing heading is declared to exist and no formal source-conformance pass is claimed. O052's similar existing issue remains C353 and is excluded from this Concern to avoid duplicate ownership.

Current D479 v6 requires exactly one registered heading in role order and prohibits inferring missing headings from prose/position. The defect needs a separately authorized source-authoring correction followed by independent review and governed persistence, preserving behavior/identity and applying O067's revision classification rather than guessing version changes.

## Blast radius

Only these eight named CORE_META_MODEL Operation Carriers and consumers requiring exact registered Property boundaries. Reconciliation can complete from readable content with the defect visible; authoring/review cannot silently declare repaired sources. No ontology redesign, new Operation, Settings/Structure value, code/runtime/source/Git/Journal change is authorized by this Concern. Parent binds actual repair/review follow-up; C380 remains unresolved.
