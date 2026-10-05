---
atom_id: CA-O-186
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: run candidate image canary"
  depends_on: [Workflow, Step, Action, Docker Image, Framework Package, Methodology, Skill, Journal]
version: 1
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-186-PROJECT_CONFIGURATION-STEP--run-the-candidate-image-canary.md
  source_atom_id: CA-O-186
  source_atom_revision: 1
  source_sha256: d77df3c5e6571e46355fba068c30977e831da9d57be30314174c777fb48a4de4
  original_relations_sha256: ecd7aad8b0d56b8c8ef2cb7f0a757140dd7cdf64ff933ba55f15e7ef8b93d061
---
# Summary

Run the candidate image canary

## Step

This Step invokes CA-O-168 once with phase `candidate_image_canary`, binding CA-O-176's exact immutable candidate image digest and staged complete package, Methodology and hook-free Skill.

## Details

This is the frozen-container canary only; it is not host Candidate E2E or Full Gate aggregation. Its result must prove the bound candidate image and staged complete package, not only source files, a manifest or build success. It cannot select N+1, remove images, use an unbound external/paid CLI or retry. Missing or unsafe proof stops before CA-O-182.
