---
subject_scopes:
  - artifact-identity
version: 11
updated_at: 2026-08-22 04:00:55
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-304--expandable-scope-path-identities
  child_of:
    - CAPRMEDIO-META-REQU-728--separate-immutable-atom-id-from-mutable-scope
    - CAPRMEDIO-META-REQU-730--preserve-atom-id-across-scope-change
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-GOV-REQU-764--register-content-role-identity-letters
    - CA-R-888
---
# Place immutable Atom ID before mutable scope path

Every accepted role-classified Markdown Atom canonically encodes its Atom ID `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>` as the immutable leading segment of its Carrier filename and must not repeat it in `atom_id` frontmatter. Its complete filename uses this grammar:

`<ATOM_ID>[-<CURRENT_SCOPE>][-<LOCAL_TIER>]-<ATOM_TYPE>[-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`

`<CURRENT_SCOPE>` occurs exactly once for a non-Project owner and identifies that Scope Unit through its registered filename `scope_path_name`; it is omitted when the owning Scope Unit is the Project root. `<LOCAL_TIER>` is `PRINCIPLE` or `CORE`; omission derives the default lower local tier and leaves no empty segment. `<ATOM_TYPE>` is the uppercase filename projection of the registered class short name. `<TARGET_SCOPE>` is required exactly once or prohibited by the Atom Type; prohibition is the default. When present, it identifies exactly one distinct Scope Unit through its registered filename `scope_path_name`. `--` occurs exactly once after the structured filename facts and before the Summary slug.

A draft uses `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>--[<CURRENT_SCOPE>-][<LOCAL_TIER>-]<ATOM_TYPE>[-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`; the empty number slot is a visible absence marker, not an Atom ID. The draft omits `<CURRENT_SCOPE>` only for the Project root. An expressly registered native Atom whose executable filename cannot carry this grammar uses its governed external Atom binding.

Atom ID, current Scope Unit, local Tier, Type, target Scope Unit, Summary, extension, and the complete filename are distinct Carrier-address facts. Once accepted, every filename Revision of the same Atom must preserve the assigned Atom-ID segment. A change to mutable current scope, Tier, Summary, or extension may rename the same Atom under its governing rule. A change to an identity-bearing Type or to the Claim's target creates a successor Atom when it changes the primary atomic meaning.
