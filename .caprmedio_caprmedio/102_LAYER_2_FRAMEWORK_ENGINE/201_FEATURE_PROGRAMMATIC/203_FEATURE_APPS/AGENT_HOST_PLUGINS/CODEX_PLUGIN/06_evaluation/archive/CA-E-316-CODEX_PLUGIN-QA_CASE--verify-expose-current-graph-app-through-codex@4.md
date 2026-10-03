---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - graph-app-access
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-198
---
# Verify expose the current graph_app through codex

## Claim checked

CA-M-198 exposes current GRAPH_APP state through Codex as an attributable read-only view with explicit stale and unavailable states.

## Applicable when

Apply before accepting any Codex plugin release that exposes Project Graph browsing.

## Test case

Compare the Codex viewing response for one governed-filtered node under three bounded GRAPH_APP states: a current source frontier, the same source carrier changed after the graph state was derived, and an unavailable source frontier. Retain the relevant source, graph-state, and repository digests before and after each view.

## Acceptance criteria

The current view returns navigation, the applied governed filter, node content, exact source path, digest, and provenance; the changed-source view reports stale state rather than presenting old content as current; the unavailable view reports its unavailable state; and viewing changes no Atom, Journal, Projection, graph source, or derived GRAPH_APP state.

## Failure disposition

Reject the Codex exposure and preserve the three GRAPH_APP states, selected-node responses, filter evidence, stale and unavailable handling, and before-and-after mutation evidence.
