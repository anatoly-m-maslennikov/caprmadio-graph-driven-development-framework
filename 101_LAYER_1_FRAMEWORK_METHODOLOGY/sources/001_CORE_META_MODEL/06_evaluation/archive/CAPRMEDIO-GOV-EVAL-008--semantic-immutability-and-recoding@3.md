---
artifact_subtype: qa_case
subjects:
  - evaluation
version: 3
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-EVAL-039--identity-migration-preserves-atomic-content
    - CAPRMEDIO-GOV-EVAL-040--semantic-immutability-boundary
  check_of:
    - CAPRMEDIO-GOV-REQU-300--semantic-immutability-and-lossless-recoding
  child_of:
    - CA-R-1054
---

# Semantic immutability and lossless recoding

## Claim checked

Lossless whole-graph recoding and unchanged archive relocation preserve every
protected semantic claim and relation, while semantic mutation requires a new
governed revision or successor.

## Applicable conditions

1. Snapshot every protected semantic field and relation endpoint.
2. Perform a complete identifier, filename, heading, carrier, and target
   spelling migration.
3. Prove the semantic snapshot and graph connectivity are equal after recoding.
4. Move an inactive atom unchanged into its role-local archive.
5. Attempt to change one protected claim, rationale, provenance, scope,
   priority, relation meaning, or evaluation criterion and require rejection.

## Acceptance criteria

Lossless graph-wide recoding and unchanged archive relocation pass; every
semantic mutation fails and requires a successor identity.

## Failure disposition

Reject the migration or mutation, retain the previous graph, and record a
high-priority Concern with the first non-equivalent field or edge.
