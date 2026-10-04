---
atom_id: CA-C-411
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Source-authoring saved Carrier validation"
  depends_on: [Artifact/Carrier, Plan]
version: 1
updated_at: "2026-10-04 15:40:40 +0000"
relations:
  concern_about: [CA-P-1131]
---
# Summary

Repair the source save validation root

## Concern

the source-save diagnostic initially selected the Docker worker's default working directory instead of its mounted Project root and therefore found none of its forty explicitly selected source Carriers.

## Evidences

the failed diagnostic changed no files. inspection of the existing worker mount identified `/project` as the correct root. the unchanged saved YAML, heading and whitespace checks then passed for all forty source Carriers, fifteen Done child Plans, P1131 and its five retained Concerns. the separate staged whitespace gate exited zero before actual Git commit `9924250ac`. this validation does not claim independent review, runtime acceptance or resolution of CA-C-410's directory-move denial.

## Blast radius

this disposable source-save validation invocation only. the root correction is verified and no unfinished diagnostic remainder remains.
