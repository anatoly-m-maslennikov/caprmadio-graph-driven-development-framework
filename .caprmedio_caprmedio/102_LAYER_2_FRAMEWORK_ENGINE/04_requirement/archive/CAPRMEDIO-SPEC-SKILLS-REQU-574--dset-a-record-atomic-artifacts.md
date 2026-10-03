---
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
relations:
  - type: child_of
    targets:
      - "CAPRMEDIO-SPEC-SKILLS-REQU-572--atomize-every-operator-input"
---

# Requirement — Use dset-a-record for new atomic artifacts

DSET provides `dset-a-record` as the secondary skill that emits new atomic
artifacts of every registered atomic type and subtype.

The skill receives or resolves the current `scope_path`, validates the
artifact-creation gate, preserves session provenance, allocates the correct
identity, and writes exactly the accepted atomic claims. It never updates an
existing atomic artifact and never creates or updates an evergreen or
maintained artifact.

The initialized DSET session may call this skill from natural-language intent
after Exploration Mode has produced a sufficiently precise claim and the
operator has clearly promoted that claim for recording.

## Rationale

A dedicated atomic writer makes immutability and creation gates explicit while
keeping the operator-facing workflow small. The provisional name may later be
replaced by a successor Requirement without weakening this responsibility
boundary.
