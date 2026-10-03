---
atom_id: CA-E-516
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Tool"
    - "Projection"
    - "Applicable Methodology"
    - "Atom/Revision"
    - "Evaluation"
version: 2
updated_at: "2026-10-01 21:46:55 +0400"
relations:
  evaluation_for:
    - CA-R-1622
  relates_to:
    - CA-D-305
    - CA-E-379
    - CA-O-087
---
# Summary

Check Atom validator projected-source bindings

## Scope

`VALIDATE_ATOMS` projected-Carrier source bindings.

## Claim

the `VALIDATE_ATOMS` projected-Carrier check **must** implement CA-D-305-CORE_META_MODEL-CORE-DELIVERY--carry-projected-atoms-without-new-identity source binding faithfully.

- accept a valid relative binding **to** the selected original source Atom **when** identity, Revision, **and** authored bytes match.
- reject missing, ambiguous, wrong-source, stale, **or** out-of-bound bindings, modified Claims, **and** generated Projection metadata placed on an authoritative source Atom.
- resolve the relative path from the projected file's directory; include nested output fixtures.
- remove **only** the admitted generated binding for byte comparison. preserve **all** source Properties **and** body content; do **not** strip arbitrary extra metadata **to** obtain a match.
- preserve the one-way Projection-to-source binding **without** inventing a second Atom identity **or** demanding an inverse link on the source.

## Details
