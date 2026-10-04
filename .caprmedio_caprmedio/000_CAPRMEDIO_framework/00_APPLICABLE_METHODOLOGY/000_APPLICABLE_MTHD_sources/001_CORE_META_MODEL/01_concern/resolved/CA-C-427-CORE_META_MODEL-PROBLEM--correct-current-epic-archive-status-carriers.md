---
atom_id: CA-C-427
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Atom/Revision/Status"
  depends_on: ["Atom/Revision", "Artifact/Carrier", "Atom/Revision/Updated At"]
version: 1
updated_at: "2026-10-04 17:58:53 +0000"
relations:
  concern_about: [CA-O-010, CA-O-011, CA-O-015, CA-P-1478]
---
# Summary

Correct current Epic archive Status carriers

## Concern

Six whole prior Workflow Revision snapshots newly retained for this Epic still explicitly carried Active despite their non-current archive placement: O010@7/@8, O011@10/@11 and O015@6/@7. This conflicts with their actual prior-Revision disposition and can misrepresent active source authority. The issue is bounded to these six files; it does not establish a defect in older history or current definitions.

## Evidences

P1478 captured each complete pre-edit carrier, found its unique explicit Active Status and matching @version basename, then changed only Status to Archived and Updated At to the actual 2026-10-04 17:55:44 +0000 edit instant. R1419v9 admits Archived for prior Revisions; R1788v1 requires actual Updated At for every accepted carrier edit; R1432v9/O067v6 retain identity and Version for carrier_only recoding; D289v12 preserves the @version basename and D270v13 governs timestamp serialization.

The saved complete before/after comparison, exact six basenames, former timestamps, byte lengths and full SHA-256 values are retained in physical Done P1478. All six full successor strings exactly equal their captured predecessors after only those two permitted frontmatter replacements. Every other byte is preserved, including Summary, body, identity, Version and other metadata.

## Blast radius

### Disposition

Resolved by the exact six-carrier correction and complete byte comparison in P1478. No current Workflow/Step source, older pre-Epic archive, implementation, source generation or runtime behavior was changed or accepted. Root retains source-stage and dependent-gate authority; this narrow Concern does not close those stages.
