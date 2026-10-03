---
subjects:
  governs: "Artifact/Revision/Status"
  depends_on: []
version: 9
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-803
    - CA-R-804

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Resolve a lifecycle transition without activating inactive state

## Claim checked

A governed lifecycle move remains one observable subject change while inactive lifecycle states remain outside the active Artifact graph.

## Test case

Move one active Plan Atom byte-for-byte from its role root **to** the registered `done/` location, observe the before-path **and** after-path, **and** gather commit context against a fixture containing another already-done Plan **and** one solved Concern.

## Acceptance criteria

the adapter emits one unclassified trigger containing both paths. `COMMIT_CONTEXT` resolves one Plan identity **and** one `MOVE`, uses the committed active state as the prior result **and** the exact done carrier as the resulting state, **and** excludes **every** done **or** solved carrier from the active graph used for current authority **and** relation resolution.

## Failure disposition

Reject the delivery **if** the transition is suppressed because of its lifecycle directory, becomes two subjects, is classified from a hard-coded directory list, **or** admits an inactive carrier into current authority.
