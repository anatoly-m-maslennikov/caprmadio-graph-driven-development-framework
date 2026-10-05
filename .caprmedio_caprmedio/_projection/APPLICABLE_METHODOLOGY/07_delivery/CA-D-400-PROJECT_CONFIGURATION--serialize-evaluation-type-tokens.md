---
subjects:
  governs: "Atom/Content Role: Evaluation/Type"
  depends_on:
    - "Carrier"
version: 9
updated_at: "2026-10-02 19:36:21 +0400"
relations: {}
atom_id: "CA-D-400"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-400-PROJECT_CONFIGURATION--serialize-evaluation-type-tokens.md
  source_atom_id: CA-D-400
  source_atom_revision: 9
  source_sha256: 6d488f047405f008c51610d8e02070e7ef890b9d220a44ab9bde794c7a023b60
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Evaluation Type Tokens

## Scope

the serialization of Evaluation Type tokens in an Evaluation Atom File Carrier filename.

## Claim

an Evaluation Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- QA Case: `QA_CASE`.
- Evaluation Control: `EVALUATION_CONTROL`.
- Evaluation Approach: `EVALUATION_APPROACH`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details
