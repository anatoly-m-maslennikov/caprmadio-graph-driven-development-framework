---
atom_id: CA-O-165
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Freeze and validate release boundary"
  depends_on: [Action, Operator, Version, Artifact/Revision, Methodology, Delivery, Skill, Test, Docker Image, Journal]
version: 2
updated_at: 2026-10-05 09:04:17 +0400
relations:
  relates_to: [CA-O-164, CA-O-170, CA-O-171, CA-O-025, CA-D-563, CA-R-1525, CA-R-1720]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-165-PROJECT_CONFIGURATION-ACTION--freeze-and-validate-the-release-boundary.md
  source_atom_id: CA-O-165
  source_atom_revision: 2
  source_sha256: 64afd80c7f93eca5a4047647f52b1471b016426fefbcf14de0eba5dfd8fec909
  original_relations_sha256: 1a8250c8e4dbbf0a36f39cc537829d2ff1635a3151cba1b01324d8c2fc6bafa7
---
# Summary

Freeze and validate the release boundary

## Action

Freeze and validate release boundary **means** the Action that first freezes the exact executing Version N and separately pinned candidate N+1, then validates all selected release bindings before a release effect is admitted.

## Scope

The `freeze` phase records N's current Framework/Methodology revisions, source frontier and rollback identity and records N+1's distinct source revisions, digests and candidate identity. The `validate` phase checks the selected staged source-delivery destination, the explicit pinned-snapshot compiler Tool boundary, the private child-materialization contract and preservation of the source-bound canonical Projection, `.caprmedio_runtime` package manifest, CA-D-563's complete hook-free project-local `ca` Skill directory target `.agents/skills/ca`, complete test declaration, candidate image identity, exact prior-image identity, permissions and canonical Journal capability.

## Details

N must remain the executing runtime and rollback point until candidate promotion passes all required gates. N+1 must be a distinct pinned candidate; neither a mutable label nor an unbound current source frontier is sufficient. A changed definition, source, digest, destination, permission, selected-snapshot compiler boundary, child-materialization or canonical-Projection-preservation contract, package contract, test declaration, image identity, Journal capability or missing reviewed path reconciliation returns blocked before delivery. This Action does not copy, compile, install, test, build, promote, remove an image, select another candidate, create a release tag, invoke a Workflow, or authorize its own retry. Its actual Action Run is journaled once with the bound boundary and result.
