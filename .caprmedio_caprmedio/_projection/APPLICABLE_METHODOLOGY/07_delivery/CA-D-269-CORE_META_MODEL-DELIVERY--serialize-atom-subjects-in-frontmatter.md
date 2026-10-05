---
subjects:
  governs: "Atom/Subjects/Frontmatter"
  depends_on:
    - "Atom/Subjects"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Subject Path"
    - "Subject"
    - "Relation Kind"
version: 12
updated_at: "2026-10-02 19:05:39 +0400"
relations: {}
atom_id: "CA-D-269"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter.md
  source_atom_id: CA-D-269
  source_atom_revision: 12
  source_sha256: eea15e5b1c2411acdd552c8701da98ac34bab89a107ee05f28760eb1ce8eeac3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Atom Subjects in Frontmatter

## Scope

New **or** migrated Markdown Atom Carriers.

## Claim

**every** new **or** migrated Markdown Atom Carrier **must** serialize its Subjects directly as **`=1`** scalar Subject Path at `subjects.governs` **and** an unordered collection of **`>=0`** unique scalar Subject Paths at `subjects.depends_on`; an absent dependency collection **means** zero dependencies. the `governs` **or** `depends_on` key encodes the Subject Relation Kind; the source Atom is implicit **and** the scalar value encodes its target's Subject Path, **not** the Subject Relation itself. these values resolve their canonical targets under CA-R-1202-CORE_META_MODEL-CORE-REQUIREMENT--resolve-every-direct-subject-target-once **without** an intermediate Subject/Entity **or** Subject/Reference field **or** a repeated target-kind field.

## Details

an existing unmigrated Carrier **may** temporarily retain `subjects.<governs|depends_on>.<continuant|occurrent>` **only** **until** its explicitly assigned carrier-migration Task is executed. this compatibility is migration-limited, preserves the same direct relation facts **and** target identities, **and** does **not** establish a second canonical representation. legacy temporal-classification authority **and** bulk Carrier conversion require their separately assigned migration Tasks.
