---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "PROGRAMMATIC/temporary execution state"
  depends_on:
    - "programmatic software"
llm_session_ids:
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
version: 5
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-R-1473
    - CA-M-289
atom_id: CA-E-467
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Reject temporary state outside project temp

## Claim checked

**every** CAPRMEDIO-controlled PROGRAMMATIC execution **must** confine temporary Carriers created by its components **and** configured dependencies **to** the Project Temporary State root.

## Test case

1. set the working directory **and** ambient host temporary location outside the configured Project Temporary State root.
2. run representative Tool, App backend, **and** MCP fixtures, including their test runner **and** a configured dependency. exercise bytecode creation, caches, temporary workspaces, atomic staging, **and** interrupted **or** denied cleanup.
3. compare the path frontier outside the Temporary State root **before** **and** **after** execution. inspect the applicable source **and** configuration for unredirected temporary-path creation.
4. delete **only** the Temporary State root **in** an isolated fixture **and** compare its protected authority **and** runtime state.
5. make the Temporary State root unavailable **or** make the selected staging
   path fail the same-filesystem precondition **in** an isolated fixture.
   inspect the affected effect **and** its boundary diagnostic.

## Acceptance criteria

**all** of the following **must** hold:

- **every** temporary, scratch, staging, cache, build, Evaluation, **and** cleanup-remnant Carrier is below the configured Project Temporary State root.
- concurrent owners use their declared component **or** run-specific descendants.
- no applicable source **or** configuration uses an ambient **or** hard-coded host temporary fallback.
- deletion of the Temporary State root leaves governed authority, Project Journal history, selected runtime releases, logs, sessions, databases, service state, **and** resumable state unchanged.
- no Python bytecode cache remains below the Runtime State root.
- an unavailable temporary root **or** unsatisfied same-filesystem precondition
  stops the affected effect **and** produces a stable diagnostic identifying
  the creating owner **and** violating path.

## Failure disposition

reject the changed component, test workflow, dependency configuration, **or** release **until** **every** observed **and** statically detectable temporary Carrier uses the Project Temporary State root. report **every** violating path **and** its creating owner.
