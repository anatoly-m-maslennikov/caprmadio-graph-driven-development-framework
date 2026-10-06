---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-18 02:17:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-153--preserve-bounded-meaning-across-structural-scales
---
# Define current Layer handoffs

Each adjacent boundary owns a handoff:

| Boundary | Accepted input | Produced output |
|---|---|---|
| META → GOV | Semantic invariants and layer constitution | Governable carriers, identities, settings, lifecycle, and conflict policy |
| GOV → SPEC | Governed project scopes, enabled artifact vocabulary, and authoring constraints | Project-owned Requirement, Method, Evaluation, and Delivery authority |
| SPEC → REALIZATION | Complete applicable `RMED` Specification | Concrete realization and its traceability |
| REALIZATION → RELEASES | Assured realization and releasable outputs | Versioned release publications and views |
| RELEASES → FIELD | Published release output | Actual use, support, telemetry, incidents, and outcomes |

Every handoff declares entry criteria, exit criteria, and blocker behavior.
Adjacent handoffs are preferred. A direct forward skip is allowed only when
the intermediate layers have no meaningful transformation or ownership to add.
CAPRMEDIO does not create placeholder artifacts merely to simulate an unnecessary handoff.
