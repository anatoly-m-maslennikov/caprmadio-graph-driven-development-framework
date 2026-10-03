---
cce_version: cce_1
cce_form: evaluation
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
version: 3
updated_at: "2026-09-21 15:52:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-659", "CA-R-1431", "CA-R-1566", "CA-R-1567", "CA-R-1568", "CA-R-1571", "CA-M-272", "CA-D-468", "CA-R-1573"]}
---
# Validate Specification and concrete content tiers

the tier Evaluation **must** reject classification that confuses specification authority with the content it governs.

- an RMED foundation governing **all** greater Global Tiers **in** its Scope Unit, including General rules **and** Standard CAPO **or** I content: classify from its own Claim as Core.
- an RMED reusable rule governing Standard content: classify from its own Claim as General **when** admitted **in** its Scope Unit.
- Concern, Analysis, Plan, Operations, **or** Implementation content with an omitted tier: resolve Standard.
- promote that content **to** Core **or** General because it is reused, nested, important, **or** long-lived: reject.
- nest Workflow **or** Objective groupings: retain Standard; do **not** infer authority tiers from containment.
- deliver a Projection representing Core **and** General source Atoms: retain the source classifications **in** that representation while classifying the output as Standard; reject conversion of that Projection into an authoritative Atom.

## Global Tier governance fixtures

- place Atoms at Global Tiers `N`, `N+1`, **and** `N+2` **in** one Scope Unit: `N` governs **all** Atoms at `N+1` **and** `N+2`; `N+1` governs **all** Atoms at `N+2`.
- leave `N+1` unoccupied: `N` still governs **all** Atoms at `N+2`; governance does **not** require an intermediate Atom **or** an explicit tier-parent chain.
- at the Scope Unit's Standard Global Tier, include (Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, Operations): **all** remain governed by **every** Atom at a numerically smaller Global Tier **in** that Scope Unit.
- give the higher-tier Atom **and** a lower-tier target different Subjects **or** different Content Roles: retain the governance; matching either is **not** a prerequisite.
- restrict governance **to** the next tier, **to** Requirement targets, **or** **to** matching Subjects: fail this Evaluation.
- infer governance between equal Global Tiers **or** from `N+1` **to** `N` from this rule: fail; those are **not** greater-tier targets.
- assign General **to** a CAPO **or** I Atom: reject under CA-R-1566; Global Tier governance does **not** waive tier admission.
