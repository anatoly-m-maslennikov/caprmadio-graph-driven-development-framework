---
subject_scopes:
  - applicability
version: 6
updated_at: 2026-08-22 04:00:55
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-R-795-REQUIREMENT-BSEED_SEMANTICS--admit-applicability-tiers-across-rmedo
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-299--effective-priority-conflict-selection
---
# Encode PRMEDO applicability tiers

GOVERNANCE retains `principle`, `core`, and `standard` as the ordered semantic local applicability-tier catalog. A tier-classified PRMEDO Markdown Atom encodes local tier `principle` with filename marker `PRINCIPLE`, encodes local tier `core` with filename marker `CORE`, and encodes the default lower local tier `standard` by omitting the local-tier filename segment. Omission leaves no empty separator. The canonical filename is the sole authority for the local tier, so active and draft Atoms omit `tier` and `priority` frontmatter. Intent is outside PRMEDO and the local tier catalog while occupying global tier `-1`.

Applicable Atoms register the readable tier catalog and the `standard` default. Project Graph State Projections expose the enabled local tiers and every global number produced by recursive Structural-level derivation for each current level and Scope Unit without becoming authority for them. Validators reject an unknown local-tier marker, a marker disabled for the Structural level, a marker on a tier-ineligible Type, an omitted marker when the default is disabled, or `tier` or `priority` frontmatter on a tier-classified PRMEDO Atom.
