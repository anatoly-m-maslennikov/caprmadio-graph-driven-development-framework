---
subject_scope: lifecycle-traceability
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-260--one-independently-replaceable-claim-per-atom
---

# Requirement — Model governed change as revision-bound parent and child transactions

Every governed change is a directed provenance transaction:

```text
exact parent revisions → new and updated children
```

A parent is an exact committed revision of an Atom whose claim the
transaction consumes. A child is a governed artifact or native project carrier
produced or revised by the transaction.

The transaction distinguishes:

- children created for the first time; and
- existing children revised by the transaction.

A same-ID Atom change is therefore a new child revision of its
earlier committed revision. Existing dependents remain bound to the parent
revision their own transaction consumed; later dependents may consume a later
revision that preserves the Atom's primary identity.

All children in one transaction belong to exactly one `scope_path`. Parents may
come from multiple scopes when one bounded child scope integrates their
authority.

Parent revisions must pre-exist the transaction. A transaction cannot depend
on a revision created by that same transaction. Creating or refining an Atom
and producing children that consume the resulting revision therefore require
separate ordered transactions.

Every parent-to-child edge must be replayable from durable repository history.
Once a parent revision has a dependent child, the history that identifies that
revision must remain reachable and unchanged.

META defines these transaction semantics without prescribing a Git message
syntax, delimiters, path representation, or resolver implementation. GOV owns
the concrete carrier contract.

## Primary claim

Each governed change consumes exact Atom revisions and produces new
or updated children in one scope through a replayable directed transaction.

## Rationale

Revision-bound edges preserve the precise authority each child consumed while
allowing conservative evolution under a stable Atom ID. The
one-child-scope boundary keeps commits reviewable without preventing
cross-scope inputs.
