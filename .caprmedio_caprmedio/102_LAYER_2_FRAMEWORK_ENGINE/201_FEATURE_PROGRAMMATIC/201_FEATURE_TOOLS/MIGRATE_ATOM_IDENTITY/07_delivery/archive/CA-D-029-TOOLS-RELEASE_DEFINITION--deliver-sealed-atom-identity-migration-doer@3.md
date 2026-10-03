---
subject_scopes:
  - delivery
version: 3
updated_at: 2026-08-23 16:45:00 +0400
relations:
  delivery_for:
    - CA-R-1048
    - CA-R-1093
---
# Deliver sealed Atom identity migration Doer

The canonical source carrier is `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/MIGRATE_ATOM_IDENTITY/migrate_atom_identity.py`; its private workers are delivered in the same Tool directory. The selected `.caprmedio_install` release exposes the stable launcher. It exposes direct inspection and dry run, but applies a sealed migration only through authorized project-local MCP delegation and returns a durable `COMMIT_TRIGGER` intake acknowledgement without appending the Journal or mutating Git.
