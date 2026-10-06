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
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  relates_to: [CA-O-164, CA-O-178, CA-O-179, CA-D-563, CA-R-1525, CA-R-1720]
---
# Summary

Promote candidate and retire exact prior image

## Action

Promote candidate and retire exact prior image **means** the final Action that performs one bound `promote` or `retire` phase: it first promotes exactly the proven N+1 runtime and project-local hook-free `ca` Skill, then only in the later phase retires exactly the selected former N image when it is proved unused.

## Scope

`promote` requires complete current evidence from CA-O-170 through CA-O-177, explicit promotion permission, the exact N and N+1 identities/digests, and the staged complete package plus CA-D-563's hook-free complete `ca` directory payload. It alone selects N+1 runtime and replaces the project-local `.agents/skills/ca` Skill after all gates. `retire` requires the completed promotion result, an approved rollback-retention condition, and an exact old-image digest. Before removal, verify that the identified old image has no running or stopped container, retained required rollback reference or other in-scope use. No name, tag prefix, age rule, global prune or inferred image is a removal target.

## Details

Promotion never starts another Release Version Workflow or changes the pinned definitions that executed this Run. If promotion succeeds but the exact old image is still used, unavailable, mismatched, permission-denied or cannot be safely checked, retain it and return the truthful retirement-blocked or partial outcome; do not claim complete release proof and do not delete another image. Image retirement is never attempted before promotion and candidate package/image proof pass. The Action preserves actual partial effects, N/N+1 identities, rollback evidence and a distinct canonical Action Run Journal record for each phase; no retry, force removal, global cleanup, source mutation or secret handling is implicit.
