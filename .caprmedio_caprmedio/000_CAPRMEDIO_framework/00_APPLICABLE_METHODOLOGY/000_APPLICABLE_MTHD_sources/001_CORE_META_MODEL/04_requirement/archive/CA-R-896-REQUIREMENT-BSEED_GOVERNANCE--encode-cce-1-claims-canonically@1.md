---
subject_scopes:
  - language
relations:
  child_of:
    - CA-R-892
    - CA-R-894
    - CA-R-895
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
version: 1
updated_at: 2026-08-22 02:53:47
---
# Encode CCE 1 Claims canonically

Every `cce_1` Markdown Atom must declare `cce_version: cce_1` and one registered `cce_form` identifier in frontmatter. After its derived H1, the Atom must contain exactly one `## CCE Claim` section whose first nonblank content is the canonical serialization of the Atom's CCE Claim. An active Atom and a draft Atom use the same CCE encoding; lifecycle and stable identity remain carrier facts and are not repeated in the Claim unless they change its meaning.

A simple statement form serializes on one line. The `method` and `evaluation` forms serialize their required headers exactly as registered and use consecutive decimal list markers beginning at `1.`. Every list item contains one complete registered action or condition clause and ends with one period. No other Markdown, inline code, link, formula, table, heading, note, comment, or explanatory sentence may occur inside `## CCE Claim`.

Uppercase function tokens use their registered spelling. Canonical terms and predicate phrases use their exact vocabulary spelling and capitalization. Serialization uses UTF-8, one ASCII space between tokens, no tabs, no trailing whitespace, one blank line around the CCE section boundary, and one final line feed. Each sentence ends with one period. A condition serializes after its governed clause in the order `WHEN`, `WHILE`, `WITHIN`.

The canonical renderer must reject rather than normalize an unknown token, undeclared alias, bare plural, unsupported punctuation, invalid list, invalid function-token case, mixed ungrouped Boolean operator, unresolved reference, missing required filling, extra filling, role-incompatible form, or noncanonical ordering. Parsing the canonical rendering must reproduce the same typed representation byte-for-byte under canonical structured serialization.
