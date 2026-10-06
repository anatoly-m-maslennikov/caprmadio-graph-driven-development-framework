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
      - CAPRMEDIO-GOV-REQU-398--all-toml-artifact-requirement
---

# Requirement — Use YAML frontmatter for Markdown

CAPRMEDIO-owned Markdown artifacts use YAML frontmatter. Standalone CAPRMEDIO-owned
structured artifacts use TOML unless an external contract requires another
format.

Markdown frontmatter begins and ends with `---`. TOML files remain ordinary
valid TOML files and do not contain Markdown frontmatter. YAML is not a
standalone DSET artifact format.

Externally prescribed formats—including GitHub Actions workflows, ecosystem
manifests, wire formats, and standards-compliant schemas—retain their required
encoding.

## Rationale

YAML frontmatter is the established Markdown metadata convention and works with
GitHub's Markdown and GitHub Pages tooling. TOML remains the more readable
format for standalone DSET settings and structured records.
