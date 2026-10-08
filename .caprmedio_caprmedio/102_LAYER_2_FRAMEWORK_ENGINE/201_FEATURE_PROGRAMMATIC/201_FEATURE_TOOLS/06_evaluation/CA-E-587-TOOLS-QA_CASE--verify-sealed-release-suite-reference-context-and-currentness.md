---
atom_id: CA-E-587
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-06 11:53:59 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Sealed suite reference-context QA"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Project Structure, Operator, Workflow, Action, Source Carrier, Digest, JUnit Report]
relations:
  evaluation_for: [CA-R-1887, CA-M-344, CA-D-580, CA-D-579]
---
# Summary

Verify sealed Release-suite reference context and currentness

## Scope

Positive and refusal checks for private control-reference capture, read-only workspace copying, and post-run revalidation.

## Claim

The QA case **must** prove that the Suite Owner passes only with one exact, allowlisted, read-only reference closure bound to the trusted candidate, compiled root, selected N, and image context; every changed or injected control reference is non-passing.

## Details

Verify a positive closure containing selected-workflow bindings, Operator registry, Project settings, Project Structure, resolved source-registry reference, CA-D-572, its transitive pins, the selected-manifest source-path closure, and both exact D580 Prompt binding frontiers. Assert typed source-path ordering, exact byte SHA-256 and mode verification, canonical `control_context_digest`, workspace copy preservation, and its inclusion in actual suite evidence and the schema-2 envelope. Each explicit Prompt source pin is current and materialized; identical shared pins occur once.

Independently reject an empty, duplicate, unknown, caller-added, runtime, Journal, secret-shaped, absolute, escaping, symlinked, non-regular, unreadable, wrong-mode, stale-digest, or stale-source-registry row. Mutate each allowed root and a transitive D572 pin between capture and execution, and again between execution and rederivation; neither case may pass or replay. Reject candidate SHA, compiled-root, selected-N, or image-context mismatch. Verify no arbitrary caller file reaches the workspace, no control carrier is written, and failure retains N and truthful non-passing evidence.

Reject an unknown Prompt binding carrier, changed binding bytes, missing or stale Atom pin, duplicate source declaration and conflicting shared pin. Mutate a binding and one referenced Prompt Atom before execution and before post-run rederivation; neither may pass. Verify the unchanged schema-1 reference context and retained N proof remain readable, without admitting obsolete Plan carriers or expanding to an entire Project folder.
