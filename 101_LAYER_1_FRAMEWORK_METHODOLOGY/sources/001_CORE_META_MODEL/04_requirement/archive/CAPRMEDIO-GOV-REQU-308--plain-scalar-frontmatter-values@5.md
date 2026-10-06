---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - carrier-format
version: 5
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
  relates_to:
    - CAPRMEDIO-GOV-REQU-307--atomic-subject-scope-cardinality
    - CAPRMEDIO-GOV-CNST-001--github-preview-compatibility
---
# Keep frontmatter values ready for plain scalars

CAPRMEDIO-controlled frontmatter keys and string values are designed for unambiguous YAML plain-scalar storage. CAPRMEDIO-authored Markdown therefore emits those values without quotation marks.

Controlled property keys use `snake_case`. Controlled vocabulary values use lowercase `kebab-case` unless the property's registered grammar requires another stable form, such as an artifact ID, `scope_path`, relation kind, URL, or LLM session reference.

Every registered string grammar MUST:

- contain no whitespace or control characters;
- use only letters, digits, `.`, `_`, `-`, `/`, or `:` unless an external standard requires another YAML-safe character;
- avoid YAML booleans, nulls, numbers, dates, timestamps, directives, tags, anchors, aliases, collection syntax, and comment syntax; and
- preserve the same string meaning when parsed as YAML 1.2.

Lists use block sequence syntax with one plain scalar per item. Structured properties use block mappings. Human prose belongs in the Markdown body. Uncontrolled external literals that cannot satisfy a registered safe grammar are represented in the body or through a governed reference rather than forcing quoted free-form strings into frontmatter.
