---
atom_id: CA-E-299
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Validate And Describe Atom Replacement"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Action"
    - "Journal/Record"
version: 9
updated_at: "2026-10-04 17:36:48 +0000"
relations: {"evaluation_for":["CA-R-1041","CA-O-031","CA-R-807"],"derived_from":["CA-A-057"]}
---
# Summary

Describe one admitted Atom replacement

## Scope

CA-O-031 descriptions of admitted singular or frozen bulk Atom replacement boundaries before application.

## Claim

CA-O-031 describes the complete admitted replacement boundary under CA-R-1041 **before** apply, including **every** already-active successor allowed by CA-R-807.

## Details

### Test cases

- submit an admitted active predecessor with **`=1`** successor; repeat with **`>=2`** distinct active successors. retain exact IDs, Revisions, stated change class, **and** sealed Initiative context.
- submit a frozen bulk set of explicit predecessor-to-successor-set mappings. include a mapping with multiple successors; check that no pair-only normalization drops a successor **or** changes the approved atomic boundary.
- independently submit a missing, unresolved, inactive, duplicate, **or** self-referential ID **and** incomplete admission evidence. a successor becoming inactive **after** preview **must not** be treated as still admitted at the effect boundary.

### Acceptance criteria

- the description preserves the exact predecessor identity **and** complete explicit successor set for **every** mapping, **without** applying, promoting, **or** archiving **any** Carrier.
- dry run is mutation-free. no inferred successor, implicit creation, replacement Relation, Journal append, staging, **or** Commit occurs during description.
- invalid **or** incomplete requests do **not** yield an admitted replacement description. a valid multi-successor mapping is **not** rejected merely because it is **not** one-to-one.
- the sealed context preserves the approved singular **or** bulk boundary; actual authorized application remains subject **to** CA-O-031 **and** the separate admission cases **in** CA-E-247.

### Failure disposition

reject the realization on lost **or** invented IDs, incomplete boundaries, unauthorized effects, changed atomicity, **or** acceptance **without** required admission evidence. retain the supplied **and** returned mappings **and** exact before/after Carrier evidence.
