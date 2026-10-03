---
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 5
updated_at: 2026-09-01 02:30:00 +0400
relations:
  evaluation_for:
    - CA-R-1048
    - CA-R-1093
---
# Evaluate one sealed Atom identity migration

## Test case

Given identityless legacy, existing-ID correction, duplicate-ID repair, and same-path relation/frontmatter-update temporary active Atom carriers with complete sealed requests, evaluate `MIGRATE_ATOM_IDENTITY` dry run twice per request. Both receipts must be byte-identical, name the expected source and result digests, list only declared changes, omit derived `atom_id` and `tier`, and report no Journal or Git effect.

Verify direct `--apply` is rejected without authorized project-local MCP delegation. Verify an authorized MCP delegation applies only the sealed migration, returns the deterministic receipt, and receives durable `COMMIT_TRIGGER` intake acknowledgement without a Journal append, staged file, or Git commit. Failure cases for source digest, version, duplicate target, occupied destination, old identity, and relation target leave every carrier unchanged.

## Sources

- [CA-R-1048 — Migrate one sealed Atom identity](../../04_requirement/CA-R-1048-TOOLS-CORE-REQUIREMENT--migrate-one-sealed-atom-identity.md)
