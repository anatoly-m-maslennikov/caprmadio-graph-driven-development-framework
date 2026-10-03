---
subject_scopes:
  - artifact-operations
version: 2
updated_at: "2026-08-23 11:37:28"
---
# Validate and describe one Atom replacement

For one replacement request, load the repository, resolve the predecessor and successor by their exact active Atom IDs, and reject an unresolved, inactive, duplicated, or self-referential pair. Preserve the supplied action context unchanged. Return a structured replacement intent naming the verified successor admission and the requested predecessor archive transition.

Return a separate deferred commit-pipeline handoff with the two explicit Atom IDs and action context. Do not derive relation kinds, edit either carrier, append a Journal event, stage files, or create a commit. On `--apply`, return the same validated intent with an apply-blocked diagnostic until the lifecycle-intent handoff is admitted by the commit pipeline.
