---
subjects:
  governs: "New Archived Revision Markdown Carrier Binding"
  depends_on:
    - "Artifact/Revision/Status"
    - "Artifact/Revision/Archive Carrier"
    - "Artifact/Carrier Placement"
version: 1
updated_at: "2026-10-05 00:00:00 +0000"
relations: {"relates_to": ["CA-D-289", "CA-D-466"]}
atom_id: "CA-D-565"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind new archived Revision Markdown Carrier

## Scope

The single Markdown Archive Carrier created for an Atom Revision newly placed in Archived status.

## Claim

**when** an Atom Revision newly attains its model-admitted `Archived` Status **and** no more-specific applicable Delivery mapping exists for its Artifact Type, its **`=1`** Markdown Archive Carrier **must** be classified as that Revision's Archive Carrier **and** be placed at `archived/<basename>@<version>.md`: `archived/` follows CA-D-466's Status fallback **and** `@<version>` follows CA-D-289.

## Details

This is a binding of the existing generic Status-placement and Archive-basename rules, not a universal placement override. A more-specific admitted Delivery mapping takes precedence. It neither relocates nor reclassifies an existing immutable legacy `archive/` Carrier, and it does not settle placement for a Revision without the stated newly archived Markdown Carrier.
