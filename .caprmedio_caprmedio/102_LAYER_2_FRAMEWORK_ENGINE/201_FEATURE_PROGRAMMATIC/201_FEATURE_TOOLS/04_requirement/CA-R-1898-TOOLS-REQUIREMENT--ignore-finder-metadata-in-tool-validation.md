---
atom_id: CA-R-1898
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-07 22:25:26 +0000"
subjects:
  governs: "Tool/Validation/Finder metadata"
  depends_on: [Tool, Carrier, Framework Package, Runtime, Skill, Projection, Journal]
relations:
  relates_to: [CA-R-1897]
---
# Summary

Ignore Finder metadata in Tool validation

## Scope

Tool selection, persistent inventories, digests, package and Projection checks, and runtime control-directory checks at any depth.

## Claim

Tool validation **must** ignore files named `.DS_Store` so their presence, absence **or** contents do **not** change validation results.

## Details

Finder metadata is not an admitted source, package member, generated output, Skill resource, Journal event or runtime message. Exclude it before reading file contents or comparing persistent inventories; neither deleting it nor preventing Finder from creating it is a prerequisite.

This exclusion is for the exact basename `.DS_Store`. All other files retain their existing admission, ownership, missing-file, digest, mode and safety checks. Historical evidence remains unchanged; an earlier metadata-related failure retains its actual recorded outcome.
