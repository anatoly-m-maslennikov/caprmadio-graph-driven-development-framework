---
atom_id: CA-O-164
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release selected Framework Version"
  depends_on: [Workflow, Step, Action, Operator, Version, Methodology, Implementation, Skill, Test, Docker Image, Journal]
version: 2
updated_at: 2026-10-05 08:12:00 +0400
relations:
  relates_to: [CA-O-011, CA-O-025, CA-O-165, CA-O-166, CA-O-167, CA-O-168, CA-O-169, CA-R-1525, CA-R-1720]
---
# Summary

Release a selected Framework Version

## Operation

Release selected Framework Version **means** the Operator-invoked, non-recursive Workflow that releases one frozen executing Framework/Methodology Version N by building and proving separately pinned candidate Version N+1. The current N definitions, source frontier, runtime and rollback evidence remain fixed for this Run; candidate N+1 never becomes this Workflow's definition or input authority mid-Run.

## Scope

The selected boundary binds one current N, one distinct candidate N+1, their exact source revisions and digests, the complete staged source delivery, selected-snapshot compiler Tool boundary, canonical Projection and runtime/package delivery contracts, the complete hook-free project-local `ca` Skill directory target `.agents/skills/ca`, full test declaration, candidate image identity, selected prior-image identity, permissions, recovery policy and Journal capability. The requested staged release copy is `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`; it never replaces the declared `METHODOLOGY_SOURCES.authority_path` or becomes a second authoring authority. No path, compiler layout, client target, image, tag, permission, secret or rollback point is inferred.

## Steps

| Step | Action | Bound phase |
| --- | --- | --- |
| CA-O-170 | CA-O-165 | freeze |
| CA-O-171 | CA-O-165 | validate |
| CA-O-172 | CA-O-166 | deliver_sources |
| CA-O-173 | CA-O-166 | compile |
| CA-O-174 | CA-O-168 | run_tests |
| CA-O-175 | CA-O-167 | stage_candidate |
| CA-O-176 | CA-O-168 | build_image |
| CA-O-177 | CA-O-168 | prove_candidate |
| CA-O-178 | CA-O-169 | promote |
| CA-O-179 | CA-O-169 | retire |

## Transitions

| Step result | Next step or outcome |
| --- | --- |
| CA-O-170 complete frozen N and candidate N+1 boundary | CA-O-171 |
| CA-O-171 complete exact delivery, compiler, package, Skill, test, image and Journal bindings | CA-O-172 |
| CA-O-172 complete full source delivery | CA-O-173 |
| CA-O-173 complete compilation from the delivered candidate frontier | CA-O-174 |
| CA-O-174 every declared candidate test passed | CA-O-175 |
| CA-O-175 complete non-active candidate runtime/package and Skill staging | CA-O-176 |
| CA-O-176 candidate image built with exact identity | CA-O-177 |
| CA-O-177 complete actual candidate package and image proof | CA-O-178 |
| CA-O-178 complete N+1 runtime and project-local Skill promotion | CA-O-179 |
| CA-O-179 complete exact unused N-image retirement | complete |
| any missing, stale, unauthorized, failed, partial, recording-blocked, unsafe, or unmatched result | stop with its actual evidence; do not promote, retire, retry, or recurse implicitly |

## Details

CA-O-164 uses only its listed Step Atoms; it does not invoke another Workflow as a Step or invoke itself to prove a candidate. CA-O-011 remains the canonical Applicable Methodology compilation authority for declared Methodology Sources. The separately pinned candidate snapshot uses its reviewed Tool boundary to materialize only the sealed child under `_release_materialized/<candidateSnapshotManifest.sha256>/`; it neither produces nor replaces the canonical `_projection/APPLICABLE_METHODOLOGY`, which remains source-bound, and neither authority is silently rewritten. CA-O-025 remains release readiness and is not substituted for this boundary. Every Workflow, Step and Action Run retains the exact definition revisions, inputs, parent lineage, start/terminal outcome, results, effects and one canonical durable Work Journal record under CA-R-1525 and CA-R-1720. Preview, rejection and a missing recording receipt never manufacture a Run or release success. This source graph grants no implementation, installation, container, source mutation, image-removal, hook, credential, Git, publication or retry authority.
