---
subjects:
  governs: "Atom/Identifier"
  depends_on:
    - "Atom/Content Role"
    - "Project"
    - "Atom/Content Role: Plan/Type: Plan/Identifier"
version: 10
updated_at: "2026-10-02 19:27:36 +0400"
relations: {}
atom_id: "CA-D-378"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-378-CORE_META_MODEL--serialize-assigned-atom-identities.md
  source_atom_id: CA-D-378
  source_atom_revision: 10
  source_sha256: 9435f3abb5a56f46c37c43c3e758afa1e288a0af259f39a34237495d8fcf255f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Assigned Atom Identities

## Scope

assigned Atom IDs.

## Claim

**every** assigned Atom ID **must** begin with the registered uppercase Project identity prefix. the Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. the Atom Content Role Identity Letter **must** be **in** (Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Implementation: I, Operations: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom, including one labeled Epic, **and** **must not** identify a separate non-Atom collection.

## Details
