---
subject_scopes:
  - authority
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-002--apply-mece-to-canonical-decompositions
    - CAPRMEDIO-REQU-003--apply-dry-across-caprmedio
---
# Single owner rule placement

Every governed claim has exactly one authoritative owner. Place it in the earliest layer that can define it completely while respecting the META eligibility rule.

Downstream layers may reference, specialize, realize, check, or observe earlier truth. They must not copy the claim into a second authority. Paths, filenames, directory numbers, hubs, diagrams, generated views, evidence, and implementation do not create authority by appearance.

If defining a proposed upstream rule requires entities owned only by a later layer, the rule is misplaced. Move it to the earliest complete owner or split the stable invariant from its downstream mechanism.
