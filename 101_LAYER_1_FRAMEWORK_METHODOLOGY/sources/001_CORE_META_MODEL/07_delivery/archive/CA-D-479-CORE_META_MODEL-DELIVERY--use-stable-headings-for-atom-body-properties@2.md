---
subjects:
  governs: "Markdown Atom Carrier/Main Content"
  depends_on:
    - "Atom/Summary"
    - "Atom/Claim"
    - "Property"
    - "Markdown Atom Carrier/Structure"
version: 2
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"relates_to": ["CA-D-356", "CA-D-478"]}
---
# Summary

Use stable headings for Atom body Properties

## Claim

a Markdown Atom's Main Content **must** use stable Property sections:

- start with **`=1`** literal `# Summary` heading; place the Summary value below it, **not** inside the heading.
- follow with **`=1`** literal `## Claim` heading; place the complete Claim below it.
- carry another body Property under its exact registered level-two heading, such as `## Definition of Done` **or** `## Details`, **only** **when** applicable. its Delivery authority specifies its cardinality **and** position.
- a body Property's value ends at the next heading of the same **or** a higher level, **or** at end of Main Content. supporting headings inside that value use lower levels.
- heading markers inside fenced code examples are content, **not** Property boundaries.
- reject missing required, duplicate, renamed, **or** ambiguously nested Property headings; do **not** infer the intended Property from prose, synonyms, **or** heading position alone.
