---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Upgrade Selected Atom Authority"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Local Tier"
    - "Atom/Global Tier"
    - "Scope Unit"
    - "Artifact/Revision"
    - "Artifact/Carrier"
version: 10
updated_at: "2026-09-17 03:44:21 +0000"
relations: {"evaluation_for":["CA-R-870","CA-O-045"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify upgrade selected active atom authority

## Claim checked

CA-O-045 upgrades one active Atom **or** a frozen bulk set **to** a strictly higher enabled `core` **or** `standard` Tier while preserving stable identity.

## Applicable when

Apply **to** **any** realization of CA-O-045 **before** it can change an active Atom's Tier **or** authority location.

## Test case

Use one fixture with one active standard-tier Atom selected singly **and** two active standard-tier Atoms selected as a frozen bulk set. Record dry-runs for a same-tier target, a forbidden non-`core`/`standard` target, a disabled `core` target, **and** enabled higher `core` targets **in** the same Scope Unit **and** an explicit ancestor Scope Unit; attempt `--apply` **without** delegated authority, **then** apply the valid singular **and** bulk requests through sealed Initiative envelopes.

## Acceptance criteria

the unauthorized, same-Tier, forbidden-tier, **and** disabled-tier requests change no carrier; valid singular **and** bulk requests create one canonical higher-Tier carrier per source **in** the approved Scope Units, preserve **every** stable Atom ID, advance each revision exactly once, derive the ancestor filename scope segment **where** applicable, remove **every** former carrier, **and** leave no second active owner of **any** ID.

## Failure disposition

Reject the realization **and** preserve Tier **and** ancestry evidence, dry-run maps, authority result, identity scans, revisions, **and** **any** duplicate **or** stale authority carrier.

## Post-effect failure coverage

from an independent recorded before-state, inject a failure **after** **`>=1`** selected Carrier is published at its target authority location **and** **before** the complete singular **or** bulk upgrade succeeds.

- verify restoration of **every** selected source **and** destination, with exact prior Carrier bytes, identity, Revision metadata, authority Relations, **and** path existence. preserve unrelated Carriers **and** pre-existing history.
- verify that no duplicate active identity **or** partial higher-authority set remains. an incomplete **or** unverified restoration fails the rollback guarantee.
- retain actual failure **and** recovery evidence. rejected preflight alone does **not** prove post-effect recovery; a failed apply is **not** reported as a successful upgrade.
