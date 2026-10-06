---
atom_id: CA-O-168
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Verify candidate release package and image"
  depends_on: [Action, Test, Framework Package, Methodology, Docker Image, Artifact/Revision, Journal]
version: 3
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  relates_to: [CA-O-164, CA-O-176, CA-O-185, CA-O-186, CA-O-178, CA-R-1525, CA-R-1720]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-168-PROJECT_CONFIGURATION-ACTION--verify-candidate-release-package-and-image.md
  source_atom_id: CA-O-168
  source_atom_revision: 3
  source_sha256: 427838ea3f7dd5cbe8905f315ffe0b44dc6a6ef8e43ba42f2174cfe431d58daf
  original_relations_sha256: 58c104028a93c5fcceb709afb9b564802117281d6a0d89fc6e17003c2190fb06
---
# Summary

Verify candidate release package and image

## Action

Verify candidate release package and image **means** the Action that performs one bound `closed_unit_gate`, `candidate_image_build`, or `candidate_image_canary` phase for frozen N+1 without promoting it.

## Scope

`closed_unit_gate` runs only the closed declared unit gate from the compiled candidate boundary; it is not the host Candidate E2E or Full Gate. `candidate_image_build` builds one fresh candidate image from the exact staged candidate package, sources and declared build context and records its immutable digest. `candidate_image_canary` verifies that exact immutable image, complete staged package, matching compiled Methodology and hook-free Skill in the frozen container boundary. The frozen Docker worker receives no Docker socket: host-capable Candidate E2E is a separate explicit Action.

## Details

An old image, host mount, mutable tag, partial suite, cached result, source-only assertion, package manifest alone, build success alone or recursive Release Version invocation is not proof. Candidate testing, image construction and proof cannot alter N, select N+1 runtime/Skill, retire an image, switch this Run's definitions, use a live paid CLI or make an unbound external call. Failed, unsafe, unavailable or recording-blocked proof returns its actual outcome and preserves candidate evidence; it never reports N+1 promoted. Each actual Action Run, including a failed test or proof, is journaled once with its exact input and image/package digests.
