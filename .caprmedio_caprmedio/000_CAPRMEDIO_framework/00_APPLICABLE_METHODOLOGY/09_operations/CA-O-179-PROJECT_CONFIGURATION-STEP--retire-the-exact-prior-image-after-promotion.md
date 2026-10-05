---
atom_id: CA-O-179
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: retire exact prior image"
  depends_on: [Workflow, Step, Action, Docker Image, Container, Permission, Journal]
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-169]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-179-PROJECT_CONFIGURATION-STEP--retire-the-exact-prior-image-after-promotion.md
  source_atom_id: CA-O-179
  source_atom_revision: 1
  source_sha256: 7472a8e806ed0859a611c733bc130fcddc11a2dab9d033492732a9253cbb8107
  original_relations_sha256: 4a7aab972e708c440d2f546dc2c51322bfc83e7c8cb16d917b379901e2b55af0
---
# Summary

Retire the exact prior image after promotion

## Step

This Step invokes CA-O-169 once with phase `retire`, binding CA-O-178's completed promotion result, approved rollback-retention condition and exact prior N-image digest.

## Details

Only CA-O-169 may remove the exact old image after it verifies no in-scope use. A used, unverified, mismatched or non-exact image remains preserved and returns retirement-blocked or partial with actual evidence; this Step does not force cleanup, prune globally, retry or claim release completion.
