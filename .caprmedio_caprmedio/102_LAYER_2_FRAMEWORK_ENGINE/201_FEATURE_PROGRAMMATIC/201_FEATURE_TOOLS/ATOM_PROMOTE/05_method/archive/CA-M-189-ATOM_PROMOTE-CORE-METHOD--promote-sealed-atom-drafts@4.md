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
    - CA-R-869
  derived_from:
    - CA-A-058
---
# Promote sealed Atom drafts

## Applicable when

Use this Method when a caller prepares acceptance of one draft Atom or one frozen bulk set of two or more drafts as current authority and assigns stable role-matching IDs. Actual promotion is permitted only when an authorized project-local MCP delegation supplies a sealed Initiative action envelope.

## Procedure

1. Resolve every selected source as a current draft and bind it to one operator-supplied stable Atom ID.
2. Validate that each assigned ID matches the draft Content role, is unused, and derives exactly one canonical active filename and active location.
3. Derive the promotion map by removing only the `drafts` lifecycle path segment and changing the carrier filename; preserve each draft carrier's bytes exactly.
4. Freeze the complete source, assigned-ID, and destination map and publish a mutation-free dry-run.
5. On explicit authorized `--apply`, recheck source digests, ID absence, and destination absence, then move the complete atomic or bulk set as one rollbackable transaction.
6. Verify byte identity, unique active identity, absence from the draft surface, and complete set membership.

## Outcome

Each accepted draft becomes exactly one byte-identical active Atom with its operator-assigned stable identity.

## Failure or stop

Remain in dry-run mode without delegated apply authority. Stop or roll back on invalid or mismatched IDs, collisions, non-draft inputs, stale carriers, changed destination absence, or incomplete promotion.
