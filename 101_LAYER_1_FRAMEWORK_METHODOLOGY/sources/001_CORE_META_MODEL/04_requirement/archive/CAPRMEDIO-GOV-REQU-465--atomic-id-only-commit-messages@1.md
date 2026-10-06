---
subject_scopes:
  - provenance
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-421--mandatory-git-and-commit-coverage
      - CAPRMEDIO-GOV-REQU-452--explicit-archive-commit-trailers
---

# Requirement — Use Atomic Artifact IDs as the complete commit message

Every governed Git commit uses exactly one line as its complete commit message:

```text
<implemented-artifact-ids> | <created-artifact-ids>
```

The left side lists the IDs of all Atomic Artifacts the commit implements. The
right side lists the IDs of all governed artifacts the commit creates.

Each side:

- contains only artifact IDs;
- separates multiple IDs with a comma followed by one space;
- contains no duplicate ID; and
- uses `none` when the list is empty.

The message contains no parentheses, labels, summary, description, body, or
trailers. File paths and free-form prose do not appear in it.

For example:

```text
CAPRMEDIO-GOV-REQU-421--mandatory-git-and-commit-coverage, CAPRMEDIO-GOV-REQU-452--explicit-archive-commit-trailers | CAPRMEDIO-GOV-REQU-465--atomic-id-only-commit-messages
```

Git retains the commit identity, author, time, parents, and changed files.
Artifact carriers retain their own relations and LLM session provenance.

## Primary claim

A governed commit message is only the implemented Atomic Artifact ID list, a
literal ` | ` separator, and the created governed-artifact ID list.

## Rationale

The diff already describes the file-level change. Restricting the message to
the two traceability sets makes commit history compact, deterministic, and
directly searchable by governed artifact ID.
