---
atom_id: CA-R-1821
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/source admission"
  depends_on: [Workflow, Action, Operator, Initiative, Journal, Tool, Implementation]
relations:
  relates_to: [CA-R-1094, CA-R-1525, CA-R-1720]
---
# Summary

Admit only current authorized selected-operation Runs

## Scope

The shared RUN_SUPPORT caller boundary for the thirteen selected CA-P-1117
requests. It is not a Workflow, source-discovery capability, or autonomous
dispatcher.

## Claim

RUN_SUPPORT **must** start an actual selected Workflow, Step, or Action Run
only from one explicit current selected-operation request and one current
Operator authorization in its sealed Initiative context.

## Details

- The request supplies one approved operation route and its typed parameters.
  It may also supply ordered exact expected definition revisions (Atom ID,
  kind, Version, safe repository-relative path, and sealed digest). RUN_SUPPORT
  resolves the route only through the current selected-source registry and
  returns the exact admitted bindings; it does not infer a route from a Tool
  name, directory, prompt, or earlier result.
- The selected source must be one of CA-P-1117's thirteen requested routes or
  an actual Action bound by one of those routes. A generic Rebuild Projections
  route remains a shortcut to its selected builders, not a fourteenth Run.
- Every actual Run carries the one sealed Initiative required by CA-R-1094,
  including its stable identity, human-instruction summary, and safe reference
  when one exists, plus the explicit sealed Operator authorization covering
  that route/effect. A worker, session, queue, MCP call, or Journal partition
  is not a substitute Initiative or authorization.
- Before dispatch and before recovery of remaining work, resolve the selected
  source, check its Version and digest, current permission, current Operator
  authorization, and mutable input/target freshness. A changed, withdrawn,
  unavailable, unauthorized, or stale source pauses the request for recorded
  revalidation; it must not substitute the newest definition or reuse an old
  approval.
- Preview, refusal, and a request denied before any execution return an
  explicit non-start disposition. They create neither a Workflow/Step/Action
  Run nor fabricated Journal execution evidence. Execute mode is explicit;
  receipt observation, status polling, recovery, and a Tool call do not start
  another Run.
