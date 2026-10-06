---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Governed Term Rendering"
  depends_on:
    - "CCE Operator"
    - "General Term"
    - "Governed Term"
    - "Scope Unit/Name"
    - "Author"
    - "Markdown Atom Carrier/Main Content/CCE Operator"
version: 9
updated_at: "2026-09-22 22:31:44 +0000"
relations:
  relates_to:
    - CA-D-280
    - CA-M-299
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Render Governed Terms and CCE Operators Distinctly

**to** render CAPRMEDIO content, the Author **must** apply the following lexical-case rules:

- start **every** Governed Term with a capital letter.
- start **every** General Term with a lowercase letter.
- preserve the lowercase spelling of **every** ordinary English word at the start of a sentence **or** list item **unless** an active rule requires an exact-case token.
- preserve the required case of canonical Terms, Scope Unit Names, **and** exact registered references, including at sentence **and** list-item starts.
- preserve the canonical spelling of **every** registered CCE Operator. use CA-D-280 for its representation **in** Markdown Atom Carrier Main Content.
