---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 01:10:00 +0400
relations:
  evaluation_for:
    - CA-M-190
---
# Verify upgrade selected active atom authority

## Claim checked

CA-M-190 upgrades one active Atom or a frozen bulk set to a strictly higher enabled `core` or `standard` Tier while preserving stable identity.

## Applicable when

Apply to any realization of CA-M-190 before it can change an active Atom's Tier or authority location.

## Test case

Use one fixture with one active standard-tier Atom selected singly and two active standard-tier Atoms selected as a frozen bulk set. Record dry-runs for a same-tier target, a forbidden non-`core`/`standard` target, a disabled `core` target, and enabled higher `core` targets in the same Scope Unit and an explicit ancestor Scope Unit; attempt `--apply` without delegated authority, then apply the valid singular and bulk requests through sealed Initiative envelopes.

## Acceptance criteria

The unauthorized, same-Tier, forbidden-tier, and disabled-tier requests change no carrier; valid singular and bulk requests create one canonical higher-Tier carrier per source in the approved Scope Units, preserve every stable Atom ID, advance each revision exactly once, derive the ancestor filename scope segment where applicable, remove every former carrier, and leave no second active owner of any ID.

## Failure disposition

Reject the realization and preserve Tier and ancestry evidence, dry-run maps, authority result, identity scans, revisions, and any duplicate or stale authority carrier.
