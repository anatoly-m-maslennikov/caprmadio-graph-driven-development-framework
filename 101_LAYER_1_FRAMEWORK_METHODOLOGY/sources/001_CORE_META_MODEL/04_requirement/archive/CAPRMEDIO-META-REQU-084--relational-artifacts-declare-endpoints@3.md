---
subject_scopes:
  - artifact-model
version: 3
updated_at: 2026-08-22 00:53:40
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-871-REQUIREMENT-BSEED_METAMODEL--distinguish-shared-authority-edges-and-relational-atoms
---
# Distinguish relational Atom meaning from graph connectivity

## Primary claim

Every Atom has one semantic shape: `standalone` or `relational`. Every relation in the governed graph is a typed edge declared under the relation-owning Atom's `relations` frontmatter. An Atom has relational semantic shape only when the relationship itself is its independently governed meaning and therefore needs its own identity, revision, and lifecycle.

An ordinary Atom may participate in any number of graph relations without becoming a relational Atom. A relational Atom remains an ordinary Artifact node and declares its exact endpoints through the same frontmatter relation mechanism.
