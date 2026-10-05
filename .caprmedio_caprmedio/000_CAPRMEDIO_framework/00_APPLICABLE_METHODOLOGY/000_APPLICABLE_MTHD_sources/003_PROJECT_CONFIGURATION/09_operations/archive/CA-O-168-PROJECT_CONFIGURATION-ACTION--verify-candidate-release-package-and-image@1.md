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
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  relates_to: [CA-O-164, CA-O-176, CA-O-177, CA-O-178, CA-R-1525, CA-R-1720]
---
# Summary

Verify candidate release package and image

## Action

Verify candidate release package and image **means** the Action that performs one bound `run_tests`, `build_image`, or `prove_candidate` phase for frozen N+1 without promoting it.

## Scope

`run_tests` runs the complete declared candidate release suite from the compiled candidate boundary, not a selected subset, before candidate runtime/Skill staging or active selection. `build_image` builds one fresh candidate image from the exact staged candidate package, sources and declared build context and records its immutable digest. `prove_candidate` verifies the staged complete package, matching compiled Methodology, staged hook-free Skill, image digest and required actual image behavior against the bound candidate evidence.

## Details

An old image, host mount, mutable tag, partial suite, cached result, source-only assertion, package manifest alone, build success alone or recursive Release Version invocation is not proof. Candidate testing, image construction and proof cannot alter N, select N+1 runtime/Skill, retire an image, switch this Run's definitions, use a live paid CLI or make an unbound external call. Failed, unsafe, unavailable or recording-blocked proof returns its actual outcome and preserves candidate evidence; it never reports N+1 promoted. Each actual Action Run, including a failed test or proof, is journaled once with its exact input and image/package digests.
