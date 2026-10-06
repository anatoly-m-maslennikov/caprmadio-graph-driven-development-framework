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
version: 2
updated_at: "2026-09-25 20:51:44 +0000"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-103-CORE_META_MODEL-ACTION--author-atom-content-before-summary.md
  source_atom_id: CA-O-103
  source_atom_revision: 2
  source_sha256: d76750e7aae02fff73f089cc142514f3dc000396df81b97100c6017a33b1ddb8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Author Atom content before Summary

## Operation

Atom Content Authoring **means** the Action that takes an authorized authoring request, the Atom's Content Role, applicable authority, **and** **any** existing Revision, then prepares a coherent candidate through this flow:

1. for RMED, write Scope describing applicability, **then** write **=1** Claim within that Scope. for other Content Roles, write their primary contribution: Question, Concern, Objective, **or** Operation.
2. write the remaining body sections under CA-D-479 **and** the applicable Method. keep Details within the primary contribution **and** its applicability; RMED Details support the Claim **without** changing Claim **or** Scope.
3. review the primary contribution **and** its applicability against the completed remaining content. for RMED, review Scope **and** Claim together. **if** either needs changing, revise it explicitly within the authorized request **and** recheck the affected sections; never let Details silently change the contribution **or** applicability.
4. derive Summary from the finalized primary contribution within its applicability **only after** that review. for RMED, summarize the Claim within Scope, **not** Scope alone. for an existing Atom identity, compare the needed Summary with its established value; **if** a change is needed, return replacement required under CA-R-1464 rather than mutating that identity.
5. return the candidate, its review findings, **and** ready, replacement required, **or** blocked outcome. unresolved inconsistency **or** unmet permission **or** confidence gates returns blocked, **not** a ready candidate.

## Details

this Action prepares content; it does **not** persist, promote, replace, **or** archive an Atom. Carrier display order remains Summary first even though Summary is authored last. an Analysis TLDR is part of the other Markdown written **before** the primary-contribution review; it does **not** become the Atom Summary source.
