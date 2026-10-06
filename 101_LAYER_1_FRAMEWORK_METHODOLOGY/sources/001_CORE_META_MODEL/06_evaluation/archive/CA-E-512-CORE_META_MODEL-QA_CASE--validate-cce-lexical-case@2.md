---
atom_id: CA-E-512
content_role: Evaluation
type: QA Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Governed Term Rendering"
  depends_on:
    - "Artifact/Revision"
    - "Atom/Claim"
    - "CCE"
    - "CCE Operator"
    - "CCE Operator Registry"
    - "Concern"
    - "General Term"
    - "Governed Term"
    - "Markdown Atom Carrier/Main Content/CCE Operator"
    - "Scope Unit/Name"
version: 2
updated_at: "2026-09-23 21:40:21 +0000"
relations:
  evaluation_for:
    - CA-D-280
    - CA-M-229
    - CA-M-234
---
# Summary

Validate CCE lexical case

## Claim

### Claim checked

**every** CCE Claim satisfies the lexical-case Method CA-M-229 **and** the Markdown operator representation specified by CA-D-280.

### Test case

- identify the tested CCE version, applicable CCE Operator Registry under CA-M-234, **and** exact Revisions of the checked authority. record the fixtures **and** their expected results.
- create valid fixtures with ordinary English words at sentence **and** list-item starts. include ordinary words that are **not** named Terms.
- create valid fixtures beginning with a Governed Term, a General Term, an exact Scope Unit Name, **and** an exact registered reference. preserve the case required for the token rather than changing it because of its sentence **or** list position.
- use **every** registered word-form CCE Operator **in** a valid context at sentence-initial **and** sentence-internal positions **where** the applicable grammar admits that position. include whole multiword forms such as **must not**, **not in**, **is not empty**, **starts with**, **and** **ends with**.
- use **every** registered symbolic CCE Operator **in** a valid context with the representation required by CA-D-280. include **`=`**, **`!=`**, **`<`**, **`<=`**, **`>`**, **`>=`**, **and** cardinality forms such as **`=1`** **and** **`>=1`**.
- derive invalid fixtures by applying **`=1`** of these mutations at a time:
  - capitalize an ordinary sentence-initial word.
  - capitalize an ordinary list-initial word.
  - capitalize a word-form CCE Operator.
  - remove an emphasis delimiter pair.
  - add an unmatched emphasis delimiter.
  - emphasize **only** part of a multiword CCE Operator.
  - omit bold rendering from a symbolic CCE Operator.
  - retain bold rendering but remove its inline-code rendering.
  - lowercase a Governed Term.
  - capitalize a General Term.
  - alter an exact Scope Unit Name.
  - alter an exact registered reference.

### Acceptance criteria

- **every** valid fixture retains **`=1`** precise interpretation **and** passes the lexical-case **and** representation checks.
- **every** invalid fixture fails the affected check. the result identifies the incorrect token occurrence, actual representation, expected token class **and** representation, **and** checked authority.
- fixture expectations come from the checked authority; this Evaluation **must not** introduce another operator spelling **or** formatting rule.

### Failure disposition

record a Concern naming the affected CCE Claim **and** incorrect token. checking **must not** rewrite the source Claim.
