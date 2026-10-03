---
subjects:
  declared:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-1048
    - CA-R-1093
---
# Evaluate one sealed Atom identity migration

Given identityless legacy, existing-ID correction, duplicate-ID repair, and same-path relation/frontmatter-update temporary active Atom carriers with complete sealed requests, evaluate `MIGRATE_ATOM_IDENTITY` dry run twice per request. Both receipts must be byte-identical, name the expected source and result digests, list only declared changes, omit derived `atom_id` and `tier`, and report no Journal or Git effect.

Verify direct `--apply` is rejected without authorized project-local MCP delegation. Verify an authorized MCP delegation applies only the sealed migration, returns the deterministic receipt, and receives durable `COMMIT_TRIGGER` intake acknowledgement without a Journal append, staged file, or Git commit. Failure cases for source digest, version, duplicate target, occupied destination, old identity, and relation target leave every carrier unchanged.
