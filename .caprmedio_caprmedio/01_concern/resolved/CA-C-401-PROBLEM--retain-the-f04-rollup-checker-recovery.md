---
atom_id: CA-C-401
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "F04 rollup checker normalization"
  depends_on: [Analysis, Evaluation]
version: 1
updated_at: "2026-10-04 14:13:37 +0000"
relations:
  concern_about: [CA-P-1349, CA-A-1067]
---
# Summary

Retain the f04 rollup checker recovery

## Concern

The F04 rollup helper generated CA-P1401 instead of CA-P-1401, so its first membership equality check failed. This was an auxiliary identifier-normalization bug, not a source mismatch or a passed check.

## Evidences

A1067 retains the first failed check at13:59:43 UTC and the corrected same-scope passing check at14:00:17 UTC. All37 primary memberships, five aliases, two prior receipts and three unchanged Done children were then checked. No failed result is counted as accepted.

## Blast radius

Only the stated auxiliary diagnostic and its truthful evidence receipt. Required independent acceptance, source authoring and runtime proof remain separate; no gate is waived or automatic rerun campaign created.
