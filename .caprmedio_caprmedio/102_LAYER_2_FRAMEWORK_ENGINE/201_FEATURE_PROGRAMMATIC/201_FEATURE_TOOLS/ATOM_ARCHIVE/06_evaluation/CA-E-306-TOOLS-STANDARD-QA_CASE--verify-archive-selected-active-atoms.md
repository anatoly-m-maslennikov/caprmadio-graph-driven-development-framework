---
atom_id: CA-E-306
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_ARCHIVE"
  depends_on: ["Atom", "Atom/Revision", "Artifact/Carrier", "Archive Selected Active Atoms", "Journal/Record", "Atom/Revision/Status", "Atom/Revision/Updated At"]
version: 11
updated_at: "2026-10-04 17:35:27 +0000"
relations:
  evaluation_for: [CA-R-868, CA-O-029, CA-D-289, CA-D-303]
  relates_to: [CA-R-1521, CA-R-1788, CA-R-1662]
---
# Summary

Verify archive selected active atoms

## Scope

Sealed single/bulk archive selections, their qualified status/placement transitions, historical preservation and complete mutable-frontier recovery.

## Claim

ATOM_ARCHIVE follows CA-R-868 **and** CA-O-029: withdraw the complete selected active authority while preserving historical meaning **and** Carriers under CA-D-289 **and** CA-D-303, with only admitted lifecycle Status **and** actual Updated At metadata changes.

### Test cases

1. use an isolated fixture with **`=1`** singly selected active Atom, **`>=2`** active Atoms selected as a bulk set, **`=1`** Draft, **`=1`** already archived Atom, **and** an existing historical reference **to** a bulk source. record exact before-state paths, IDs, Versions, Summaries, bodies, properties, bytes **and** digests, plus the actual Content Role/Type's applicable status/transition model.
2. record singular **and** bulk dry runs. attempt apply **without** delegated authority; submit mixed-lifecycle, non-Atom, repeated-target, stale-source, missing/unsupported status-model, invalid-destination, **and** destination-collision requests. **every** rejected preflight leaves the fixture unchanged.
3. archive the valid single **and** bulk selections through sealed Initiative envelopes. verify the role-local destinations **and** required `@<version>` basenames. separately prove unchanged IDs, Versions, Summaries, complete body, governed meaning, other properties **and** prior history; prove the admitted archival Status **and** actual refreshed Updated At under CA-R-1521/CA-R-1788. retain exact before/after digests as evidence of the real transition, **not** an expectation that the complete Carrier digest stays equal across permitted metadata changes. current discovery excludes the withdrawn authority, the Draft remains a Draft, **and** the historical reference still resolves.
4. from an independent before-state, inject a failure **after** **`>=1`** selected archive effect **or**, for one atomic publication, **after** publication **and** **before** final verification. also exercise a postcondition failure.

### Acceptance criteria

- valid applies archive **all** selected Atoms **and** leave no active selected Carrier. no promotion, upgrade, semantic Version change, unrelated mutation, **or** loss of existing history occurs; lifecycle Status **and** actual Updated At change only as admitted.
- dry runs mutate nothing **and** expose the full archive map, including the suffix **and** admitted metadata effects. an unchanged active filename is **not** the expected archive filename.
- a post-effect failure restores **every** selected mutable source **and** destination **to** its exact before-state. preserve accepted Journal evidence **and** report failure with the actual recovery result, **not** archive success.
- a preflight rejection alone does **not** establish rollback coverage. incomplete **or** unverified restoration fails the Evaluation.

### Failure disposition

reject a realization that violates **any** required case. retain lifecycle classifications, authority result, archive map, current-authority result, preserved-body/property comparisons, exact before/after digests, historical-reference evidence, injected fault position, **and** recovery evidence.

## Details
