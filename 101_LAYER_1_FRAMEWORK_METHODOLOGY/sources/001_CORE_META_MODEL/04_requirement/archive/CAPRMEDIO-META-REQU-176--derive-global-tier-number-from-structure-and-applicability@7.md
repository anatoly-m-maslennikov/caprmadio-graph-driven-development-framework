---
subject_scopes:
  - requirement-topology
tier: core
version: 7
updated_at: 2026-08-20 18:26:25
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-031--model-project-structure-as-numbered-levels
    - CAPRMEDIO-REQU-049--use-one-global-tier-number-for-rmed-authority
---
# Derive global tier number from structure and applicability

CAPRMEDIO assigns Intent global tier `-1`; Project Principle, Core, and Standard global tiers `0`, `1`, and `2`; and each child Scope Unit's Core and Standard the next two global tiers after its immediate parent's Standard, repeating that derivation recursively while peer Scope Units at one Structural level share one mapping.
