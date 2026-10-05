---
atom_id: CA-O-173
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: compile candidate Methodology"
  depends_on: [Workflow, Step, Action, Applicable Methodology, Compiler, Delivery, Journal]
version: 3
updated_at: 2026-10-05 15:29:23 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-166]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-173-PROJECT_CONFIGURATION-STEP--compile-the-candidate-applicable-methodology.md
  source_atom_id: CA-O-173
  source_atom_revision: 3
  source_sha256: f5209614e245abcd3f1b38ab60c2b23f3f92f3b6f7682af8b9302f028cf255b8
  original_relations_sha256: 6129e7d188819e6b84f628ad315d8972e2af3aa6b781669e5ac0b4dfe2938295
---
# Summary

Compile the candidate Applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile`, binding only the complete delivered source manifest from CA-O-172 and the reviewed selected-snapshot compiler Tool boundary. Its candidate output is only the sealed child materialization under `_release_materialized/<candidateSnapshotManifest.sha256>/`; the canonical Applicable Methodology at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/` remains source-bound and is not this Step's output. A later derived runtime Methodology delivery is not compiler output authority.

## Details

This is not another compiler graph: CA-O-166 uses the reviewed Tool boundary required for a selected pinned snapshot while preserving the existing canonical compiler authority. A changed frontier, incomplete delivery, unbound Tool/layout, child-materialization mismatch, or any canonical projection mutation stops without runtime installation, image work or promotion.
