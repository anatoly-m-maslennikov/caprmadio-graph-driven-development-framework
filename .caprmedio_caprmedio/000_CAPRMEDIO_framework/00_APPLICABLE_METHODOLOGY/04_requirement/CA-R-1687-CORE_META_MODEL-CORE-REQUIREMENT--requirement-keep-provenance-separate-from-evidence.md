---
subjects:
  governs: "evaluation"
  depends_on: []
version: 19
updated_at: "2026-10-03 02:10:09 +0400"
relations: {}
atom_id: "CA-R-1687"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1687-CORE_META_MODEL-CORE-REQUIREMENT--requirement-keep-provenance-separate-from-evidence.md
---
# Summary

Requirement — Keep provenance separate from evidence

## Scope

provenance and Evidence for governed claims and Implementations.

## Claim

provenance establishes the origin, carrier identity, revision, sequence, **and** transformation history of a governed claim **or** Implementation. it does **not** by itself establish that the claim is correct, accepted, current, applicable, **or** sufficiently assured.

complete governed provenance remains owned under CA-R-1720. a storage-history record, Author identity, session identifier, signature, hash, **or** intact Carrier proves **only** the bounded historical fact it records. **none** of those facts becomes evidence for the carrier's semantic claim **without** a separate, explicit claim-bound Evidence relation.

Evidence used for reliance **must** identify the claim it supports, the relevant carrier **or** Journal Record, the producing **or** interpreting work **or** Method **when** material, **and** the applicable scope **and** time boundary. Verification remains a separate Evaluation conclusion. a claim, its carrier, **and** the work that created it **must not** silently evidence themselves.

## Details
