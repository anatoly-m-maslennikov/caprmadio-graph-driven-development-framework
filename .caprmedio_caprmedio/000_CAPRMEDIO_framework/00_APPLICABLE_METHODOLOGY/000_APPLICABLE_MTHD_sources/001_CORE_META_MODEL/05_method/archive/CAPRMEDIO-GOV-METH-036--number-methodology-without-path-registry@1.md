---
artifact_subtype: implementation_decision
subject_scopes:
  - layout
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-METH-034--number-installed-methodology-descendants
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-METH-035--discover-project-artifacts-by-identity
---

# Decision — Number methodology without a path registry

The installed methodology keeps the accepted `00_project` through `05_ops`
layer roots. Every descendant entry uses a zero-padded numeric prefix unique
among its siblings. The materializer applies the governed numbering algorithm
directly and does not publish a source-path-to-installed-path registry.

Skills ignore the numbering when resolving an identity. They search the
project's `.caprmedio` tree and require exactly one matching identity or unique
carrier name.

## Rationale

Numbering improves local reading order, while identity-based lookup prevents
that presentation choice from becoming a second authority or a persistent
coupling in settings.

## Primary claim

Every committed file and directory below .caprmedio/000_caprmedio_methodology uses a stable numeric prefix within its parent, and deterministic materialization derives those names without a durable source-to-carrier path registry.
