---
subjects:
  governs: "Step Run/Tool Call"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Step"
    - "Action"
    - "Tool"
    - "Journal"
    - "Projection"
version: 4
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-R-1528", "CA-R-1511"]}
atom_id: "CA-E-496"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-496-CORE_META_MODEL-QA_CASE--validate-nested-tool-call-evidence.md
  source_atom_id: CA-E-496
  source_atom_revision: 4
  source_sha256: 7122717a9d94a903bd4268393ebf9dacfac2da9450b55cbf6a800fb7ec311b31
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate nested Tool-call evidence

## Scope

Tool-call evidence within a Step Run.

## Claim

the Evaluation **must** check Tool-call evidence within a Step Run under CA-R-1528.

## Details

- an Agentic Action makes several Tool calls: require their actual parent Step Run, Tool identities, inputs **or** admitted protected references, results **or** errors, **and** distinguishing call evidence.
- a repeated attempt uses the same Tool **and** inputs: preserve distinct attempt identities **without** claiming a second effect **when** its outcome is unknown.
- a Tool call fails **or** its effect cannot be confirmed: retain that outcome rather than recording successful completion.
- a nested trace is rebuilt: require derivation from the canonical Journal **without** another source of execution history.
- a Tool call automatically creates a Workflow Step, ON_RESULT edge, **or** new Action definition: reject that inference.
- secret input is encountered: require its governed protected representation rather than plaintext duplication for trace completeness.

missing evidence **or** an unperformed check is **not** a passing result.
