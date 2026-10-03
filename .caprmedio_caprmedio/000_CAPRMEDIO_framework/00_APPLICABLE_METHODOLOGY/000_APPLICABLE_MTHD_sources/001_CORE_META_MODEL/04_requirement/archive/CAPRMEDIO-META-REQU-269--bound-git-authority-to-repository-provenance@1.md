---
subject_scope: lifecycle-traceability
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-245--git-as-canonical-history-engine
  child_of:
    - CAPRMEDIO-REQU-056--require-falsifiable-claims-and-stop-conditions
---
# Requirement — Bound Git authority to repository provenance

Every CAPRMEDIO-governed project uses Git as the required history and provenance
engine for persisted repository state. The accepted Git graph is canonical for
the repository snapshots, changes, integrations, authorship, and release
boundaries that it records.

Git provenance does not by itself own semantic authority, Evaluation, Ops
Evidence, or graph-independent relationships between exact artifact revisions
and their realizations. Governed Journals preserve those relationships when a
normal delivery workflow squashes, rebases, cherry-picks, or migrates Git
history. A generated index remains derived and replaceable.

Rewriting a Git graph is permitted only when required governed relationships
and released-state identities remain replayable through stable artifact and
target revisions plus their Journals. A rewritten commit identifier cannot be
the sole identity of a semantic dependency.

Git is the explicit version-control dependency of the CAPRMEDIO framework, not a
hidden implementation choice. GOV defines concrete commit, integration,
archive, and Journal-binding conventions.

## Primary claim

Git is mandatory and canonical for persisted repository provenance, while
graph-independent semantic lineage is preserved by governed Journals rather
than by permanent reachability of every intermediate commit.
