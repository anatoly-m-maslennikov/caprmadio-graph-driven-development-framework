---
subject_scopes:
  - delivery
version: 2
updated_at: 2026-08-23 13:21:41
relations:
  delivery_for:
    - CA-R-1048
---
# Deliver sealed Atom identity migration Doer

The canonical source carrier is `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/MIGRATE_ATOM_IDENTITY/migrate_atom_identity.py`; its private workers are delivered in the same Tool directory. The selected `.caprmedio_install` Tool release exposes it through the stable `migrate-atom-identity` launcher. Its describe response identifies `atom_id` and `tier` as removal-only legacy frontmatter fields. Mutable execution state is not required and is not written by this Tool.
