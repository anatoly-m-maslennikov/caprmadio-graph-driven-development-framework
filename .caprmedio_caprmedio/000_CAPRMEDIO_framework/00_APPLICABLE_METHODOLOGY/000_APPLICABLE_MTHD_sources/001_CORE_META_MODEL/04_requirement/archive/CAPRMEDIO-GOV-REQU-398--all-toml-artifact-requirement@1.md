---
subject_scopes:
  - carrier-format
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-395--verbose-project-settings
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-METH-028--semantic-immutability-and-toml-carriers
  - type: resolution_of
    targets:
      - CAPRMEDIO-SPEC-TOOLS-CONC-061--yaml-artifact-gap
---

# Requirement — Use TOML for every DSET artifact carrier

The canonical root settings carrier remains `caprmedio_settings.toml` with the same
documented settings, defaults, accepted values, and settings-versus-manifest-
versus-governance ownership boundary defined by its predecessor.

All CAPRMEDIO-owned structured artifact files and DSET Markdown frontmatter use
TOML. This includes emitted atoms, promoted evidence, legacy Decision carriers,
and historical structured editions after an authorized carrier transition.
No CAPRMEDIO-owned `.yaml` or `.yml` artifact and no DSET Markdown YAML frontmatter
remains in the current repository.

Historical standalone editions use adjacent `<stem>.legacy.toml` envelopes
when `<stem>.toml` already owns current truth. Current readers never fall back
to those envelopes. Every migrated carrier is registered in the append-only
transition ledger with semantic-equivalence proof and a Git source-return
address.

Standards-compliant JSON Schema, GitHub Actions, host skill metadata, ecosystem
manifests and lockfiles, wire/CLI formats, and machine-local runtime journals
retain externally prescribed formats. They are not alternative DSET artifact
encodings.

This Requirement atom is immutable. Later correction requires a successor and
append-only lifecycle event.

## Primary claim

DSET exposes operator-selectable behavior through one verbose caprmedio_settings.toml and uses TOML for every CAPRMEDIO-owned structured artifact and Markdown frontmatter, including historical carriers migrated through governed transitions.

## Rationale

One readable current encoding removes the historical YAML exception while the transition ledger preserves provenance and return paths separately from current authority.
