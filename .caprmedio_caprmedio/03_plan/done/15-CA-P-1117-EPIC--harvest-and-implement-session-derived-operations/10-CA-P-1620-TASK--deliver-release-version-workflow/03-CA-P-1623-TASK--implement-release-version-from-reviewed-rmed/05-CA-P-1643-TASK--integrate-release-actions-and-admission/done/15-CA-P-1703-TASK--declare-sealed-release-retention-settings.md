---
atom_id: CA-P-1703
content_role: Plan
type: Plan
label: Task
work_sequence_number: 15
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Declare sealed Release retention settings"
  depends_on: [Framework Instance Settings, Image, Manifest, Tool, Evaluation]
version: 1
updated_at: "2026-10-05 07:25:06 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1697, CA-P-1644]
---
# Summary

Declare sealed Release retention settings

## Objective

Within <=10 minutes, author the one narrow Delivery contract for the already-sealed Framework Instance Settings rollback-retention condition.

## Details

Own only new TOOLS/07_delivery/CA-D-573-TOOLS-DELIVERY--serialize-approved-release-rollback-retention.md. Read current R1879/R1880/O169 and C466; no code, settings values, source admission or existing source edits. Declare a closed [release_version.rollback_retention] table in the existing authoritative Framework Instance Settings file already sealed by D566's framework_settings_digest. Use explicit condition retain_prior or until_verified_promotion and a required_image_digests list of exact immutable sha256 IDs. Missing/unknown/malformed condition means unknown retention and no removal; explicit retain_prior retains N. until_verified_promotion requires independently verified same-candidate suite/image/promotion and no required old-image reference before possible exact non-forced removal. Historical prior-selector evidence alone is not required retention. No caller flags, mutable tags, new registry, implicit default deletion, actual settings mutation or authority bypass.

This authoring result requires independent source review before implementation or addition to the current D572 source-frontier record; no current admission is silently widened.

## Definition of Done

Save the self-sufficient one-Claim D carrier, exact hash and source/ambiguity disposition. Review, source-admission update and actual removal implementation remain required dependent work.

### Current authored result

D573@1 SHA08baf33ec1200468c132237561bd92cf6a9a5322aa76636cca87261fe2c27bcd is saved at the assigned Tool Delivery carrier. It declares only the explicit closed retention table, exact condition and duplicate-free immutable digest list, reopens the same sealed settings digest and refuses unknown or required retention. No settings value, runtime/image effect or current admission was changed. P1704 reviews this bounded source before the D572 frontier update and removal implementation.
