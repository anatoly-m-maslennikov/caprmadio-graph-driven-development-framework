---
atom_id: CA-P-937
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - CA Deterministic Routing Runtime Tool Set
    occurrent:
      - CA Deterministic Routing Runtime Tool Implementation
  depends_on:
    occurrent:
      - CA-P-936
version: 1
updated_at: 2026-09-01 23:04:33 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Implement CA Deterministic Routing Runtime Tools

**when** CA-P-936 is Done, **then** the Assignee **must** implement the deterministic provider-neutral Tools that load the accepted CA authority, normalize an invocation, resolve the active Project, select the canonical route, and admit or reject the requested effect.

## Scope

`((accepted CA Main Skill Authority Bundle) union (canonical Tool source, schemas, tests, structured results, and failure contracts for CA authority loading, normalization, Project resolution, routing, effect classification, approval gating, and authority-snapshot pinning))`

## Definition of Done

the Task is **not done if** (identical authority and invocation inputs can produce different route results **or** any Tool invents authority, embeds host-specific Skill procedure, bypasses an effect or approval gate, accepts an unresolved Project or route, widens scope implicitly, or fails open **or** results omit the selected authority revision and digest, normalized request, exact route, effect class, approval decision, and explicit failure meaning **or** focused positive, negative, stale-snapshot, ambiguity, and determinism tests fail).

## Details

keep Tool mechanics independent from MCP transport and Skill prose. pin one accepted authority snapshot for each invocation and reject a mid-run authority change until an explicit reload creates a new admitted snapshot.
