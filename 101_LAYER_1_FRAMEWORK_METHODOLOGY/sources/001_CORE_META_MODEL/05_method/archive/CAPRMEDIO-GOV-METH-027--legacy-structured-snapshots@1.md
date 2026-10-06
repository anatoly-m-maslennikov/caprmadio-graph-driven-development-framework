---
artifact_subtype: implementation_decision
subject_scopes:
  - settings
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-REQU-395--verbose-project-settings
  - type: resolution_of
    targets:
      - CAPRMEDIO-SPEC-TOOLS-CONC-058--immutable-toml-migration
---

# Decision — Retain exact legacy structured snapshots

The artifact-classification registry owns one exact, no-wildcard
`legacy_structured` entry for every retained YAML snapshot. Each entry records
the old path, whole-file SHA-256, TOML `current_owner`, artifact type and
optional subtype, and the exact historical carrier IDs plus retention reason.

Readers use TOML only and never fall back to a registered snapshot. Validation
fails when a snapshot changes, its current owner is missing, a YAML/TOML pair
is unregistered, an entry is duplicated, a mutable carrier still links to the
old path, or new immutable evidence links to an unregistered legacy carrier.

Migration creates the TOML owner and registration transactionally, updates only
mutable references, preserves registered source bytes, and is a no-op on a
second run. Selector fragment seals and whole-carrier snapshot digests remain
separate checks with separate purposes.

This emitted Decision atom is immutable. Later correction requires a successor
and append-only lifecycle evidence.

## Primary claim

A YAML carrier required by immutable historical links or selector-sealed authority remains byte-stable only as an exactly registered historical snapshot while its TOML sibling is the sole current owner.

## Rationale

Physical byte-stable snapshots preserve GitHub links and historical identity without making pointer stubs, symlinks, virtual resolution, or YAML fallback part of the current authority model.
