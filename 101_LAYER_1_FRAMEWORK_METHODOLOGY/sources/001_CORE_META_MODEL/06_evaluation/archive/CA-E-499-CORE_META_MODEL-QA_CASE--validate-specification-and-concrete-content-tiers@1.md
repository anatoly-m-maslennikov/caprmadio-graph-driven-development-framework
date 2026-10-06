---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Local Tier"
  depends_on:
    - "Spec Content Roles"
    - "Change Content Roles"
    - "Implementation"
    - "Atom Collection"
    - "Projection"
    - "Atom/Local Tier: Standard"
version: 1
updated_at: "2026-09-21 00:57:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-659", "CA-R-1431", "CA-R-1566", "CA-R-1567", "CA-R-1568", "CA-R-1571", "CA-M-272", "CA-D-468"]}
---
# Validate Specification and concrete content tiers

the tier Evaluation **must** reject classification that confuses specification authority with the content it governs.

- an RMED foundation governing General rules about CAPO **or** I: classify from its own Claim as Core.
- an RMED reusable rule governing Standard content: classify from its own Claim as General **when** admitted **in** its Scope Unit.
- Concern, Analysis, Plan, Operations, **or** Implementation content with an omitted tier: resolve Standard.
- promote that content **to** Core **or** General because it is reused, nested, important, **or** long-lived: reject.
- nest Workflow **or** Objective groupings: retain Standard; do **not** infer authority tiers from containment.
- deliver a Projection representing Core **and** General source Atoms: retain the source classifications **in** that representation while classifying the output as Standard; reject conversion of that Projection into an authoritative Atom.
