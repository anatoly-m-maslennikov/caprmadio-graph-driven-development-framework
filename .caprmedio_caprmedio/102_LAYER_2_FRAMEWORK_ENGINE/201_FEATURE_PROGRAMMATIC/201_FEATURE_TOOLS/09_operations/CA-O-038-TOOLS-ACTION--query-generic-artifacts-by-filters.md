---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Query Generic Artifacts"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "Relation"
version: 2
updated_at: "2026-09-17 03:31:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Query generic Artifacts by filters

Query Generic Artifacts **means** the reusable Action that produces one complete body-free generic Artifact query result against the selected source frontier under CA-R-1135. its modeled boundary is the complete requested result; partial comparison, incomplete attribution, **or** an unreported unresolved input is **not** an independently successful outcome.

## Applicable when

use this Action **when** framework internals need a body-free ordered set of generic Artifact identities **and** paths selected by composable filters.

## Action

1. normalize the requested structural scope, layer, Tier, Feature, Content role, subject scope, lifecycle, **and** typed-relation filters.
2. evaluate their declared composition over generic Artifact metadata **and** carrier-derived identity **without** loading **any** Artifact body.
3. include **every** **and** **only** matching canonical Artifact ID **and** carrier path, deduplicate them, **and** order them by the registered stable ordering rule.
4. attribute the result **to** the selected source frontier **and** preserve explicit diagnostics for unsupported filters **or** malformed metadata.
5. return the helper result **without** applying CAPRMEDIO Atom eligibility, content-query, lifecycle, subtree, **or** output-view semantics.

## Outcome

one deterministic generic Artifact query result **contains** **only** matching canonical IDs **and** carrier paths **in** stable order.

## Failure or stop

return no partial accepted result on an unsupported filter, ambiguous selector, **or** malformed required metadata; never load bodies **or** mutate carriers.
