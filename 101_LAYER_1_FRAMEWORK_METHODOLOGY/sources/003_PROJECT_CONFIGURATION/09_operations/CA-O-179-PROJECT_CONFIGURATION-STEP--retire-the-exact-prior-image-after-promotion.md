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
version: 2
updated_at: "2026-10-06 02:13:39 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-169]
---
# Summary

Retire the exact prior image after promotion

## Step

This Step invokes CA-O-169 once with phase `retire`, binding CA-O-178's completed promotion result, sealed rollback-retention condition and exact prior N-image digest to the final exact prior N-image disposition.

## Details

Only CA-O-169 may remove the exact old image after it verifies no in-scope use. Under sealed `retain_prior`, this Step completes as `exact prior N-image disposition` only with an actual Docker-subprocess, SHA-256-valid retention receipt bound to the exact sealed condition reference and settings digest, that observes the exact required prior image, has `retaining_container_refs == ()`, and has no removal fields; that retained outcome is not retirement. A used, unavailable, unverified, mismatched or non-exact image remains preserved and partial with actual evidence. Actual retirement remains pending until its separate exact removal effect has a canonical Journal record; this Step does not force cleanup, prune globally, retry or claim release completion.
