---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 4
updated_at: 2026-09-02 01:10:00 +0400
relations:
  method_for:
    - CA-R-865
  derived_from:
    - CA-A-058
---
# Create sealed CAPRMEDIO Atom carriers

## Applicable when

Use this Method when a caller prepares one new Atom or one frozen bulk set of two or more new Atoms. Actual creation is permitted only when an authorized project-local MCP delegation supplies a sealed Initiative action envelope.

## Procedure

1. Normalize the declared atomic or bulk request into one target directory and canonical filename per carrier, complete frontmatter, and a Markdown body.
2. Require every target to be inside a configured control-root Content-role location; validate placement, filename grammar, required metadata, direct relations, and initial revision metadata before filesystem mutation.
3. Prove that every target path, filename, and stable Atom ID is absent from both current authority and the entire requested set.
4. Freeze the target map with expected empty destinations and publish a mutation-free dry-run containing every derived carrier and validation result.
5. On explicit authorized `--apply`, recheck the frozen absence conditions, stage all new carriers, and publish the complete atomic or bulk set as one transaction.
6. If staging, publication, or post-write validation fails, remove unpublished staging artifacts and restore the pre-action state.

## Outcome

The requested set is either fully absent or fully present as valid first revisions with no partial creation.

## Failure or stop

Remain in dry-run mode unless delegated apply authority and the sealed Initiative envelope are explicit. Stop on an invalid carrier, collision, changed absence precondition, changed target set, or failed atomic publication.
