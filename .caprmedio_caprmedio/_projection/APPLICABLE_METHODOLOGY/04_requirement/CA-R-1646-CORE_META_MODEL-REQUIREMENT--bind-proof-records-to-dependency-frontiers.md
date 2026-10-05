---
subjects:
  governs: "Evidence"
  depends_on:
    - "Artifact/Revision"
    - "Atom/Content Role: Implementation"
    - "Projection"
    - "Carrier"
version: 18
updated_at: "2026-10-03 01:31:08 +0400"
relations:
  resolution_of:
    - "CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented"
  relates_to:
    - "CA-D-329"
atom_id: "CA-R-1646"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1646-CORE_META_MODEL-REQUIREMENT--bind-proof-records-to-dependency-frontiers.md
  source_atom_id: CA-R-1646
  source_atom_revision: 18
  source_sha256: 3e10153314d2dc0953b1b2d53f34f78ff8870ba006bf70091fbe8ed9f34a148a
  original_relations_sha256: 7d5e5955ca0ee72f9019f7d2d5dbbcfbeac9d5f91bff5e109d83e55ba651637f
---
# Bind proof records to dependency frontiers

## Scope

governed proof records, their applicable inputs, and all selected Workflows, release policies, and version-control mechanisms.

## Claim

**every** governed proof record **must** bind its observation **to** the exact applicable inputs under which it was produced.

- the binding includes the relevant Artifact **and** Implementation Revisions, configuration, evaluators, environments, **and** material inputs; CA-D-329 governs its representation.
- reliance on that observation for a current candidate requires a matching input binding **and** satisfaction of its additional governing invalidation conditions.
- a changed material input makes the affected proof stale for that candidate **until** the required checks run against the changed inputs. a missing **or** unresolved binding is unknown, **not** current.
- an unrelated change does **not** invalidate proof **unless** it changes the evaluated dependencies **or** satisfies an additional governing invalidation condition.
- retain the historical record unchanged. **not** (a recent timestamp **or** a refreshed Projection) alone proves currentness.

## Details
