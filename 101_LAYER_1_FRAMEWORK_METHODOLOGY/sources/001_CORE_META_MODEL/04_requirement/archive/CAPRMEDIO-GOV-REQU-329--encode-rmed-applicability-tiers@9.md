---
subject_scopes:
  - applicability
project_settings:
  authority:
    tiers:
      default: standard
version: 9
updated_at: 2026-08-20 02:38:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-177--limit-applicability-tiers-to-rmed-authority
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-299--effective-priority-conflict-selection
---
# Encode RMED applicability tiers

GOV encodes Goal and Principle as Requirement Types while retaining `principle`, `core`, and `standard` as the ordered applicability-tier catalog. Each active or draft tier-classified RMED Markdown Atom resolves `tier` to one registered readable catalog name and omits `priority`; Goal derives its global tier from its structural position without joining the local tier catalog. Project settings register the ordered readable tier catalog and every global number produced by the recursive parent-Standard to child-Goal handoff. Validators reject unknown names, invalid Type and Structural-scope combinations, role-ineligible tiers, numeric tier values in Atoms, and `priority` on tier-classified RMED Atoms.
