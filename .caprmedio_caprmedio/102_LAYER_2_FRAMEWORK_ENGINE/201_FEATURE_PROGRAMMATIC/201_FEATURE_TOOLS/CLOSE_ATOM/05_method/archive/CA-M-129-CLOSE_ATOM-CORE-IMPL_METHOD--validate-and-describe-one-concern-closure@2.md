---
subject_scopes:
  - concern-resolution
version: 2
updated_at: "2026-08-23 11:37:28"
---
# Validate and describe one Concern closure

For one closure request, load the repository, resolve the Concern and every supplied resolver or solution by exact active Atom ID, and reject an unresolved or inactive carrier. Require a nonempty terminal disposition, preserve the action context unchanged, and return a closure intent targeting `solved`.

Return a separate deferred commit-pipeline handoff with the exact Concern, resolver, and solution IDs. Do not infer graph relations, write a solved carrier, append a Journal event, stage files, or create a commit. On `--apply`, return the validated intent with an apply-blocked diagnostic until the lifecycle-intent handoff is admitted by the commit pipeline.
