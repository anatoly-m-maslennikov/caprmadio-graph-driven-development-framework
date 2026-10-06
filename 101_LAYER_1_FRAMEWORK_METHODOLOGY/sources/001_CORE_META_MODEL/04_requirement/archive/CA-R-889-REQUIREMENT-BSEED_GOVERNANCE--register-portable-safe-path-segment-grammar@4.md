---
cce_version: cce_1
cce_form: definition
subjects:
  - carrier-format
version: 4
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CA-R-888
    - CA-R-1054
---
# Register portable-safe path-segment grammar

A Project-owned filename or directory segment is portable-safe only when it uses ASCII letters, digits, underscores, hyphens, and dots; begins with an ASCII letter, digit, or underscore; and ends with an ASCII letter or digit. A registered root metadata or control entry MAY begin with one dot. A filename extension is separated by one dot and uses lowercase ASCII letters or digits.

Whitespace, control characters, path separators, quotes, shell metacharacters, empty segments, `.` and `..`, leading hyphens, trailing dots or spaces, and names whose stem case-insensitively equals `con`, `prn`, `aux`, `nul`, `com1` through `com9`, or `lpt1` through `lpt9` are invalid. Two sibling names MUST NOT become equal under ASCII case folding. A tool MUST pass a canonical name as path data; when a consumer requires a language identifier rather than a path, its additional identifier and reserved-word grammar MUST also be validated before use.
