---
cce_version: cce_1
cce_form: obligation
subjects:
  - settings
version: 7
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-619--classify-project-configuration-as-an-implementation-atom
---
# Encode Project Configuration as a native TOML Atom

The native Project Configuration TOML Atom MUST encode operator-editable confidence thresholds; the `.caprmedio` control-root locator; one or more code-root locators; active and background Tools with their settings; and enabled or disabled Extensions with retained per-Extension settings. Installation state is not an activation setting, and retained settings for a disabled Extension do not enable it. The carrier MAY include human-readable configuration comments but MUST NOT embed YAML frontmatter, `atom_id`, Revision metadata, relations, rationale, or provenance. A governed external Atom binding carries those properties for this native Atom.
