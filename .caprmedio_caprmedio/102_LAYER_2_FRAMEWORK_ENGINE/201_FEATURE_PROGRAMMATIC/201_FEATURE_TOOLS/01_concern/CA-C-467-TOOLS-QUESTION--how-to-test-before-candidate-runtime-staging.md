---
atom_id: CA-C-467
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 07:19:04 +0000"
subjects:
  governs: "Release suite before runtime staging"
  depends_on: [Tool, Workflow, Step, Runtime, Manifest, Evaluation]
relations:
  concern_about: [CA-P-1701, CA-P-1702, CA-O-174, CA-O-175, CA-E-572]
---
# Summary

How to test before candidate runtime staging

## Concern

O164/O174 order the full suite before O175 candidate runtime/package staging, while execute_bound_release_suite currently requires the physical runtime-package directory. That implementation prerequisite makes the selected fresh-release path stop before the suite.

## Evidences

The suite helper already revalidates the exact candidate source frontier, compilation and complete package rows. E572@2 requires complete candidate package and full-suite proof before exposure and permits, but does not require, package preparation before the suite. O174 forbids runtime/package or Skill staging within this earlier phase.

## Blast radius

Only pre-staging suite admission and the fresh Release phase composition. Image admission, actual complete package verification, promotion and all permission gates remain unchanged.

## Decision

Options are hidden early staging, external manual pre-staging, or testing the exact bound source/compiled candidate before installation. Choose the third at90% confidence: validate all complete sealed candidate rows before execution; require exact package verification when a retained candidate package already exists, but do not create or require that package before testing. O175 subsequently stages/verifies those exact bytes, and image/promotion gates still require the complete package and successful suite evidence. P1702 owns the narrow correction and no-package/stale/tamper tests. Continue autonomously without a new Operator decision.
