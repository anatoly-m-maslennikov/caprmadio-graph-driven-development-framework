---
atom_id: CA-C-317
content_role: Concern
type: Problem
label: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "CA-P-1298 context retention"
relations:
  concern_about: [CA-P-1298]
version: 2
updated_at: "2026-10-04 13:41:16 +0400"
---
# Summary

P1298 parser used the wrong frozen-context key

## Concern

Initial A1016 extraction looked for `context_only_messages` instead of the Plan binding's actual `context_only` array, leaving the initial literal-context container empty. The16 full bound contexts4331characters were appended from the correct array. This repair adds zero source coverage.

## Evidences

The actual P1298 binding has top-level `context_only` with16 complete records. A1016's separate retained-context JSON array contains all16 exact records/native parts/text/full metadata/fingerprints and16 individual dispositions; its initial empty context placeholder is historical extraction structure, not unavailable source evidence. Read-only native/saved proof passed2026-10-04 09:27:20UTC: all16saved records equal the binding, each native rawSHA256/parts/time/role/channel/textSHA256/character count matches. The68 selected records/aggregate andactualnextbinding also passed. Resolution is literal recovery/native proof only; no semantic next execution/current adoption is inferred.

## Blast radius

Only P1298/A1016 context retention was affected. Full literal yes/question/CCE/operation/same-goal antecedents are recoverable;68 selected substantive coverage andthefrozenmonthlycutoff are unchanged. Original elapsed-limit recovery is separately C318.
