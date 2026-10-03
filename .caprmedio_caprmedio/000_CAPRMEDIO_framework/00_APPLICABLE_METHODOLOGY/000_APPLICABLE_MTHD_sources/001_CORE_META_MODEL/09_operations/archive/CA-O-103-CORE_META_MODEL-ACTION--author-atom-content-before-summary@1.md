---
atom_id: CA-O-103
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Atom Content Authoring"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Claim"
    - "Atom/Details"
    - "Atom/Summary"
    - "Atom/Content Role"
    - "Author"
relations: {"relates_to": ["CA-M-111", "CA-D-479", "CA-R-1465", "CA-R-1464", "CA-E-384"]}
version: 1
updated_at: "2026-09-25 11:32:01 +0000"
global_tier: 11
---
# Summary

Author Atom content before Summary

## Operation

Atom Content Authoring **means** the Action that takes an authorized authoring request, the Atom's Content Role, applicable authority, **and** **any** existing Revision, then prepares a coherent candidate through this flow:

1. write the first body block for the selected Content Role: Claim, Question, Concern, Objective, **or** Operation.
2. write the remaining body sections under CA-D-479 **and** the applicable Method. keep Details within the first block.
3. review the first block against the completed remaining content. **if** it needs changing, revise it explicitly within the authorized request **and** recheck the affected sections; never let Details silently change the primary contribution.
4. derive Summary from the finalized first block **only after** that review. for an existing Atom identity, compare the needed Summary with its established value; **if** a change is needed, return replacement required under CA-R-1464 rather than mutating that identity.
5. return the candidate, its review findings, **and** ready, replacement required, **or** blocked outcome. unresolved inconsistency **or** unmet permission **or** confidence gates returns blocked, **not** a ready candidate.

## Details

this Action prepares content; it does **not** persist, promote, replace, **or** archive an Atom. Carrier display order remains Summary first even though Summary is authored last. an Analysis TLDR is part of the other Markdown written **before** the first-block review; it does **not** become the Atom Summary source.
