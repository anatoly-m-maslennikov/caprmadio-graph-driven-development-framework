---
subject_scopes:
  - authority
version: 2
updated_at: 2026-08-21 03:22:46
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-155--classify-rmed-atoms-by-applicability-tier
---
# Route priority and tier by Content role

Concern Atoms and action-point Plan Atoms use `priority` for current disposition or execution order and do not use `tier`. `action_policy` Plan Atoms and RMEDO Atoms together form the PRMEDO roles eligible for applicability tiers and do not use `priority` when tier-classified. Analysis and Implementation Atoms use neither property by default because their ordering or normative breadth is inherited from the governed work, Claim, or realization they serve; non-tier-classified Ops Atoms likewise use neither property by default.
