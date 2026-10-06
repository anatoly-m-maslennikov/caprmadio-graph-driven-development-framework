---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Evidence"
  depends_on:
    - "Artifact/Revision"
    - "Atom/Content Role: Implementation"
    - "Projection"
    - "Carrier"
version: 14
updated_at: "2026-09-18 14:16:20 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  resolution_of:
    - "CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented"
  relates_to:
    - "CA-D-329"
---
# Bind proof records to dependency frontiers

**every** governed proof record **must** bind its observation **to** the exact applicable inputs under which it was produced.

- the binding includes the relevant Artifact **and** Implementation Revisions, configuration, evaluators, environments, **and** material inputs; CA-D-329 governs its representation.
- reliance on that observation for a current candidate requires a matching input binding **and** satisfaction of its additional governing invalidation conditions.
- a changed material input makes the affected proof stale for that candidate **until** the required checks run against the changed inputs. a missing **or** unresolved binding is unknown, **not** current.
- an unrelated change does **not** invalidate proof **unless** it changes the evaluated dependencies **or** satisfies an additional governing invalidation condition.
- retain the historical record unchanged. neither a recent timestamp **nor** a refreshed Projection alone proves currentness.

this rule applies independently of the selected Workflow, release policy, **or** version-control mechanism.
