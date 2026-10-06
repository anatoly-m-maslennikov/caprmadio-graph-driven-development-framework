---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Content Role"
  depends_on:
    - "Atom/Claim"
    - "Atom/Local Tier: Principle"
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role: Plan/Type: Objective"
    - "Actor"
    - "Action"
    - "Process"
    - "Artifact/Carrier"
version: 2
updated_at: "2026-09-17 04:55:03 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1282
    - CA-R-1338
    - CA-R-1339
    - CA-R-1340
    - CA-R-1341
    - CA-R-1342
    - CA-R-1344
    - CA-R-1018
---
# Validate Principle Content-role semantics

a Principle's Content Role classification **must** fail this Evaluation **if** its complete Claim's primary contribution does **not** match the applicable Content Role definition.

## role distinctions

- Operations covers reusable operational behavior **or** Actor participation/authorization policy, **not** a Claim merely mentioning an Actor **or** Operation.
- Requirement covers required outcomes, obligations, permissions, prohibitions, **or** externally observable boundaries according **to** its primary model contribution.
- Delivery covers what a Carrier stores **and** how it represents **or** places that content.
- Method covers an Implementation choice **or** convention, **not** the authoritative operational Action **or** Process definition.
- Evaluation covers a falsifiable check, acceptance criterion, **or** disposition rule. its checked authority follows CA-R-1018 **and** is **not** limited **to** RMED Spec.
- intended Task **or** Objective content belongs **to** Plan, **not** Operations merely because its intended work involves an Actor.

the semantic test uses the complete Claim **and** does **not** require a literal wording template. the active Content Role definitions remain the authority for these distinctions; this Evaluation does **not** create a second classification system.
