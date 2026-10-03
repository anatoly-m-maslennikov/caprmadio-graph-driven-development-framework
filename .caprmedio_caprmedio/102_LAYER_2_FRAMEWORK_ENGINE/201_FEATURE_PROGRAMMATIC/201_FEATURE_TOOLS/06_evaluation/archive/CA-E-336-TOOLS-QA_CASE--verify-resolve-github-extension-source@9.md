---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "extension-packaging"
  depends_on: []
version: 9
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-218
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify resolve GitHub Extension source

## Claim checked

CA-M-218 resolves the declared GitHub repository **and** package-root boundary for one Extension **without** choosing an installed state.

## Applicable when

apply whenever GitHub Extension source-boundary resolution changes.

## Test case

resolve one Extension whose package root is a declared repository subdirectory, **then** resolve another whose package root is the complete repository. repeat with an undeclared subdirectory.

## Acceptance criteria

each valid case reports the declared GitHub repository **and** its exact complete-repository **or** declared-directory package root. the undeclared-subdirectory case produces an explicit failure **and** no alternative source boundary.

## Failure disposition

reject the realization **and** preserve source declarations, resolved boundaries, undeclared-subdirectory finding, **and** proof that installed Extension state was unchanged.
