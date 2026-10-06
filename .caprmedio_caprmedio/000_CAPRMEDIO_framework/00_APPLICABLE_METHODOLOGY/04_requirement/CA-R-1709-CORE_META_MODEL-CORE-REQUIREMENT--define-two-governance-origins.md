---
subjects:
  governs: "Governance Origin"
  depends_on:
    - "semantics"
version: 24
updated_at: "2026-10-03 02:24:19 +0400"
relations:
  child_of:
    - CA-M-001
atom_id: "CA-R-1709"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1709-CORE_META_MODEL-CORE-REQUIREMENT--define-two-governance-origins.md
  source_atom_id: CA-R-1709
  source_atom_revision: 24
  source_sha256: 77358bb1255d3e82877764480f0d6667e93ce7f4268572101ce129232a3879aa
  original_relations_sha256: 2f95e55e3d0a844c858c40eeab601ef29e88bfb9f5c8b9fd17a85ccd2af662a7
---
# Summary

Define two Governance origins

## Scope

Governance Origins of governed Artifacts.

## Claim

Governance Origin classifies **where** a governed Artifact's primary meaning is owned. Governance Origin has **`=2`** values:

- `internal` **means** the current project establishes **and** owns the meaning;
- `external` **means** an identified source outside the current project establishes **or** imposes the meaning, while the project records **and** binds itself **to** that source.

Governance Origin is independent of Artifact form, Content Role, structural scope, provenance, **and** graph relations. a typed graph relation does **not** create another Governance Origin; its Carrier encoding is governed by CA-D-268.

the current project boundary is ambient. Requirement authority defines these two values **and** the admitted Types; Delivery authority governs their Carrier encoding.

## Details
