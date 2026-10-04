---
atom_id: CA-E-304
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_UPDATE"
  depends_on: ["Atom", "Atom/Revision", "Atom/Summary", "Atom/Revision/Updated At", "Update Sealed Atom Carriers", "Artifact/Carrier", "Journal/Record"]
version: 11
updated_at: "2026-10-04 17:35:27 +0000"
relations:
  evaluation_for: [CA-R-866, CA-O-030, CA-R-1464, CA-R-1415, CA-R-1371]
  relates_to: [CA-O-067, CA-R-1432, CA-R-1788, CA-R-1662]
---
# Summary

Verify update sealed caprmedio atom carriers

## Scope

The sealed single/bulk ATOM_UPDATE capability, including identity-preserving change classes, exact current source state, prior semantic history and honest failed recovery.

## Claim

ATOM_UPDATE follows CA-R-866 **and** CA-O-030 **to** apply the sealed set atomically, preserving identity, Summary, placement, **and** exact prior semantic history with class-specific Version **and** actual edit-time results.

### Test cases

1. prepare an isolated fixture with a valid single-Atom semantic content update, a frozen two-Atom frontmatter-and-content update, **and** an unassigned Draft update. include a mixed-class bulk set. seal paths, filenames, assigned IDs **when** present, Versions, Updated At values, digests, exact proposals **and** admitted change classes. record exact dry-run previews.
2. submit repeated, missing, ambiguous, invalid, unauthorized, **and** stale requests, including a bulk source changed **after** dry run **or** an uncertain class. reject **without** changing the fixture. restore the sealed source **and** apply valid single **and** bulk requests through sealed Initiative envelopes.
3. request a Summary change while retaining the Atom ID, including a changed heading **and** a filename Summary Slug change. reject it as a same-ID update even **if** the Claim is unchanged; report the need for replacement **without** silently allocating **or** applying a successor.
4. apply formatting-only, lossless Subject-serialization **and** demonstrably equivalent refinement changes. compare interpreted values, applicability, Subjects, Relations, Summary **and** acceptance meaning **before** **and** **after**. require unchanged Version **and** actual refreshed Updated At for each accepted edit, with existing history unaltered **and** no fabricated semantic Revision. apply a semantic change to the same primary Claim with fixed Summary: require **`=1`** next Version **and** exact preservation of the prior semantic Revision. a changed Claim, applicability, Subject target **or** Relation meaning is **not** carrier-only **or** equivalent refinement merely because its serialization is lossless.
5. inject a failure **after** **`>=1`** selected effect, **or** **after** atomic publication **and** **before** final verification; also exercise failed post-write validation. compare the complete changed-then-restored mutable frontier, including current Carriers **and** newly created semantic archive destinations.
6. request an evidenced unchanged result. distinguish actual no-op from an accepted carrier edit: require no invented Version, Updated At **or** archive mutation. retain the actual no-op/result evidence for the governing Run receipt; file equality alone does **not** establish that receipt.

### Acceptance criteria

- valid applies match their sealed previews **and** admitted classes: `carrier_only` **and** equivalent `refinement` keep Version, while `semantic_revision` advances it **`=1`** time **and** preserves its exact prior semantic Revision. **every** accepted edit refreshes actual Updated At under CA-R-1788. retain identity, Summary, path **and** filename; the unassigned Draft remains unassigned.
- dry runs **and** rejected requests change nothing. no temporary, mixed, **or** partially updated state remains **after** a successful apply. an actual no-op is not a fictitious accepted edit **or** semantic Revision.
- successful recovery restores the entire mutable before-state, preserves pre-existing history **and** accepted Journal evidence, **and** reports the failed attempt rather than update success.
- preflight-only rejection does **not** prove recovery. incomplete **or** unverified restoration fails the Evaluation.

### Failure disposition

reject a realization that violates **any** required case. preserve sealed preconditions, authority **and** classification result, exact previews, rejection evidence, prior **and** final Carriers, fault position, **and** actual recovery result.

## Details
