---
subjects:
  governs: "Projection/Type: Implementation Overview"
  depends_on:
    - "Projection"
    - "Atom"
    - "Artifact/Revision"
    - "Implementation Binding"
    - "Journal"
    - "Implementation"
    - "Verification"
version: 27
updated_at: "2026-10-03 01:23:33 +0400"
relations:
  relates_to:
    - CA-R-1634
    - CA-R-1695
atom_id: "CA-R-1638"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1638-CORE_META_MODEL-CORE-REQUIREMENT--register-the-implementation-overview-projection.md
  source_atom_id: CA-R-1638
  source_atom_revision: 27
  source_sha256: b6e8d268fc9546c9ae843a22b79f0f39f8c78362545fc86728a8dd314a35b099
  original_relations_sha256: ca8e30248bc494e61dbfca5dfc464cb2cac735cd10ec843d8b815405c124319c
---
# Summary

Register the Implementation Overview Projection

## Scope

the Implementation Overview Projection.

## Claim

Implementation Overview **means** the internal Type value under Projection that presents current realization, coverage, source-to-target bindings, relevant provenance, **and** unresolved gaps derived from its declared source frontier.

the Projection declares the exact normative Atom, native-target, provenance, **and** **any** registered implementation-lineage frontier it represents. its Implementation Bindings derive from the shared Project Journal under CA-R-1695-CORE_META_MODEL-REQUIREMENT--preserve-implementation-traceability-in-the-shared-project-journal. regeneration replaces its rendered content **without** converting it into an Atom **or** granting it authority over the Journal, native project, normative specification, Operations evidence, **or** Verification. historical implementation event records remain **in** the Journal; this Projection presents the current view **without** replacing those records.

its storage **and** retention policy is configured separately. a generated runtime copy **may** be disposable; a committed current view **may** be reviewable history. the two storage choices do **not** change the Projection's semantic role.

## Details

the predecessor incorrectly bundled Change Plan **and** Implementation Record under one Implementation-role Projection rule. the split preserves the record while routing Change Plan **to** the new Plan Atom family.

the historical name Implementation Record **in** this rationale referred **to** the current-state Projection now named Implementation Overview; the name change distinguishes that view from the implementation event records retained **in** the Journal.
