---
atom_id: CA-P-953
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    occurrent:
      - "Scope"
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Claim/Scope
      - Scope Unit
      - Atom/Local Tier
      - Atom/Global Tier
      - Autonomous Confidence Threshold
version: 2
updated_at: "2026-09-10 01:48:30 +0400"
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-952
---
# Specify Scope derivation independent from Local Tier

the Assignee **must** specify the Scope derivation rule that preserves the intended Scope **when** Local Tier distinguishes Core, General, **and** Standard.

## Scope

(the active CORE_META_MODEL authority for Scope derivation **and** its dependence on Local Tier, including CA-R-931, CA-R-922, CA-R-1287, CA-R-659, CA-R-660, **and** their direct affected rules)

## Definition of Done

the Task is **not** Done **if** (the proposed rule cannot identify its authoritative Scope-defining inputs **or** reclassification alone can silently change the intended Scope **or** default, empty, composite, inherited, **or** relational cases have an unresolved interpretation **or** an unresolved material decision is accepted below the effective Autonomous Confidence Threshold).

## Details

FX-04: produce a reviewable specification, **not** active authority changes. use CA-P-952 as the evidence frontier. distinguish structural ownership, Claim Scope, **and** Local Tier. do **not** create a separate Task Scope model. reuse existing Entities **and** Relations; ask the Operator one question at a time **if** a required design decision remains below the effective threshold.
