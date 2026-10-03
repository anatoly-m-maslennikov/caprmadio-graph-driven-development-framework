---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "project-graph-state"
  depends_on:
    - "Project Structure"
    - "Project Settings"
    - "Framework Instance Settings"
    - "Projection"
version: 8
updated_at: "2026-09-17 21:51:44 +0000"
relations:
  evaluation_for:
    - CA-M-149
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Rebuild one project graph state from configuration

## Claim checked

the graph-state Tool derives one current non-authoritative Projection from the inputs admitted by CA-M-149: authoritative Project Structure, separate Settings authority, **and** the selected Atom, directory-observation **and** Journal evidence frontier.

## Test case

rebuild graph state twice from unchanged source Revisions **and** observations. include accepted declarations whose folder materialization **or** Goal coverage is missing, **and** observed directories that do **not** match an accepted declaration.

## Acceptance criteria

- both Projections agree semantically **and** identify their selected sources.
- accepted Scope Unit declarations **and** concrete bindings come **only** from Project Structure. Project Settings **and** Framework Instance Settings retain their separate selected-value authority.
- declarations, Atom Claims, directory observations **and** Journal evidence remain distinct. missing coverage **and** mismatches stay visible **without** creating **or** rewriting accepted declarations.
- no direct output edit becomes authority, **and** **all** source Carriers remain unchanged.
- missing, invalid **or** incompletely read required authority is reported as incomplete coverage, **not** a complete accepted Project Structure.

## Failure disposition

reject the Projection as stale, nondeterministic, source-altering **or** authority-creating **when** **any** corresponding condition fails.
