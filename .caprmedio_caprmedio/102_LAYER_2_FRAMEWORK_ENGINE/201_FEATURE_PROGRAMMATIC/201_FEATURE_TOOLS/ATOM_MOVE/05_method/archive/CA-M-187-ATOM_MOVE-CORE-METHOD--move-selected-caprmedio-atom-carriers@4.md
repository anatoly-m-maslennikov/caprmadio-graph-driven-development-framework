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
    - CA-R-867
  derived_from:
    - CA-A-058
---
# Move selected CAPRMEDIO Atom carriers

## Applicable when

Use this Method when a caller prepares relocation of one exact Atom or one frozen bulk set of two or more Atom carriers without changing their bytes, filenames, or identities. Actual relocation is permitted only when an authorized project-local MCP delegation supplies a sealed Initiative action envelope.

## Procedure

1. Resolve the exact selector or recursive source subtree, retain only Atom carriers, and capture every source path, filename, ID, and digest.
2. Derive one destination mapping per selected Atom, preserving selected subtree shape by default and flattening only when the sealed Initiative explicitly requests it.
3. Validate destination Scope Unit and Content-role placement, source membership, path uniqueness, and destination collision freedom without editing carrier bytes.
4. Freeze the complete move map and publish a mutation-free dry-run.
5. On explicit authorized `--apply`, recheck source digests and destination absence, then move the complete atomic or bulk set as one rollbackable transaction.
6. Verify that every source is absent, every mapped destination is present, non-Atom files are untouched, and each moved carrier retains its original bytes, filename, and Atom ID.

## Outcome

The selected carriers occupy exactly their approved destinations and remain byte-identical governed Atoms.

## Failure or stop

Remain in dry-run mode without delegated apply authority. Stop or roll back the full move on an invalid destination, collision, stale source, incomplete mapping, changed destination absence, or failed post-move verification.
