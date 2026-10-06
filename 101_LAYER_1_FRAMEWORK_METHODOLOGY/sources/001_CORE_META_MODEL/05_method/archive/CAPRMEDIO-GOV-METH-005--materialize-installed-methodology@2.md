---
subject_scopes:
  - methodology
tier: core
version: 2
updated_at: 2026-08-19 16:45:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-METH-031--portable-reference-carriers
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Materialize installed methodology

The reusable methodology is authored in the repository-root source and copied
unidirectionally into `.caprmedio/000_caprmedio_framework/` only by an explicit
operator synchronization command.

Installed methodology carriers contain the actual governed content. They are
not symbolic links or repository-relative reference carriers. Skills resolve
all methodology, settings, artifacts, and Projections only inside the
selected project's `.caprmedio/` control root.

Synchronization computes the destination layout deterministically, stages and
validates the complete result, refuses unresolved collisions, and replaces only
the installed methodology snapshot. Ordinary source edits never trigger an
implicit mirror.

## Rationale

Materialization keeps project governance self-contained for every supported
host and avoids symlink behavior, reference traversal, or dependence on a
repository-specific source layout at skill runtime.
