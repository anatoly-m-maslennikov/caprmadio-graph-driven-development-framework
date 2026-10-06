---
subject_scopes:
  - carrier-format
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 7
updated_at: 2026-08-21 04:43:43
relations:
  child_of:
    - CAPRMEDIO-META-REQU-165--atoms-have-version-and-updated-at
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Encode Atom revision properties

Every Atom Revision encoding carries `version` as a positive integer and `updated_at` in `YYYY-MM-DD HH:MM:SS` format interpreted in the configured Artifact timestamp timezone. Markdown Atoms encode both properties in YAML frontmatter. A registered native Atom whose executable format excludes governance metadata encodes both properties in its governed external revision binding. Atom ID is an Atom identity derived from the canonical Carrier filename's immutable Atom-ID segment, not a Revision or frontmatter property; a draft has no assigned Atom ID. Creation writes version one; every committed edit to the Atom Carrier contents, including a carrier-only correction, increments `version` by exactly one and updates `updated_at` in the same operation. A path-only lifecycle move changes neither Revision property, while a replacement Atom starts at version one.
