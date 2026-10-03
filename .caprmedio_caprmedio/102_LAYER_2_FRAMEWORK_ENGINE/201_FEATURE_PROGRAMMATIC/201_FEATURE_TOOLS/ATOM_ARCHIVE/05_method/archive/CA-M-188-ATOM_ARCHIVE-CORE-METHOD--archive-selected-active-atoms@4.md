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
    - CA-R-868
  derived_from:
    - CA-A-058
---
# Archive selected active Atoms

## Applicable when

Use this Method when a caller prepares withdrawal of current authority from one active Atom or one frozen bulk set of two or more active Atoms while preserving historical carriers. Actual archiving is permitted only when an authorized project-local MCP delegation supplies a sealed Initiative action envelope.

## Procedure

1. Resolve every target uniquely, prove it is an active Atom in its owning Content role, and capture its path, ID, revision, and digest.
2. Derive one role-local archive destination per target while preserving its filename, bytes, stable Atom ID, revision history, and any existing historical dependents.
3. Reject drafts, already archived carriers, non-Atoms, invalid archive locations, destination collisions, and repeated or stale targets.
4. Freeze the complete archive map and publish a mutation-free dry-run.
5. On explicit authorized `--apply`, recheck every source and destination precondition, then move the complete atomic or bulk set and remove it from current-authority discovery.
6. Verify archived presence, active absence, byte identity, and retained historical resolvability; roll back on any discrepancy.

## Outcome

Every selected Atom is preserved in its role-local archive and no longer contributes current authority.

## Failure or stop

Remain in dry-run mode without delegated apply authority. Stop or roll back the full set when lifecycle, source, destination, collision, or postcondition checks fail.
