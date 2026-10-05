---
subjects:
  governs: "Authorize Structural Change"
  depends_on:
    - "Action"
    - "Project Structure"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 5
updated_at: "2026-10-04 15:08:26 +0000"
relations: {}
atom_id: "CA-O-013"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-013-CORE_META_MODEL-ACTION--authorize-structural-change.md
  source_atom_id: CA-O-013
  source_atom_revision: 5
  source_sha256: eeb3c6426669b778c0dc44c28065eeff51f2af3b4a0aef5af3e924b505e1bbe9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Authorize structural change

## Operation

Authorize Structural Change **means** the Action that checks a structural change proposal against the Operator's actual authorization **and** the effective Autonomous Confidence Threshold, returning permission for the exact proposed effects **or** a blocked decision with its reason. existing authorization **may** cover those effects; a new approval **must** be requested **if** they exceed it, conflict resolution requires it, **or** uncertainty fails the effective threshold. approval **must** remain bound **to** the proposal **and** selected source state. this Action **must not** infer permission from a folder observation, a generated result, confidence alone, **or** the existence of a Plan.

## Details
