---
subject_scopes:
  - principles
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-273--use-canonical-carrier-address-as-authority
    - CAPRMEDIO-META-REQU-135--write-context-complete-minimal-atom-prose
---
# Economical, readable YAML frontmatter

Every CAPRMEDIO YAML frontmatter schema must use the least syntax and nesting
that preserves unambiguous meaning, deterministic parsing and validation,
required extensibility, and immediate human readability.

A key, wrapper, discriminator, or repeated value is forbidden when its meaning
is already determined by the canonical carrier address, parent key, registered
Type, or value shape. Syntax economy must not depend on positional conventions,
ambiguous shorthand, or hidden inference that makes a carrier harder to read,
validate, extend, or diagnose.
