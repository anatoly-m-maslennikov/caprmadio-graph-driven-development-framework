---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMEDIO-GOV-METH-042--verbose-semantic-identities
      - CAPRMEDIO-GOV-REQU-416--identity-migration-preserves-atomic-content
---

# Test Case — Preserve atomic content during identity migration

For each migrated atomic artifact, compare the pre-migration and post-migration
carriers after normalizing only:

1. the artifact's canonical semantic ID;
2. its carrier filename and identity-bearing heading label;
3. relation and lifecycle target identifiers;
4. canonical identifier references in governed text; and
5. generated or compiled references derived from those identifiers.

The normalized carriers must be equal. The migrated repository must contain no
identifier using a retired short kind, no alias lookup for one, no duplicate
canonical identity, and no unresolved relation or lifecycle target.

## Primary claim

A deterministic migration check proves canonical identity closure while preserving every atomic artifact's non-identity governed content.
