---
subjects:
  governs: "Terminology Projection Derivation"
  depends_on:
    - "Projection/Type: Catalog"
    - "Generator"
    - "Definition Atom"
    - "Governed Term"
    - "Project"
    - "Atom/Claim"
    - "Subject"
    - "Subject Path"
    - "Entity"
    - "Term"
    - "Action"
    - "Workflow"
version: 20
updated_at: "2026-10-01 21:33:03 +0400"
relations: {}
atom_id: "CA-M-114"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-114-CORE_META_MODEL--derive-terminology-projection-from-definition-atoms.md
  source_atom_id: CA-M-114
  source_atom_revision: 20
  source_sha256: 16513dca0a7370d9a98999f537da293fd8d14ae4d9a47fee7f70fb1f8a9b1dd6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Terminology Projection from Definition Atoms

## Scope

derivation of a terminology Projection from active Definition Atoms.

## Claim

**to** build a terminology list using the Catalog Type, the Generator **must** derive **every** Governed Term's name **and** Project-specific meaning from its active Definition Atom. read the Term named by the defining Claim **and** verify that the Definition Atom's GOVERNS Subject Relation identifies its defined target under CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term. extract Term references from **every** named component of a Subject Path, **not** **only** its terminal component; obtain **every** referenced Term's meaning from that Term's own defining Claim, **not** by treating **all** path components as definitions supplied by the referencing Atom. include an entry **only** **when** the defining Claim establishes a Project-specific meaning; consistent use, capitalization, **or** occurrence **in** a Subject Path alone does **not** supply defining authority. an unresolved named component is a Term-reference gap **to** report, **not** permission **to** invent a definition **or** silently treat that component as ordinary vocabulary. exclude words **and** phrases used **only** with their ordinary English meanings. retain the source reference **without** classifying the direct Subject reference **or** a complete composite Subject Path as a Term **or** creating independent vocabulary authority.

## Details
