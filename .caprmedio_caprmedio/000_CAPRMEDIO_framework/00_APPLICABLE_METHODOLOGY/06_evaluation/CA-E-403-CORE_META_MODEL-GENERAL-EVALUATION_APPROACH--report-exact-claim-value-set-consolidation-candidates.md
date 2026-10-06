---
subjects:
  governs: "Claim Value Set Consolidation Candidate Evaluation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Scope"
    - "Atom/Governed Subject"
    - "Claim Value Set"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 12
updated_at: "2026-10-02 20:03:51 +0400"
relations:
  evaluation_for:
    - CA-R-1358
    - CA-R-1359
atom_id: "CA-E-403"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-403-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--report-exact-claim-value-set-consolidation-candidates.md
  source_atom_id: CA-E-403
  source_atom_revision: 12
  source_sha256: 3aa9a341876eee5a153e923a4a7d4fadc400d69b2925ff11a7c25c278fa444c9
  original_relations_sha256: 520fb5ded33b8149da4371614ad71a1b5b9bfed9da1d8e54cedf4ae9c0eacd52
---
# Summary

Report Exact Claim Value-Set Consolidation Candidates

## Scope

Claim Value Set consolidation candidates.

## Claim

the Evaluation **must** report **`=1`** Claim Value Set consolidation candidate **only** **if** **every** contributing active Atom has the same Atom Scope, Atom Governed Subject, Claim Target Scope Unit, textual Claim Scope, Property, **and** exact qualifiers, has **`=1`** mechanically parseable single-value Claim, **and** differs **only** by **`=1`** unique value proven through IS_ALLOWED_VALUE_OF for that Property; it **must not** mutate, merge, archive, replace, compile, **or** change a Source Atom by another operation, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation **to** fail.

## Details
