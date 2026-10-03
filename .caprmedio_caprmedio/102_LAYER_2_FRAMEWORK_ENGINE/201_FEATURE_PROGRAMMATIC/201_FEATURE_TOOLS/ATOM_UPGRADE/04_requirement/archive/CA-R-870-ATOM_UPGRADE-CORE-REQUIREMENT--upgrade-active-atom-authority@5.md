---
subjects:
  declared:
    continuant:
      - artifact-operations
version: 5
updated_at: 2026-08-23 16:16:20 +0400
---
# Upgrade active Atom authority

The `ATOM_UPGRADE` Tool is the canonical Doer for upgrading active CAPRMEDIO Markdown Atoms to an explicit operator-supplied enabled target Tier of `core` or `standard` that is higher than the source Tier. Upgrade is neither archive nor promotion: it preserves the stable Atom ID and may keep the current Scope Unit or move the Atom only to an explicitly named ancestor Scope Unit. The Tool must derive the target authority location and filename scope segment when the Scope Unit changes, advance revision metadata, and reject missing, disabled, non-higher, or other invalid target Tiers, non-active Atoms, non-ancestor Scope Units, identity or destination collisions, and partial operations. An atomic action upgrades exactly one Atom; a bulk action freezes two or more Atom targets with their expected revisions or digests and is all-or-nothing. It must default to a mutation-free dry run and accept `--apply` only through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Check

Automated tests must prove singular and bulk same-Scope tier upgrades, ancestor-Scope upgrades, explicit target-tier enforcement, stable-ID preservation, derived filename and location, revision advancement, mutation-free dry run, MCP-gated apply, invalid target rejection, and restoration of every source and destination after an apply failure.
