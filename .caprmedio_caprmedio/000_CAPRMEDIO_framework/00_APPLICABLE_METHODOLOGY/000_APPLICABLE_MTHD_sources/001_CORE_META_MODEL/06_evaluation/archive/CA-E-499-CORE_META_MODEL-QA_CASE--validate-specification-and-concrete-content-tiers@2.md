---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Local Tier"
  depends_on:
    - "Spec Content Roles"
    - "Change Content Roles"
    - "Atom/Content Role"
    - "Atom/Scope"
    - "Atom/Subjects"
    - "Implementation"
    - "Atom Collection"
    - "Projection"
    - "Atom/Local Tier: Standard"
version: 2
updated_at: "2026-09-21 15:41:53 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-659", "CA-R-1431", "CA-R-1566", "CA-R-1567", "CA-R-1568", "CA-R-1571", "CA-M-272", "CA-D-468", "CA-R-1572"]}
---
# Validate Specification and concrete content tiers

the tier Evaluation **must** reject classification that confuses specification authority with the content it governs.

- an RMED foundation governing General rules about CAPO **or** I: classify from its own Claim as Core.
- an RMED reusable rule governing Standard content: classify from its own Claim as General **when** admitted **in** its Scope Unit.
- Concern, Analysis, Plan, Operations, **or** Implementation content with an omitted tier: resolve Standard.
- promote that content **to** Core **or** General because it is reused, nested, important, **or** long-lived: reject.
- nest Workflow **or** Objective groupings: retain Standard; do **not** infer authority tiers from containment.
- deliver a Projection representing Core **and** General source Atoms: retain the source classifications **in** that representation while classifying the output as Standard; reject conversion of that Projection into an authoritative Atom.

## Cross-role governance fixtures

- apply **`=1`** Core Requirement foundation **to** applicable General Requirement, Method, Evaluation, **and** Delivery rules: accept **all** four roles, **not** **only** Requirement.
- apply a General rule **to** applicable Standard Atoms **in** (Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, Operations): retain **every** applicable target regardless of its Content Role.
- reject **only** the cross-role targets while retaining same-role targets: fail this Evaluation.
- keep the tier ordering but make a target unrelated **to** the governing Scope **or** Subject: do **not** infer applicability merely from its lower Local Tier.
- assign General **to** a CAPO **or** I Atom **to** manufacture another cross-role target: reject under CA-R-1566; cross-role governance does **not** waive tier admission.
