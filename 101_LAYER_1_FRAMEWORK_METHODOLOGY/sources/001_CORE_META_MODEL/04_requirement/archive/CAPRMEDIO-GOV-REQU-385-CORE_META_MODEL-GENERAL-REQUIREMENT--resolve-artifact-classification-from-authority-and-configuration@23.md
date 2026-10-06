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
version: 23
updated_at: "2026-09-17 04:38:15 +0000"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-385"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Resolve Artifact Classification from Authority and Configuration

CAPRMEDIO **must** resolve **every** Artifact's applicable classification from Applicable Methodology **and** Project Configuration, with structural context from authoritative Project Structure:

- resolve Artifact Type under the applicable Type authority.
- resolve Content Role **only** for an Atom; do **not** require a Journal **or** Projection **to** have an Atom Content Role.
- resolve a semantic route **only** **where** the applicable authority defines that classification.
- classify an unknown, disabled, stale, multiply mapped, **or** ambiguous value as an unresolved **or** failed classification, **not** as an accepted one.

a derived Scope Unit Graph **must not** replace Project Structure as structural authority. reporting a classification failure does **not** itself impose a universal mutation **or** execution prohibition; the applicable Authority Mode **and** admission rules govern that consequence.
