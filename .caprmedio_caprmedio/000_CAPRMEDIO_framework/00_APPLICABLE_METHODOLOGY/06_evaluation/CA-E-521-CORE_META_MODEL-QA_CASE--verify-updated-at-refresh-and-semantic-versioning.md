---
subjects:
  governs: "Atom/Revision/Updated At"
  depends_on:
    - "Evaluation"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Atom/Revision/Version"
    - "Atom/Revision/Status"
    - "Atom/Summary"
    - "Atom/Identifier"
    - "Entity"
version: 1
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  evaluation_for:
    - CA-D-270
    - CA-R-1432
    - CA-R-1433
    - CA-R-1788
    - CA-O-051
atom_id: "CA-E-521"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-521-CORE_META_MODEL-QA_CASE--verify-updated-at-refresh-and-semantic-versioning.md
---
# Summary

Verify Updated At refresh and semantic Versioning

## Scope

accepted Markdown Atom Carrier edits classified by governed meaning.

## Claim

the Evaluation **must** accept **only** an edit that refreshes `updated_at` **and** changes Version exactly **when** governed meaning changes.

## Details

### Test case

- apply a formatting-only edit, a lossless Entity-name edit, **and** an equivalent refinement; verify an actual refreshed timestamp **and** an unchanged Version for **every** edit.
- apply a semantic revision; verify an actual refreshed timestamp **and** the next Version.
- archive a predecessor; verify `status: Archived`, archive-time `updated_at`, preserved Version, **and** preservation of body, Summary, identity, **and** **all** other metadata.

### Acceptance criteria

- reject an accepted edit with an unchanged `updated_at`.
- reject a nonsemantic edit that increments Version.
- reject a meaning-changing edit that retains Version.

the checked rules are `CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter`, `CA-R-1432-CORE_META_MODEL-GENERAL-REQUIREMENT--classify-admitted-atom-changes-by-semantic-effect`, `CA-R-1433-CORE_META_MODEL-GENERAL-REQUIREMENT--permit-version-preservation-for-carrier-only-relocation`, `CA-R-1788-CORE_META_MODEL--refresh-updated-at-whenever-an-atom-changes`, and `CA-O-051-CORE_META_MODEL-ACTION--persist-atom-replacement-through-ordered-carrier-transitions`.
