---
subjects:
  governs: "Artifact Classification Resolution"
  depends_on:
    - "Artifact"
    - "Atom"
    - "Atom/Content Role"
    - "Type"
    - "Applicable Methodology"
    - "Project Configuration"
    - "Project Structure"
    - "Scope Unit Graph"
    - "Journal"
    - "Projection"
    - "Authority Mode"
version: 25
updated_at: "2026-10-03 01:41:15 +0400"
relations: {}
atom_id: "CA-R-1655"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1655-CORE_META_MODEL-GENERAL-REQUIREMENT--resolve-artifact-classification-from-authority-and-configuration.md
  source_atom_id: CA-R-1655
  source_atom_revision: 25
  source_sha256: b7760e3c573ae634cdf1a68ae8dbd290cc7d54f66cb8d04fb2eab16fba6b4da1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Resolve Artifact Classification from Authority and Configuration

## Scope

Artifact classifications resolved from Applicable Methodology and Project Configuration with structural context from authoritative Project Structure.

## Claim

CAPRMEDIO **must** resolve **every** Artifact's applicable classification from Applicable Methodology **and** Project Configuration, with structural context from authoritative Project Structure:

- resolve Artifact Type under the applicable Type authority.
- resolve Content Role **only** for an Atom; do **not** require a Journal **or** Projection **to** have an Atom Content Role.
- resolve a semantic route **only** **where** the applicable authority defines that classification.
- classify an unknown, disabled, stale, multiply mapped, **or** ambiguous value as an unresolved **or** failed classification, **not** as an accepted one.

a derived Scope Unit Graph **must not** replace Project Structure as structural authority. reporting a classification failure does **not** itself impose a universal mutation **or** execution prohibition; the applicable Authority Mode **and** admission rules govern that consequence.

## Details
