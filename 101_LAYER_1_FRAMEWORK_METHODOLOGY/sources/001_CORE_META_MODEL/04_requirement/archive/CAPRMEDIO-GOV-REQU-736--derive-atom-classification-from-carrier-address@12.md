---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - carrier-format
version: 12
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CAPRMEDIO-META-REQU-741--prohibit-artifact-subtypes
    - CAPRMEDIO-GOV-REQU-348--use-canonical-carrier-address-as-authority
    - CA-R-888
---
# Derive Atom classification from carrier address

GOVERNANCE derives a role-classified Atom's Atom ID from the canonical carrier basename's `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>` identity segment after any permitted Work Sequence Number, its Content role from the canonical role folder and registered uppercase role letter, its owning Scope Unit from `<CURRENT_SCOPE>` or the governed Project-root omission, its local Tier from `PRINCIPLE`, `CORE`, or the unmarked default, and its Type from the registered class short name whose uppercase projection equals `<ATOM_TYPE>`. When the Type admits a target, GOVERNANCE derives that exact Scope Unit from `<TARGET_SCOPE>` and validates the Type's target cardinality. It derives the Summary and format from `<SUMMARY_SLUG>` and `<EXT>`.

The Carrier MUST NOT repeat `atom_id`, `content_role`, `tier`, `type`, `current_scope`, or `target_scope` frontmatter when the canonical address derives those facts. For a draft the filename requires the visible empty number slot and therefore derives no Atom ID. Unknown, ambiguous, missing, duplicated, unsafe, role-inconsistent, scope-inconsistent, tier-ineligible, Type-inconsistent, or target-cardinality-inconsistent values are invalid.
