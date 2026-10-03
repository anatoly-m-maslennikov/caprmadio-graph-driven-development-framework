---
subjects:
  governs: "Atom/Property/Carrier"
  depends_on:
    - "Atom/Property"
    - "Markdown Atom Carrier"
    - "Atom/Frontmatter"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Relation"
version: 3
updated_at: "2026-09-24 13:59:55 +0000"
relations: {"delivery_for": ["CA-R-1598"], "relates_to": ["CA-D-479", "CA-D-268", "CA-R-1470"]}
---
# Summary

Store every Atom Property in one internal location

## Claim

**every** applicable Atom Property **must** have **`=1`** canonical internal location assigned by its Delivery authority:

- use YAML Frontmatter **unless** that Property is assigned **to** a named Main Content section.
- use the named section as the sole value source **when** Main Content carries the Property; do **not** maintain the same Property again **in** frontmatter.
- names, filename tokens, **and** placement are representations checked against the internal value under CA-D-480, **not** alternative authority.
- Atom-to-Atom Relations follow their registered owning direction under CA-D-268; do **not** copy inverse **or** transitive Relations **to** make an Atom self-sufficient.
- the retired top-level fields `cce_version`, `cce_form`, **and** `llm_session_ids` are **not** admitted Atom Properties **and** **must not** be serialized **in** an Atom Carrier. their absence is conforming; their presence is a retired-field finding, **not** a reason **to** select legacy authority. this rule does **not** remove session provenance from its separately governed Journal Carrier.
