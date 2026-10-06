---
atom_id: CA-M-338
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-06 00:04:31 +0400"
subjects:
  governs: "Tool/FRAMEWORK_INITIALIZATION/Package derivation"
  depends_on: [Tool, Framework Package, Runtime, Methodology, Skill, Docker Image, Journal]
relations:
  method_for: [CA-R-1881]
---
# Summary

Derive and verify the first Framework runtime package

## Scope

The bounded construction and admission of one first active Framework package.

## Claim

FRAMEWORK_INITIALIZATION **must** first read-verify a current canonical compiled Methodology and a complete privately produced bootstrap-image evidence carrier, then reopen the exact source and canonical started-Run proof, validate the empty state, construct and verify one sealed package, verify that carrier's immutable image binding, publish the complete `ca` Skill, atomically select the verified package as the final activation point, and finally append the terminal Action evidence through the sole canonical Journal writer.

## Details

1. Before planning, read-verify preexisting canonical Methodology input and compiled-output evidence against the current canonical Methodology source root. Require `source_snapshot_is_current` before and after the read; reopen canonical `compile_report` and `output_plan`, require zero conflicts and a complete selected frontier, and reconstruct every expected compiled output from its exact `projection_bytes` at the `role_directory`/`basename` and source-relative path prescribed by that plan. Require the complete compiled-tree path set, payload hashes, generated-tree digest, source hashes, and metadata to match that reconstruction, the compiler entrypoint identity, canonical compiled root, and current input frontier. Refuse a missing, stale, partial, symlinked, obsolete, unresolved, conflict-dependent, colliding, or changed-snapshot selection. This proves a current mechanical projection without asserting a compiler Run occurred. Planning neither runs the compiler nor publishes a runtime, Skill, selector, or image.
2. Inventory the current Framework Engine, read-only-currentness-proven Methodology source and compiled carriers, and complete `ca` Skill without secrets or ephemeral tooling state. Seal their ordered bytes and modes into one manifest-addressed package plan and source-context SHA-256.
3. The private bootstrap-image producer builds only a local immutable image ID from a fixed isolated context containing that sealed package, the existing fixed `IMAGE_DOCKERFILE`, and the exact sealed `pyproject.toml` and `uv.lock` rows required by that producer, plus required fixed canary carriers. Every context member is an enumerated sealed row; no other host file is readable by the build or canary. It reuses the existing Release fixed canary and bounded pure build, command-record, and image-inspection primitives only where compatible with the bootstrap labels; package-driven adapters must not invoke selected-N, candidate-suite, promotion, or retirement preconditions. It uses no caller path, tag, label, Dockerfile, command, network, or package override; it neither tags, pushes, selects, nor deletes an image. It retains immutable canonical command records for the actual build, immutable-ID inspection, and fixed complete-package/MCP canary: exact argv, exit status, start and finish times, and stdout/stderr SHA-256 values bound to retained immutable stdout and stderr byte carriers at fixed relative paths under the derived proof root. The canary must prove the exact immutable ID and package manifest and source-context binding; it must not merely echo labels.
4. Derive `bootstrap_proof_key` from the exact package-manifest SHA-256 and immutable image digest, and retain the proof and fixed context only at their canonical private location keyed by that value. Admit a canonical started Run only after internally reopening that exact retained proof and re-inspecting the image; neither proof nor context location is a caller input. Its existing `requested_run_id`, package-manifest SHA-256, sealed source-context SHA-256, and immutable image digest form one exact intent. Reusing a `requested_run_id` with any changed intent member permits only existing-Run inspection or recovery; it does not create another started evidence entry or source ledger. The producer is not implicit in planning, startup, or this Action and does not change CA-O-180's explicit image input.
5. Reject a missing, ambiguous, stale, symlinked, non-directory, or already populated initialization boundary before an installation effect. Reopen the package bytes and manifest, verify the complete hook-free Skill payload, and verify the retained image evidence plus its inspected immutable digest and exact `org.caprmedio.framework.package_manifest_sha256` and `org.caprmedio.framework.source_context_sha256` labels against the started intent and actual plan.
6. Publish the verified project-local Skill first. Atomically publish the selector last, only after the Skill is complete; the selector is the single activation point.
7. Record observed package, Skill, selector, and terminal installation result effects through the canonical Work Journal as CA-O-180 requires. A failed Skill publication, selector publication, or Journal append reports its actual state and does not replay an uncertain effect. The separate producer retains its own actual build/inspect/canary evidence and never publishes or removes a runtime, Skill, selector, or image.

This Method does not select a Release Version candidate, require an existing N, promote or retire a Release Version image, change settings or authoring sources, register MCP, install hooks, create a selected-workflow route, or infer a source or image from mutable labels.
