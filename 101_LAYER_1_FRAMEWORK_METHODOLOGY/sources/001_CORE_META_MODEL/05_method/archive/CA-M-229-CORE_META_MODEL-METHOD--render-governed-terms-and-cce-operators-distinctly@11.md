---
subjects:
  governs: "Governed Term Rendering"
  depends_on:
    - "CCE Operator"
    - "General Term"
    - "Governed Term"
    - "Scope Unit/Name"
    - "Author"
    - "Markdown Atom Carrier/Main Content/CCE Operator"
version: 11
updated_at: "2026-09-22 22:31:44 +0000"
relations:
  relates_to:
    - CA-D-280
    - CA-M-299
atom_id: "CA-M-229"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Method"
---
# Render Governed Terms and CCE Operators Distinctly

**to** render CAPRMEDIO content, the Author **must** apply the following lexical-case rules:

- start **every** Governed Term with a capital letter.
- start **every** General Term with a lowercase letter.
- preserve the lowercase spelling of **every** ordinary English word at the start of a sentence **or** list item **unless** an active rule requires an exact-case token.
- preserve the required case of canonical Terms, Scope Unit Names, **and** exact registered references, including at sentence **and** list-item starts.
- preserve the canonical spelling of **every** registered CCE Operator. use CA-D-280 for its representation **in** Markdown Atom Carrier Main Content.
