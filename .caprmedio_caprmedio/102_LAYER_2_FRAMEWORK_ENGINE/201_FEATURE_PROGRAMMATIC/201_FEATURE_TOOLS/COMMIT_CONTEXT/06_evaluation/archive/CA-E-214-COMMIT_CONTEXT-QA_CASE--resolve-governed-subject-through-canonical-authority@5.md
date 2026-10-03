---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-803
    - CA-R-804

---
# Resolve a governed subject through canonical Artifact authority

## Claim checked

Trigger observation and commit-context gathering do not substitute filename or path-shape heuristics for governed Artifact classification.

## Test case

Create one registered active Markdown Atom and, in the same fixture, a narrative Markdown document, a narrative Projection, an unknown Markdown file, and a non-Markdown carrier whose names deliberately contain Atom-like prefixes or `--`. Observe one content change to the real Atom and gather its context.

## Acceptance criteria

The adapter emits one unclassified path-candidate trigger. `COMMIT_CONTEXT` resolves exactly the registered Atom through current Artifact routes, Type authority, lifecycle placement, Project Configuration, and the Project Scope Unit Graph; it does not admit any lookalike carrier into the Atom graph or sealed subject. Repeating the run returns the same classification and identities without mutation.

## Failure disposition

Reject the delivery if filename punctuation or extension alone admits or excludes a subject, a lookalike becomes an Atom, the registered Atom is missed, or classification changes between identical runs.
