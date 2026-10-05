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
version: 2
updated_at: 2026-10-06 00:00:00 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Build the candidate release image

## Step

This Step invokes CA-O-168 once with phase `candidate_image_build`, binding CA-O-175's staged package, exact source/context rows and immutable candidate image identity. The frozen Docker worker has no Docker socket and cannot substitute for host Candidate E2E.

## Details

It creates no authority from a tag, cached image or successful build alone. A build mismatch, host mount, stale package/source, unsafe context, failed result or missing Journal receipt stops without proof, promotion or old-image removal.
