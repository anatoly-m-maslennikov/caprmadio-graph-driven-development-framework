---
version: 12
updated_at: "2026-10-02 19:57:02 +0400"
relations: {"child_of":["CA-E-001"],"evaluation_for":["CA-M-298","CA-O-054","CA-R-1375"]}
subjects:
  governs: "Methodology Source/expansion mapping"
  depends_on:
    - "Methodology Source"
    - "Core Meta-Model"
    - "Extension"
    - "Project Configuration"
    - "Operator"
    - "Entity"
atom_id: "CA-E-249"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-249-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--evaluate-methodology-expansion-mappings.md
  source_atom_id: CA-E-249
  source_atom_revision: 12
  source_sha256: fcb2658717a91add097f34751c89d54f03a047442031ee7cf79e89c9f817d965
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Evaluate methodology expansion mappings

## Scope

methodology expansion mappings.

## Claim

a methodology expansion mapping Evaluation **must** return `fail` **if** a source element, exact canonical target, mapping rule, intended Scope, **or** applicable Core Meta-Model distinction at **any** Local Tier is missing, canonical ownership is ambiguous, preservation is unproven, **or** the mapping redefines, replaces, shadows, weakens, deletes, contradicts, **or** reinterprets applicable Core Meta-Model authority at **any** Local Tier; it **must** return `pass` **only** **when** the declared mapping preserves that authority **and** stays within its permitted expansion boundary. an Operator-approved loss **must not** count as conformance; report the failed boundary **and** leave the affected application stopped.

## Details
