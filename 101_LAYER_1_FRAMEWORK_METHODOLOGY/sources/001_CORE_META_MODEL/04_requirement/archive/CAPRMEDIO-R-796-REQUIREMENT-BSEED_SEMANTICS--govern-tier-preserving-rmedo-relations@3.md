---
subject_scopes:
  - requirement-topology
tier: core
version: 3
updated_at: 2026-08-21 03:22:46
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-049--use-one-global-tier-number-for-rmed-authority
---
# Govern tier-preserving PRMEDO relations

Every active tier-classified PRMEDO Atom `child_of` edge must point to an applicable parent with a lower global tier number. Cross-scope parents must belong to the child's ancestor path; backward, equal-tier, and cross-branch authority edges are forbidden.
