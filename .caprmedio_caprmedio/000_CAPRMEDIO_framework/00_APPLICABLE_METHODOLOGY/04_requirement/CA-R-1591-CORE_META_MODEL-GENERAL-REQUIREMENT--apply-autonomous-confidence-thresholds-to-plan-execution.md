---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Autonomous Confidence Threshold"
    - "Operator"
    - "AI Agent"
version: 4
updated_at: "2026-10-03 00:47:46 +0400"
relations: {"relates_to": ["CA-R-1587", "CA-M-271"]}
atom_id: "CA-R-1591"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1591-CORE_META_MODEL-GENERAL-REQUIREMENT--apply-autonomous-confidence-thresholds-to-plan-execution.md
  source_atom_id: CA-R-1591
  source_atom_revision: 4
  source_sha256: 3f42557e69c77dd597d05da1506c42ee86799e97e61128c2c06ad586f9f27e79
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Apply autonomous confidence thresholds to Plan execution

## Scope

autonomous continuation of Plan work.

## Claim

autonomous continuation of Plan work **must** satisfy its effective Autonomous Confidence Threshold:

- resolve the value under CA-M-271-CORE_META_MODEL-METHOD--resolve-confidence-thresholds-by-source-precedence.
- **if** confidence **in** correct execution is below it, request Operator disposition **before** continuing.
- **otherwise**, continue **only** within existing authority; meeting the threshold does **not** grant additional authority.

## Details
