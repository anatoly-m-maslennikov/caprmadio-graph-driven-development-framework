---
atom_id: CA-D-574
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 11:18:00 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Recovery checkpoint"
  depends_on: [Tool, Workflow, Step, Action, Journal, Manifest, Implementation, Permission]
relations:
  delivery_for: [CA-R-1525, CA-R-1720, CA-O-164]
---
# Summary

Serialize typed Release recovery checkpoints

## Scope

Private Release Version runtime state retained by the shared selected-execution progress writer for one frozen Workflow Run.

## Claim

Release Version recovery state **must** use **=1** closed, versioned JSON checkpoint per saved phase frontier, binding the exact frozen request, Workflow/Step/Action identities and definitions, phase observations, typed candidate/preflight/evidence and shared recording state to that Run.

## Details

1. the checkpoint is a private runtime carrier beside the existing selected request and Action progress in the configured orchestrator Run directory; it references the canonical Work Journal and is not another Journal.
2. its envelope contains a schema identifier, frozen-request digest, Run identity, phase frontier, typed state and canonical content digest. Typed state preserves the candidate, preflight compiler bytes, phase contexts/results and source-copy, compilation, suite, package, image, promotion and retirement evidence needed for continuation. A closed type allowlist admits only the existing named evidence models and primitive containers; bytes have an explicit reversible encoding.
3. no callable, image executor, credential or import instruction is stored. The program reinjects an admitted image executor separately; checkpoint data cannot select an executor or grant permission.
4. the shared writer saves an intent before an effect and observed state before terminal recording. Recovery retains the failed event identity and result/effect references, reopens the exact checkpoint and current definition bindings, and uses the existing canonical recorder for pending recording.
5. an unknown field/type, digest or identity mismatch, missing prerequisite, changed source, unresolved in-progress effect or missing recording proof returns an explicit blocked or pending result. Recovery never infers success from file presence, silently replays an uncertain effect or fabricates a Journal receipt.
6. a terminal Action result is reusable only with its exact durable shared receipt. A complete saved Workflow returns its original outcome without another effect or duplicate start/terminal event.
