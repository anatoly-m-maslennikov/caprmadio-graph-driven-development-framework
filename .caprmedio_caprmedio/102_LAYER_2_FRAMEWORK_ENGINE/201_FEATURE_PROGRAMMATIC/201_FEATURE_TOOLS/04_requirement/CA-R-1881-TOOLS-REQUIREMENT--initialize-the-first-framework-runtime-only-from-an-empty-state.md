---
atom_id: CA-R-1881
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-06 00:04:31 +0400"
subjects:
  governs: "Tool/FRAMEWORK_INITIALIZATION/Empty-state installation"
  depends_on: [Tool, Framework Package, Runtime, Skill, Docker Image, Journal, Operator]
relations:
  relates_to: [CA-R-1873, CA-R-1877, CA-R-1878, CA-R-1879, CA-R-1525, CA-R-1720]
---
# Summary

Initialize the first Framework runtime only from an empty state

## Scope

One explicit first installation of the full Framework runtime and the project-local `ca` Skill.

## Claim

FRAMEWORK_INITIALIZATION **must** create the first active Framework runtime only when `.caprmedio_runtime/framework/current.toml` is absent and `.caprmedio_runtime/framework/releases/` and `.agents/skills/ca/` are each absent or an empty regular directory. It **must** admit only a canonical-compiled Methodology current with its source frontier and **=1** complete content-addressed Framework package, hook-free project-local `ca` Skill, current selector, and independently verified immutable bootstrap image built from that same sealed package frontier; it records the actual installation Action Run through the canonical Work Journal.

## Details

An existing selector, retained release, project-local Skill, file, symlink, non-directory, nonempty directory, partial state, changed source, stale or unproven canonical compiled Methodology, incomplete package, mismatched image, unavailable permission, or missing canonical Journal proof stops without overwrite. The selected package contains Framework Engine, current Methodology source and compiled carriers, and the full `ca` Skill payload. Before the installation Action may publish a Skill or selector, a private bootstrap-image producer must construct a fixed isolated context from the sealed package, build and inspect one immutable image ID, and run the fixed complete-package and executable MCP canary against that exact ID. The build, inspect, and canary evidence must bind the exact package manifest SHA-256 and sealed source-context SHA-256; labels alone, an unrelated image, a tag, or a caller assertion do not prove the image. This producer is a separate private prerequisite: planning and startup only read-verify preexisting compiled input/output evidence by reconstructing expected projection bytes from the complete current conflict-free selected frontier, with source-snapshot currentness before and after that read; they do not run a compiler or build an image. The existing explicit `image_digest` input and CA-O-180 Action order remain unchanged. This initial installation is explicitly Operator-invoked; it is neither a selected-workflow route nor an N-to-N+1 Release Version promotion. It preserves authoring sources, settings, Journals, unrelated Skills, and existing images. A partial effect remains an actual blocked or partial result; it never becomes an active selection or a claimed initialized runtime.
