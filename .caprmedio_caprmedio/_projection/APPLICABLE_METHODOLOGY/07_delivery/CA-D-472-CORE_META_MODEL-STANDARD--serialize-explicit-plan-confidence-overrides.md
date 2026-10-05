---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Autonomous Confidence Threshold"
    - "Hub Atom"
    - "File Carrier"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
version: 5
updated_at: "2026-10-02 19:44:54 +0400"
relations: {"relates_to": ["CA-D-460", "CA-D-470", "CA-M-271", "CA-R-1428"]}
atom_id: "CA-D-472"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-472-CORE_META_MODEL-STANDARD--serialize-explicit-plan-confidence-overrides.md
  source_atom_id: CA-D-472
  source_atom_revision: 5
  source_sha256: ccda5b5fdacef80965b8eaaee28e6a5a44ff6f10c89111bb8748a2d4bba2be90
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize explicit Plan confidence overrides

## Scope

explicit Plan Autonomous Confidence Threshold overrides in Plan Atom Markdown File Carriers.

## Claim

an explicit Plan Autonomous Confidence Threshold override **must** use the top-level integer frontmatter field `autonomous_confidence_threshold` **in** that Plan Atom's own mandatory Markdown File Carrier.

- a Hub uses that same file, **not** a separately identified Objective **or** Epic settings file.
- omit an unselected override **without** copying its inherited value; the mandatory file requirement does **not** turn inheritance into a local selection.
- retain an explicit override even **when** it equals the inherited value.
- `epic_overrides` is **not** an alternative canonical encoding.

## Details
