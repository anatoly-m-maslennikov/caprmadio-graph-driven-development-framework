---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Search Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_SEARCH"
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 1
updated_at: "2026-09-17 04:11:05 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Search CAPRMEDIO Atom carriers

Search Atom Carriers **means** the reusable read-only Action that returns the complete matching set of Atom Carriers for **=1** declared search frontier **and** requested output view under CA-R-863. incomplete membership **or** missing attribution is **not** a successful result.

## Applicable conditions

an Operator **or** another Tool requests deterministic Atom discovery within a declared frontier.

## Action

1. resolve the configured CAPRMEDIO control root, **=1** declared subtree boundary, the requested output view, **and** supplied exact-selector, lifecycle, path, filename, frontmatter, **or** body-text filters.
2. reject an invalid root, selector, filter, lifecycle, **or** output-view request **before** traversing the frontier.
3. enumerate **only** Markdown candidates inside that frontier. classify Atom eligibility from current locations **and** filenames; exclude runtime state, Projections, **and** non-Atom files.
4. apply the exact selector **and** **every** supplied filter conjunctively. retain a separate diagnostic for **every** malformed **or** unreadable candidate.
5. read **only** the filename, frontmatter, **and** body fields needed for the requested metadata-only, content-only, **or** combined view.
6. return the empty, singular, **or** bulk result **in** stable repository-relative path order, with **=1** attributable result record per matching Atom.
7. perform no write, rename, move, lifecycle transition, repair, **or** Projection rebuild.

## Outcome and stops

the result identifies **every** **and** **only** matching Atom Carrier within the declared frontier. stop **without** mutation **when** the root **or** request grammar is invalid; distinguish malformed candidates from valid non-matches **and** never infer a match from unreadable content.
