---
content_role: Requirement
type: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Implementation"
  depends_on:
    - "Analysis"
    - "Atom/Claim"
    - "Evaluation"
    - "Evidence"
    - "Projection"
version: 2
updated_at: "2026-09-23 20:47:56 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1470", "CAPRMEDIO-META-REQU-097", "CAPRMEDIO-META-REQU-657"]}
---
# Summary

Separate legacy observations from refactoring decisions

## Claim

reverse-engineering results **must** distinguish observed Implementation facts from proposed decisions about the intended refactored result.

- identify behavior **or** constraints proposed for preservation.
- identify behavior **or** constraints proposed for change.
- identify unresolved behavior, missing evidence, **and** uncertain interpretations.

an observed behavior **or** defect **must not** become a Requirement merely because it exists **in** the legacy Implementation. preserve supporting evidence **without** presenting a proposed disposition **or** uncertainty as an observed fact.
