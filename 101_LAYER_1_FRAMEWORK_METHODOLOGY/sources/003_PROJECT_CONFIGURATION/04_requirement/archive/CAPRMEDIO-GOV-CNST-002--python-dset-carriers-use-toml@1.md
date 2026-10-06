---
subject_scopes:
  - carrier-format
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-REQU-398--all-toml-artifact-requirement
  - type: override_of
    targets:
      - CAPRMEDIO-GOV-METH-025--json-schema-boundary
---

# Constraint — Python-owned DSET carriers use TOML

All CAPRMEDIO-owned structured artifacts, settings, generated structured state,
portable bundle data, and schema definitions in this Python framework use
TOML. Python code reads and writes those carriers through the TOML boundary.

YAML is permitted only for externally prescribed host files whose consumers
require YAML, including GitHub Actions workflows and Codex skill metadata.
JSON is permitted only inside a genuinely JavaScript or TypeScript-owned work
area, or as transient command output where an external protocol requires it;
it is not a repository artifact format for this Python project.

This Constraint overrides the former project Decision that kept JSON Schema
files as a canonical exception. The semantic validation contracts remain, but
their project-owned carriers move to TOML.

## Primary claim

The Python-owned DSET framework uses TOML for every CAPRMEDIO-owned structured carrier and schema; YAML remains only where an external host contract mandates YAML, and JSON remains only in genuinely JavaScript or TypeScript-owned areas.

## Rationale

A Python and TOML implementation should not retain YAML and JSON compatibility surfaces that create duplicate parsers, schema formats, and migration exceptions.
