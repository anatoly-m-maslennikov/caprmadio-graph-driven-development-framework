---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Revision/Author/Frontmatter"
  depends_on:
    - "Actor"
version: 12
updated_at: "2026-09-24 14:16:19 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Serialize Explicit Atom Revision Author

## Claim

a Markdown Atom Carrier **must** serialize **`=1`** resolved Author as the top-level frontmatter Property `author`; apply the applicable Author default during authoring rather than leaving the accepted Revision dependent on an omitted Author.

- encode `author` as **=1** nonempty YAML string referencing the identified Author under the applicable Actor authority, **not** a list **or** a null value.
- resolve required Actor details from their canonical authority rather than adding an independently maintained Author record **to** this field. the Author need **not** be the Atom's owner.
