---
subjects:
  governs:
    continuant:
      - language
    occurrent:
      - evaluation
  depends_on:
    continuant:
      - CCE
cce_version: cce_1
cce_form: evaluation
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations:
  evaluation_for:
    - CA-M-113
---
# Validate CCE lexical case

## Claim checked

**every** CCE Claim preserves lowercase ordinary words at sentence **and** list-item starts, uses the registered lowercase spelling of **every** CCE Operator, **and** renders **every** CCE Operator occurrence with Markdown strong emphasis.

## Test case

create valid fixtures beginning with an ordinary word, a CAPRMEDIO Term, **and** an exact registered reference. use **every** registered CCE Operator at sentence-initial **and** sentence-internal positions with forms such as `**means**`, `**if**`, `**then**`, `**must**`, **and** `**every**`. then capitalize one ordinary sentence-initial word, capitalize one CCE Operator, remove one delimiter pair, add an extra emphasis delimiter, emphasize only part of one multiword CCE Operator, lowercase one exact-case Term, **and** change one exact registered reference.

## Acceptance criteria

**every** valid fixture parses to one precise interpretation. **every** invalid fixture fails with the incorrect lexical token, emphasis boundary, **and** expected token class identified.

## Failure disposition

record a Concern naming the affected CCE Claim **and** incorrect token.
