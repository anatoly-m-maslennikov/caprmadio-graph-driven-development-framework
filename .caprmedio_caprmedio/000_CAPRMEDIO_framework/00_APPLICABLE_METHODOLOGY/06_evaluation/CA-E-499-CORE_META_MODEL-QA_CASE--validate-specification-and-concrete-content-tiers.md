---
subjects:
  governs: "Atom/Local Tier"
  depends_on:
    - "Spec Content Roles"
    - "Change Content Roles"
    - "Atom/Content Role"
    - "Atom/Global Tier"
    - "Scope Unit"
    - "Atom/Subjects"
    - "Implementation"
    - "Atom Collection"
    - "Projection"
    - "Atom/Local Tier: Standard"
version: 7
updated_at: "2026-10-01 21:33:03 +0400"
relations: {"evaluation_for": ["CA-R-659", "CA-R-1431", "CA-R-1566", "CA-R-1567", "CA-R-1568", "CA-R-1571", "CA-M-272", "CA-D-484", "CA-R-1573"]}
atom_id: "CA-E-499"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-499-CORE_META_MODEL-QA_CASE--validate-specification-and-concrete-content-tiers.md
---
# Summary

Validate Specification **and** concrete content tiers

## Scope

classification of specification authority and concrete content tiers.

## Claim

the tier Evaluation **must** reject classification that confuses specification authority with the content it governs.

- an RMED foundation governing **all** greater Global Tiers **in** its Scope Unit, including General rules **and** Standard CAPO **or** I content: classify from its own Claim as Core.
- an RMED reusable rule governing Standard content: classify from its own Claim as General **when** admitted **in** its Scope Unit.
- Concern, Analysis, Plan, Operations, **or** Implementation content carries Standard internally; an omitted filename tier token represents that same value.
- promote that content **to** Core **or** General because it is reused, nested, important, **or** long-lived: reject.
- nest Workflow **or** Objective groupings: retain Standard; do **not** infer authority tiers from containment.
- deliver a Projection representing Core **and** General source Atoms: retain the source classifications **in** that representation while classifying the output as Standard; reject conversion of that Projection into an authoritative Atom.

### Global Tier governance fixtures

- place Atoms at Global Tiers `N`, `N+1`, **and** `N+2` **in** one Scope Unit: `N` governs **all** Atoms at `N+1` **and** `N+2`; `N+1` governs **all** Atoms at `N+2`.
- leave `N+1` unoccupied: `N` still governs **all** Atoms at `N+2`; governance does **not** require an intermediate Atom **or** an explicit tier-parent chain.
- at the Scope Unit's Standard Global Tier, include (Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, Operations): **all** remain governed by **every** Atom at a numerically smaller Global Tier **in** that Scope Unit.
- give the higher-tier Atom **and** a lower-tier target different Subjects **or** different Content Roles: retain the governance; matching either is **not** a prerequisite.
- restrict governance **to** the next tier, **to** Requirement targets, **or** **to** matching Subjects: fail this Evaluation.
- infer governance between equal Global Tiers **or** from `N+1` **to** `N` from this rule: fail; those are **not** greater-tier targets.
- assign General **to** a CAPO **or** I Atom: reject under CA-R-1566-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-change-and-implementation-content-at-standard; Global Tier governance does **not** waive tier admission.

## Details
