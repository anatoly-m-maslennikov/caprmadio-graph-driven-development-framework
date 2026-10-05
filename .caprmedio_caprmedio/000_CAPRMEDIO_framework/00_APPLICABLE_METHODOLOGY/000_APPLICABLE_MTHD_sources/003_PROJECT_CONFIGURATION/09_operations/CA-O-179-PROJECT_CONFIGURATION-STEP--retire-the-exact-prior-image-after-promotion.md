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
---
# Summary

Retire the exact prior image after promotion

## Step

This Step invokes CA-O-169 once with phase `retire`, binding CA-O-178's completed promotion result, approved rollback-retention condition and exact prior N-image digest.

## Details

Only CA-O-169 may remove the exact old image after it verifies no in-scope use. A used, unverified, mismatched or non-exact image remains preserved and returns retirement-blocked or partial with actual evidence; this Step does not force cleanup, prune globally, retry or claim release completion.
