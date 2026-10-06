---
subjects:
  governs: "CCE Operator Registry"
  depends_on:
    - "CCE Operator"
    - "CCE Method"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-234"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-234-CORE_META_MODEL--register-expandable-canonical-cce-operator-list.md
  source_atom_id: CA-M-234
  source_atom_revision: 12
  source_sha256: 76e25a9c4bc88ecf5d9e44f7379ed4ba421e3248ae80583efef48ac2e43ad2c5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Register Expandable Canonical CCE Operator List

## Scope

the canonical CCE Operator Registry.

## Claim

the current canonical CCE Operator Registry **must** contain this expandable set:

1. statement form: **to**, **means**.
2. modality: **must**, **must not**, **may**.
3. condition: **if**, **then**, **when**, **otherwise**.
4. temporal condition: **before**, **after**, **until**, **unless**.
5. quantification: **all**, **every**, **any**, **none**.
6. logical/set: **and**, **or**, **not**, **without**, **where**.
7. restriction: **only**.
8. predicate: **in**, **not in**, **is empty**, **is not empty**, **contains**, **starts with**, **ends with**.
9. comparison: **`=`**, **`!=`**, **`<`**, **`<=`**, **`>`**, **`>=`**.

## Details

another token **may** enter the CCE Operator Registry **when** one active CCE Method assigns the token one syntactic **or** logical function.
