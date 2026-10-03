---
subjects:
  governs: "Atom/Carrier/Canonical Address"
  depends_on:
    - "Atom/Property"
    - "Atom/Summary"
    - "Atom/Identifier"
    - "Atom/Revision/Status"
    - "Markdown Atom Carrier"
version: 4
updated_at: "2026-10-02 19:57:02 +0400"
relations: {"relates_to": ["CA-D-478", "CA-D-282", "CA-D-466"]}
atom_id: "CA-D-480"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Keep Atom addresses consistent with carried Properties

## Scope

Atom Properties represented by a filename, matching directory name, or placement.

## Claim

**every** Atom Property represented by a filename, matching directory name, **or** placement **must** agree with its canonical internal value under the applicable Delivery encoding.

- compare resolved values using the registered encoding; a Summary Slug is checked against its Summary serialization, **not** against identical raw text.
- a mismatch is invalid **and** **must** be reported; the address **must not** silently override the value carried inside the Atom.
- agreement checking does **not** authorize rewriting the Atom **or** address. corrections require the applicable authorized change.

## Details
