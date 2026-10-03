---
atom_id: CA-P-956
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    occurrent:
      - "Atom/Local Tier"
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Claim/Scope
      - Scope Unit
      - Atom/Global Tier
      - Autonomous Confidence Threshold
version: 2
updated_at: "2026-09-10 01:48:30 +0400"
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-955
---
# Update canonical three-tier RMED authority

the Assignee **must** reconcile the active CORE_META_MODEL tier-governing RMED authority with the Core / General / Standard design accepted by CA-P-955.

## Scope

(the CORE_META_MODEL Atoms identified by CA-P-952 as defining, applying, evaluating, **or** serializing Local Tier **and** its affected Scope, Global Tier, Goal, Type-admission, **and** expansion rules)

## Definition of Done

the Task is **not** Done **if** (an active in-scope rule contradicts the accepted three-tier design **or** a required R, M, E, **or** D rule is missing **or** superseded authority remains independently active **or** a replacement lacks preserved identity, revision, relation, **or** Journal provenance **or** the updated authority fails its own admitted tier rules).

## Details

FX-03 begins **only** **after** the complete FX-04 gate. update, add, replace, **or** archive only the tier-governing source Atoms. R defines the model; M defines classification; E checks it; D defines its representation. use the accepted default **and** mappings rather than inventing them. reconcile CA-R-1429 **and** the affected CA-E-428 criteria. record Tools that consume changed representations as follow-up impacts; do **not** claim runtime migration **or** edit generated APPLICABLE_METHODOLOGY.
