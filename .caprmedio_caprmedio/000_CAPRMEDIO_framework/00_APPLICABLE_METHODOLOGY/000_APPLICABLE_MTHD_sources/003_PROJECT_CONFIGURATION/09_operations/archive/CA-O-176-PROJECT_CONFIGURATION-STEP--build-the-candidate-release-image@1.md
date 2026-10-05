---
atom_id: CA-O-176
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: build candidate image"
  depends_on: [Workflow, Step, Action, Docker Image, Framework Package, Test, Journal]
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Build the candidate release image

## Step

This Step invokes CA-O-168 once with phase `build_image`, binding the complete passed candidate test result, staged package manifest, sources, declared build context and immutable candidate image identity.

## Details

It creates no authority from a tag, cached image or successful build alone. A build mismatch, host mount, stale package/source, unsafe context, failed result or missing Journal receipt stops without proof, promotion or old-image removal.
