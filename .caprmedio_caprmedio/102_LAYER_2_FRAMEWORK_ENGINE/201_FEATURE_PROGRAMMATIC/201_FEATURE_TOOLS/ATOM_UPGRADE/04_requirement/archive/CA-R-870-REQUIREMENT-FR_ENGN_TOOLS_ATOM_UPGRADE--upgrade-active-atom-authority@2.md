---
subject_scopes:
  - artifact-operations
tier: core
version: 2
updated_at: 2026-08-22 03:01:35
relations:
  child_of:
    - CA-R-004
    - CA-R-861
---
# Upgrade active Atom authority

The `ATOM_UPGRADE` Tool must upgrade one or many active CAPRMEDIO Markdown Atoms to an explicit operator-supplied higher tier. An upgrade may keep the current Scope Unit or move the Atom to an explicitly named ancestor Scope Unit. The Tool must preserve the stable Atom ID, derive the target authority location and filename scope segment when the Scope Unit changes, advance revision metadata, and reject missing or non-higher tiers, non-active Atoms, non-ancestor Scope Units, identity or destination collisions, and partial bulk operations. It must default to a mutation-free dry run and apply all validated upgrades as one recoverable operation only when explicitly requested.

## Check

Automated tests must prove singular and bulk same-Scope tier upgrades, ancestor-Scope upgrades, explicit target-tier enforcement, stable-ID preservation, derived filename and location, revision advancement, mutation-free dry run, invalid target rejection, and restoration of every source and destination after an apply failure.
