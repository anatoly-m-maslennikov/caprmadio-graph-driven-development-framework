---
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
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-388--artifact-type-name-policy
---

# Requirement — Select artifact naming in canonical settings

New artifact IDs and filenames include the primary artifact-type token by
default. An optional direct artifact subtype remains metadata unless
`artifacts.subtype_in_names = true` is selected in root
`caprmedio_settings.toml`.

The setting affects only newly emitted carriers. It never renames an immutable
atom or another already stable artifact identity, and it is independent from
every other optional capability.

## Rationale

This successor preserves the accepted naming behavior while correcting the
retired settings filename and key in the active authority graph.

This emitted Requirement atom is immutable. Later correction requires a
successor and append-only lifecycle evidence.

## Primary claim

New artifact names use the primary artifact type by default and the optional subtype only when artifacts.subtype_in_names is enabled in caprmedio_settings.toml.

## Rationale

The behavior is unchanged, but its active source must name the canonical settings carrier and key without relying on a contradictory compiled rewrite.
