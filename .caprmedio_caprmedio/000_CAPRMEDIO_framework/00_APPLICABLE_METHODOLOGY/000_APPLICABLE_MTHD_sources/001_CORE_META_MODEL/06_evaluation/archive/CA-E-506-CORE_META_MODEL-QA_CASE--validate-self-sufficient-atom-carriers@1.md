---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Carrier/Validation"
  depends_on:
    - "Atom"
    - "Atom/Property"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Revision/Status"
    - "Relation"
    - "Markdown Atom Carrier"
version: 1
updated_at: "2026-09-22 23:02:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1598", "CA-R-1599", "CA-D-478", "CA-D-479", "CA-D-480", "CA-D-481", "CA-D-482", "CA-D-483", "CA-D-485", "CA-D-460", "CA-D-470"]}
---
# Summary

Validate self-sufficient Atom Carriers

## Claim

the Evaluation **must** accept **only** Atom Carriers that preserve self-sufficiency, one internal value source, **and** consistent outward representations.

#### Test case

- construct a valid Atom with its required Properties inside its Markdown Carrier, using the applicable registered fields **and** body sections. include a required defaulted value, an optional absent Property, **and** an inapplicable Property that is correctly absent.
- extract Summary **and** Claim without reading the filename **or** containing directories. include fenced code containing example headings; those examples **must not** create Property boundaries.
- compare the carried values against filename **and** placement representations using the applicable encoding. include a Summary whose slug differs from its readable text.
- include a Current-scope target explicitly equal **to** its owner; it remains Current-scope. include a permitted different target **and** an Operator-owned Project Goal.
- include a Plan with its mandatory Markdown file **and** DoD, with **and** **without** a matching directory; include a child-owned decomposition edge with its inverse derived.
- include an unselected inherited confidence setting **and** a selected override currently equal **to** inheritance; change the upstream setting **and** check that **only** the inherited selection follows it.
- create invalid fixtures by removing a required internal value, supplying that value **only** through an address, duplicating it **in** frontmatter **and** body, repeating a heading **or** YAML key, renaming a required heading, introducing an ambiguous boundary, conflicting with the address, omitting a Plan's file **or** DoD, **or** storing an inverse Atom Relation independently.

#### Acceptance criteria

- **every** valid fixture yields the expected Property values **and** Relations.
- **every** invalid fixture fails with the exact Property, location, Relation, **or** address conflict identified.
- address **and** inverse checks **must not** silently rewrite the source **or** treat derived representations as separate authority.
