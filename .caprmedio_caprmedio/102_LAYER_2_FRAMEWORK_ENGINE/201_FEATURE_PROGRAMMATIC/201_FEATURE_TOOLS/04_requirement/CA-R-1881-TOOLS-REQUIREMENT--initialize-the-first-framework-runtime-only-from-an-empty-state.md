---
atom_id: CA-R-1881
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 16:34:05 +0400"
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

FRAMEWORK_INITIALIZATION **must** create the first active Framework runtime only when `.caprmedio_runtime/framework/current.toml` is absent and `.caprmedio_runtime/framework/releases/` and `.agents/skills/ca/` are each absent or an empty regular directory. It **must** derive **=1** complete content-addressed Framework package, hook-free project-local `ca` Skill, current selector, and verified immutable image binding from the same sealed source frontier and record the actual Action Run through the canonical Work Journal.

## Details

An existing selector, retained release, project-local Skill, file, symlink, non-directory, nonempty directory, partial state, changed source, incomplete package, mismatched image, unavailable permission, or missing canonical Journal proof stops without overwrite. The selected package contains Framework Engine, Methodology, and the full `ca` Skill payload. Docker inspection must prove the image's immutable ID carries `org.caprmedio.framework.package_manifest_sha256` equal to the package manifest SHA-256 and `org.caprmedio.framework.source_context_sha256` equal to that manifest's sealed source-context SHA-256. This initial installation is explicitly Operator-invoked; it is neither a selected-workflow route nor an N-to-N+1 Release Version promotion. It preserves authoring sources, settings, Journals, unrelated Skills, and existing images. A partial effect remains an actual blocked or partial result; it never becomes an active selection or a claimed initialized runtime.
