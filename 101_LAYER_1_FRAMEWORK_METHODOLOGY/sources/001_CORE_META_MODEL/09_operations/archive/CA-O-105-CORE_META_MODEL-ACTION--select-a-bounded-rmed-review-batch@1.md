---
atom_id: CA-O-105
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-09-28 16:14:59 +0400"
subjects:
  governs: "Select RMED Review Batch"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Revision"
    - "Scope Unit"
    - "Framework Instance Settings"
    - "Operator"
relations: {"relates_to":["CA-D-496","CA-D-497"]}
---
# Summary

Select a bounded RMED review batch

## Operation

Select RMED Review Batch **means** the read-only Action that resolves a requested selection into a bounded, reproducible batch.

1. resolve the requested Scope Unit locally **or** with descendants, Global **or** Local Tiers, **or** explicit Carrier list from carried Properties **and** authoritative Project Structure; select active RMED source Atoms **only**. do **not** select Projections, history, **or** non-RMED sources.
2. establish an exact deduplicated source inventory **and** relevant authority, including Project Principles, Property/Entity definitions, relation targets, the Operator registry, settings, **and** current source bindings. missing selection-critical context returns `blocked`; context gaps for individual evaluation checks remain explicit.
3. resolve limits under CA-D-497. sort by canonical Atom ID, Revision, **then** source path; retain malformed **or** missing identifiers as inspectable candidates sorted by path, **not** fabricated identities.
4. estimate total work per candidate **and** take a deterministic prefix within both limits. retain the unselected queue. **if** the next single candidate exceeds the budget, return `blocked` with that candidate **and** the required budget decision; do **not** skip it invisibly **or** claim an empty successful batch.
5. create the manifest under CA-D-496 **without** modifying source Atoms. return `ready`, `empty` **only** for a genuinely empty requested selection, **or** `blocked`.

## Details

the default limits are stored **in** Default Settings. the caller supplies the admitted temporary output directory **and** effective permissions. estimate uncertainty is recorded; no fixed runtime is promised.
