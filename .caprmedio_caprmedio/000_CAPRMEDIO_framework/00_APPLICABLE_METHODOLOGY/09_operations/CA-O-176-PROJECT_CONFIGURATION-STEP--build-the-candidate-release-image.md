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
version: 3
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-176-PROJECT_CONFIGURATION-STEP--build-the-candidate-release-image.md
  source_atom_id: CA-O-176
  source_atom_revision: 3
  source_sha256: d7a4d6dd7bbed0773b25dac721695e6f95c0b14655f53982389e37cc6fb8ae88
  original_relations_sha256: ecd7aad8b0d56b8c8ef2cb7f0a757140dd7cdf64ff933ba55f15e7ef8b93d061
---
# Summary

Build the candidate release image

## Step

This Step invokes CA-O-168 once with phase `candidate_image_build`, binding CA-O-175's staged package, exact source/context rows and immutable candidate image identity. The frozen Docker worker has no Docker socket and cannot substitute for host Candidate E2E.

## Details

It creates no authority from a tag, cached image or successful build alone. A build mismatch, host mount, stale package/source, unsafe context, failed result or missing Journal receipt stops without proof, promotion or old-image removal.
