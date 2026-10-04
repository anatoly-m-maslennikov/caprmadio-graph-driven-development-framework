---
atom_id: CA-C-421
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 1
updated_at: "2026-10-04 16:55:19 +0000"
subjects:
  governs: "Source verification evidence"
  depends_on: [Operations, Implementation, Plan, Artifact/Carrier]
relations:
  concern_about: [CA-P-1444, CA-P-1445]
---
# Summary

Retain recovered source-verifier assumptions

## Concern

Two disposable source completion checks used overly specific incorrect assertions, although the saved carriers did not have those claimed defects.

## Evidences

P1445 assumed fourteen transition rows instead of deriving thirteen from the preserved seven explicit rows plus six wildcard expansions. P1444 expected a literal disclaimer rather than its saved equivalent wording. Both stopped honestly, corrected only the check assumption, and reran the bounded saved gate; source/output meaning was not altered to satisfy a verifier.

## Blast radius

These acquisition/verification incidents remain retained in the owned Plan evidence; they are not runtime failures or evidence of source acceptance. Use actual original structure and semantic disclaimers in the corrected gate. No broad verifier rewrite campaign is required.

