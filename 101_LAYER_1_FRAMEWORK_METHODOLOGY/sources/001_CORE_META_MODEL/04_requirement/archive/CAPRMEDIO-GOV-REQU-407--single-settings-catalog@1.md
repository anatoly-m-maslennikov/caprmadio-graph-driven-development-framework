---
subject_scopes:
  - settings
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---

# Requirement — Keep one settings and catalog carrier

`caprmedio_settings.toml` absorbs the active content of `artifact-types.toml`,
`artifacts.toml`, the governance registry, project/version configuration, and
other non-artifact registries. It does not absorb atomic claims or evergreen
specification prose.

The obsolete `legacy_evidence_paths` compatibility list is not carried into
the active catalog. Historical classification inputs remain in the explicit
root legacy archive when provenance requires them.

## Rationale

One verbose settings carrier makes selected behavior and structural ownership
reviewable without reconciling several mutable aggregate registries.

## Primary claim

The canonical caprmedio_settings.toml owns project settings, structural roots, artifact classification, artifact areas, profiles, and other non-artifact registries without competing aggregate settings files.
