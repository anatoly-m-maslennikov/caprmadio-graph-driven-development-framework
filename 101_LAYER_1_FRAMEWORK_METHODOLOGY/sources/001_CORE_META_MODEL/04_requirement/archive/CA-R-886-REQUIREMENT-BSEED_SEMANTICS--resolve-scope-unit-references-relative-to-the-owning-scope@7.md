---
subject_scopes:
  - scope-topology
tier: core
version: 7
updated_at: 2026-08-22 04:00:55
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CA-R-858-REQUIREMENT-BSEED_METAMODEL--define-scope-unit-name-prefix-and-places
---
# Resolve Scope Unit references relative to the owning scope

A current Scope Unit reference made inside an Atom is interpreted relative to that Atom's owning Scope Unit. The reference selects the current unit, one exact descendant by its registered full name, or one exact sibling by its registered full name. Atom prose and frontmatter always use the registered full atomic name when they mention a current Scope Unit, for example `FRAMEWORK_ENGINE`. Scope Unit names are case-sensitive semantic tokens: `TOOLS` identifies a Scope Unit; `tools` is ordinary language and does not identify that Unit. A registered filename `scope_path_name`, such as `FR_ENGN`, is used only in an Atom filename's `<CURRENT_SCOPE>` or `<TARGET_SCOPE>` component and never substitutes for a current Scope Unit name inside Atom meaning. Faithfully preserved historical evidence may contain obsolete compact names without making them current identifiers.

Resolution must produce exactly one Scope Unit in the permitted structural position. Zero or multiple matches are invalid.
