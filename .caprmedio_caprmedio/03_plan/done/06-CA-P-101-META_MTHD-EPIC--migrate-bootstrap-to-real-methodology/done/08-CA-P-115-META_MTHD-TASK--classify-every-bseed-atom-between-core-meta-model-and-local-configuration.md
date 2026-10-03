---
atom_id: CA-P-115
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Bootstrap Atom/Methodology Source Classification
    occurrent:
      - Bootstrap Authority Reconciliation
  depends_on:
    occurrent:
      - CA-P-107
version: 1
updated_at: 2026-08-27 03:31:51 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Classify Every BSEED Atom Between Core Meta-Model and Local Configuration

**when** CA-P-107 is Done, **then** the Assignee **must** classify every BSEED Atom as CORE_META_MODEL or LOCAL_CONFIGURATION before CA-P-108 resumes.

## Scope

`((the CA-P-102 frozen BSEED Carrier frontier) union (the CA-P-108 unresolved normal Bootstrap Carrier set) union (every revision and lifecycle Carrier of each classified BSEED Atom) union (the accepted Core, Local Configuration, compilation, Job, default-Type, and self-application authority that determines one classification))`

## Definition of Done

the Task is **not done if** (any of the 563 frozen normal Bootstrap Carriers lacks exactly one CORE_META_MODEL or LOCAL_CONFIGURATION classification **or** any BSEED Atom identity lacks revision and lifecycle coverage **or** any methodology-source-eligible Carrier lacks one exact final Source Layer path **or** any Concern, Analysis, Plan, Implementation, or Ops work, history, evidence, or plan-structure Carrier is treated as compiled methodology authority **or** any non-source Carrier lacks the exact `OUT_OF_SCOPE_RETAIN_IN_PLACE` disposition with its current path as final path **or** any classification uses only folder inheritance rather than the Atom Claim and its exact evidence **or** any Core classification admits a Project-specific selection, topology, non-minimal default, migration choice, mode, or customization **or** any Local Configuration classification omits a Project-specific selection, topology, non-minimal default, migration choice, mode, or customization **or** any active default-Type Claim conflicts with the accepted default-Type boundary **or** the Core self-application recursion is not represented by one-Claim authority Atoms **or** any final target collision, unclassified successor, or unresolved semantic category remains).

## Details

classify an Atom as CORE_META_MODEL only when its Claim is necessary and sufficient to interpret, extend, configure, or self-apply CAPRMEDIO through canonical Entities, relations, invariants, extension mechanisms, configuration mechanisms, Carrier mechanisms, or minimal default Atom Types. classify every other Claim as LOCAL_CONFIGURATION. CORE_META_MODEL owns exactly the default Concern Types QUESTION, CONFLICT, and PROBLEM; it owns exactly the default Analysis Types ANALYSIS_REPORT and RATIONALE; and it uses Local Tiers PRINCIPLE, CORE, and STD rather than default Atom Types for Plan, Requirement, Method, Evaluation, Delivery, Implementation, and Ops. CORE local Tier and CORE_META_MODEL Source Layer are independent coordinates. retain every non-source BSEED Concern, Analysis, Plan, Implementation, Ops, history, evidence, and plan-structure Carrier at its current path with disposition `OUT_OF_SCOPE_RETAIN_IN_PLACE`; record its semantic classification but do not compile or relocate it. retain Core and Local source-eligible revision history in the matching Source Layer and Content Role lifecycle folder. preserve `.caprmedio_install` in place. record exact source path, digest, Atom identity, Claim evidence, classification reason, lifecycle coverage, disposition, and exact target for every frozen Carrier.

## Task Scope Resolution

the Operator established this prerequisite after CA-P-108 found 563 unresolved normal Bootstrap Carriers. every non-source BSEED history, Plan, evidence, and plan-structure Carrier remains exactly at its current path with disposition `OUT_OF_SCOPE_RETAIN_IN_PLACE`; no Bootstrap-history topology or Project-carrier relocation is introduced. CA-P-108 resumes only after this Task supplies its complete deterministic classification evidence.

## Completion Record

PASS. [CA-P-115 BSEED Atom classification](../execution_evidence/CA-P-115-bseed-atom-classification.projection.json) records one claim-evidenced CORE_META_MODEL or LOCAL_CONFIGURATION classification for all 563 normal Bootstrap Carriers: 440 Core Meta-Model source Carriers, 45 Local Configuration source Carriers, 74 non-source retain-in-place Carriers, and four superseded default-Type predecessors. It covers all 2,869 frozen BSEED Carriers and 1,310 identities, retains every non-source Carrier at its current path, and records one exact final target for every source-eligible Carrier. CA-R-1231 through CA-R-1234 reconcile the default-Type and coordinate boundary. CA-R-1235 through CA-R-1239 state the required self-application recursion as separate one-Claim Core authority Atoms. The evidence reports zero target collisions, zero unclassified normal Carriers, and no revision-identity classification disagreement. Every Definition-of-Done condition passes at 99 percent execution confidence.
