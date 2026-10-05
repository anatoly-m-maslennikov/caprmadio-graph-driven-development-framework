---
subjects:
  governs: "Atom/Content Role: Plan/Authoritative Carrier Bundle"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan/Carrier/Stem"
    - "File Carrier"
    - "Directory Carrier"
version: 6
updated_at: "2026-10-02 19:44:54 +0400"
relations: {"relates_to": ["CA-R-1578", "CA-D-469"]}
atom_id: "CA-D-460"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-460-CORE_META_MODEL-CORE--serialize-plan-atom-carrier-bundles.md
  source_atom_id: CA-D-460
  source_atom_revision: 6
  source_sha256: 7879c6dd77ac6eab1f6a5b80b9fab58112b9d7d6111b169d5038185597b53f23
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Plan Atom Carrier Bundles

## Scope

Plan Atom Carrier Bundles.

## Claim

a Plan Atom Carrier Bundle **must** consist of **`=1`** Markdown File Carrier **and** **`<=1`** optional matching Directory Carrier using the same canonical stem under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems.

- the Markdown file carries the Plan's own Properties **and** follows CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections, including its mandatory Definition of Done.
- a matching directory organizes related Plan Carriers; it neither creates another Atom **nor** replaces the mandatory Markdown file.
- the file **and** optional directory represent the same identity, Summary, Label, **and** Status, checked under CA-D-480-CORE_META_MODEL-DELIVERY--keep-atom-addresses-consistent-with-carried-properties.
- related Plan files carry independent Atoms; they are **not** additional Carriers of the Hub's Claim.

## Details
