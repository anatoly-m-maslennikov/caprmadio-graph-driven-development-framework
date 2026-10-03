---
atom_id: CA-R-1386
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define the GENERATE_ENTITY_GRAPH Tool unit

`GENERATE_ENTITY_GRAPH` MUST be an immediate executable projection Doer Tool Scope Unit of `TOOLS`, with authority-relative path `GENERATE_ENTITY_GRAPH` and delivery-relative path `GENERATE_ENTITY_GRAPH` under the current configured TOOLS authority and delivery roots.

The Tool derives and optionally persists a non-authoritative Entity and Term graph Projection from one explicitly selected source frontier. It may read authority but MUST NOT create, update, move, archive, promote, upgrade, replace, or otherwise mutate an Atom, Journal, configuration carrier, or other source of truth.
