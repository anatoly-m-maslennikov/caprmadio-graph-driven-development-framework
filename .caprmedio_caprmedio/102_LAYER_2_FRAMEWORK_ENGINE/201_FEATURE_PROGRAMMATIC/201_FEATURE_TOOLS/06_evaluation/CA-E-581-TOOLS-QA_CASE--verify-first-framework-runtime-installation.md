---
atom_id: CA-E-581
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 16:34:05 +0400"
subjects:
  governs: "Tool/FRAMEWORK_INITIALIZATION/Installation QA"
  depends_on: [Tool, Framework Package, Runtime, Methodology, Skill, Docker Image, Journal]
relations:
  evaluation_for: [CA-R-1881, CA-M-338, CA-D-575]
---
# Summary

Verify first Framework runtime installation

## Scope

One empty Project fixture and its accepted initial runtime installation.

## Claim

The QA case **must** prove that an explicit initialization from an empty state creates exactly **=1** complete manifest-addressed package, hook-free project-local `ca` Skill, selector, immutable image binding, and canonical started/terminal Action Run evidence; every nonempty-state, partial, mismatched, or stale-input case **must** stop without replacing an existing selection or Skill.

## Details

The success assertion reopens package bytes, manifest paths and digests, selector fields, `FRAMEWORK_ENGINE/`, `METHODOLOGY/`, the full `SKILLS/ca/` payload, `.agents/skills/ca/`, the inspected immutable image identity, its exact `org.caprmedio.framework.package_manifest_sha256` and `org.caprmedio.framework.source_context_sha256` labels, and canonical Journal identities. It verifies that the Skill is complete before selector publication and that the selector is the only activation point. Failure assertions cover preexisting selector, release, or Skill; file, symlink, non-directory, or nonempty initial carrier; incomplete package or Skill; changed source; missing or mismatched image labels; Skill or selector publication failure; and Journal-terminal failure. A partial carrier may remain as explicit recovery evidence, but it cannot be selected as the active runtime or asserted as a completed installation.
