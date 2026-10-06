---
atom_id: CA-O-169
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Promote candidate and retire exact prior image"
  depends_on: [Action, Version, Framework Package, Docker Image, Container, Permission, Journal]
version: 3
updated_at: "2026-10-06 02:13:39 +0000"
relations:
  relates_to: [CA-O-164, CA-O-178, CA-O-179, CA-D-563, CA-R-1525, CA-R-1720]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-169-PROJECT_CONFIGURATION-ACTION--promote-candidate-and-retire-exact-prior-image.md
  source_atom_id: CA-O-169
  source_atom_revision: 3
  source_sha256: 7d7727217e6dbdb2f3d2a0ada85dd485bc4649a11a08f206af664d4492e5418b
  original_relations_sha256: 39e68791e95827b849159063ea81321c917cb7f516c0a0881986d5adde329390
---
# Summary

Promote candidate and retire exact prior image

## Action

Promote candidate and retire exact prior image **means** the final Action that performs one bound `promote` or `retire` phase: it first promotes exactly the proven N+1 runtime and project-local hook-free `ca` Skill, then records the exact selected former N-image disposition. It removes that image only when the sealed condition permits retirement and it is proved unused.

## Scope

`promote` requires CA-O-184's exact passing Full Gate aggregate, explicit promotion permission, the exact frozen N and N+1 identities/digests, candidate manifest, source frontier, compiled output, staged package, immutable candidate image and parent lineage, plus CA-D-563's hook-free complete `ca` directory payload. This check is required even when this Action is directly invoked: an earlier receipt chain, workflow sequence, or caller assertion is not admission. A missing, stale, non-pass or differently bound aggregate stops before selection. It alone selects N+1 runtime and replaces the project-local `.agents/skills/ca` Skill after all gates. The final prior-image disposition requires the completed promotion result, sealed rollback-retention condition and exact old-image digest. Under `retain_prior`, it completes only with an actual Docker-subprocess, SHA-256-valid retention receipt bound to the exact sealed condition reference and settings digest, that observes that exact required image, has `retaining_container_refs == ()`, and has no removal fields. Retirement is permitted only when a sealed condition requires it and the identified old image has no running or stopped container, retained required rollback reference or other in-scope use. No name, tag prefix, age rule, global prune or inferred image is a removal target.

## Details

Promotion never starts another Release Version Workflow or changes the pinned definitions that executed this Run. With sealed `retain_prior`, the complete final outcome is `exact prior N-image disposition` only when the exact required prior image is observed by that bound retention receipt, `retaining_container_refs == ()`, and no removal occurs; it must not claim retirement. A used, unavailable, unverified, mismatched, permission-denied or otherwise unsafe prior image remains partial with actual evidence; do not delete another image. Actual retirement remains pending until its unchanged exact retired-effect handoff is recorded as a canonical effect. Image retirement is never attempted before promotion and candidate package/image proof pass. The Action preserves actual partial effects, N/N+1 identities, rollback evidence and a distinct canonical Action Run Journal record for each phase; no retry, force removal, global cleanup, source mutation or secret handling is implicit.
