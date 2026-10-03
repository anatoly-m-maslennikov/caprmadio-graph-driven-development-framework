---
atom_id: CA-D-028
subject_scopes:
  - delivery
version: 3
updated_at: 2026-08-23 16:45:00 +0400
relations:
  delivery_for:
    - CA-R-1042
    - CA-R-1093
---
# Deliver CLOSE_ATOM intent Doer

The canonical source carrier for `CLOSE_ATOM` is `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/CLOSE_ATOM/close_atom.py`. It is installed only in the selected framework Tool release, delegates lifecycle effects to the canonical Atom lifecycle operation, and exposes mutation only through authorized project-local MCP delegation with a sealed Initiative action. Direct execution remains dry-run only.
