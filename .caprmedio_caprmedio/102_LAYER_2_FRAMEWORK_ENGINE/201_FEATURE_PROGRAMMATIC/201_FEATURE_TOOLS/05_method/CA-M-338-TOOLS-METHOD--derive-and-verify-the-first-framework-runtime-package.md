---
atom_id: CA-M-338
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 16:58:11 +0400"
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

FRAMEWORK_INITIALIZATION **must** first reopen the exact source and canonical started-Run proof, then validate the empty state, construct and verify one sealed package, verify its immutable image binding, publish the complete `ca` Skill, atomically select the verified package as the final activation point, and finally append the terminal Action evidence through the sole canonical Journal writer.

## Details

1. Admit a canonical started Run only when its `requested_run_id`, package-manifest SHA-256, sealed source-context SHA-256, and immutable image digest form one exact intent. Reusing a `requested_run_id` with any changed intent member permits only existing-Run inspection or recovery; it does not create another started evidence entry or source ledger.
2. Reject a missing, ambiguous, stale, symlinked, non-directory, or already populated initialization boundary before an effect.
3. Inventory the current canonical Framework Engine, Methodology, and complete `ca` Skill without secrets or ephemeral tooling state; write **=1** manifest-addressed package under the declared runtime release root.
4. Reopen the package bytes and manifest, verify the complete hook-free Skill payload, and inspect one immutable Docker image. Its inspected immutable digest and its `org.caprmedio.framework.package_manifest_sha256` and `org.caprmedio.framework.source_context_sha256` labels must equal the started intent and the actual manifest and sealed source-context digests.
5. Publish the verified project-local Skill first. Atomically publish the selector last, only after the Skill is complete; the selector is the single activation point.
6. Record observed effects and the terminal result through the canonical Work Journal. A failed Skill publication, selector publication, or Journal append reports its actual state and does not replay an uncertain effect.

This Method does not select a Release Version candidate, promote or retire a Release Version image, change settings or authoring sources, register MCP, install hooks, or infer a source or image from mutable labels.
