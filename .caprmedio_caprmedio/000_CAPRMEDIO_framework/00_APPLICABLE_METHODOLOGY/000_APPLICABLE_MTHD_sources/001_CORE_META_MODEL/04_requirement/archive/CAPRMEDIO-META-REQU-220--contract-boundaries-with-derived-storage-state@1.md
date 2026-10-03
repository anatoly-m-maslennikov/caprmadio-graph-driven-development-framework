---
subject_scope: scope-topology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-186--contract-boundaries
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-192--explicit-relational-endpoints
      - CAPRMEDIO-META-REQU-214--nonduplicative-artifact-properties
---

# Requirement — Preserve Contract boundaries without stored lifecycle state

An operator-accepted DDL, file schema, API, protocol, host format,
supported-platform interface, CI interface, dependency boundary, or comparable
participant obligation is governed as an atomic relational Definition named
Contract.

Every Contract declares its accepted source, relation kind, role-bearing
endpoints, direction, conformance, compatibility, priority, and applicable
replacement relations. External sources are pinned by version or digest.
Implementation conforms to the Contract and cannot rewrite it.

Acceptance is inherent to atomic emission. Active or archived storage state is
derived from repository placement and is not duplicated in the Contract.

## Rationale

A boundary obligation must remain explicit and independently authoritative.
Removing stored lifecycle state preserves atomic immutability and prevents a
second writable representation of repository placement.
