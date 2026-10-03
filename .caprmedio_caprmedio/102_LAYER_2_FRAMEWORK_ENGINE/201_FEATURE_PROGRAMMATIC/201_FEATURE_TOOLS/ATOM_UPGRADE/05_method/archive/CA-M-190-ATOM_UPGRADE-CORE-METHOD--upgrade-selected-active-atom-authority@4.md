---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 4
updated_at: 2026-09-02 01:10:00 +0400
relations:
  method_for:
    - CA-R-870
  derived_from:
    - CA-A-058
---
# Upgrade selected active Atom authority

## Applicable when

Use this Method when a caller prepares one active Atom or one frozen bulk set of two or more active Atoms for an explicitly supplied enabled higher `core` or `standard` Tier while retaining stable identity. Actual upgrade is permitted only when an authorized project-local MCP delegation supplies a sealed Initiative action envelope.

## Procedure

1. Resolve every source as an active Atom and capture its current Tier, Scope Unit, stable ID, revision, and digest together with its explicit target Tier and optional target Scope Unit.
2. Require each target Tier to be enabled, `core` or `standard`, and strictly higher than the source Tier; require the target Scope Unit to be the source unit or one explicitly named ancestor.
3. Derive the target authority location and, when Scope Unit changes, the canonical filename scope segment while preserving the stable Atom ID and advancing revision metadata once.
4. Validate target placement, authority relations, ID and destination collision freedom, and every complete resulting carrier; then publish the frozen dry-run map.
5. On explicit authorized `--apply`, recheck every source and destination precondition and perform the complete atomic or bulk upgrade as one rollbackable transaction.
6. Verify that exactly one active carrier owns each stable ID at its approved higher Tier and that every former carrier is absent.

## Outcome

Each Atom retains its stable identity while its current authority is represented exactly once at the approved higher Tier.

## Failure or stop

Remain in dry-run mode without delegated apply authority. Stop or roll back on a non-active source, forbidden, disabled, or non-higher target Tier, invalid scope ancestry, collision, stale precondition, or failed uniqueness check.
