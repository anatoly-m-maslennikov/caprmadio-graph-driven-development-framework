---
atom_id: CA-E-581
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-06 00:04:31 +0400"
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

The QA case **must** prove that an explicit initialization from an empty state creates exactly **=1** compiler-current complete manifest-addressed package, hook-free project-local `ca` Skill, selector, independently verified immutable bootstrap image, and canonical started/terminal Action Run evidence; every nonempty-state, partial, mismatched, stale, or label-only input case **must** stop without replacing an existing selection or Skill.

## Details

The success assertion requires `source_snapshot_is_current` before and after reopening canonical `compile_report` and `output_plan`, a complete zero-conflict selected frontier, and expected output reconstruction from exact `projection_bytes` at each planned `role_directory`/`basename` and source-relative path. It verifies the exact compiled-tree path set, payload hashes, generated-tree digest, source hashes, metadata, compiler entrypoint, and canonical root before reopening package bytes, manifest paths and digests, selector fields, `FRAMEWORK_ENGINE/`, `METHODOLOGY/`, the full `SKILLS/ca/` payload, and `.agents/skills/ca/`. It reopens the retained private bootstrap context, actual Docker build and immutable-ID inspection evidence, and fixed complete-package/MCP canary evidence, proving the exact manifest SHA-256 and source-context SHA-256 rather than labels alone. It verifies the derived private proof/context locations, the three immutable command records' exact argv, exit status, timing, and stdout/stderr SHA-256 values, and their exact fixed relative stdout/stderr byte-carrier paths under the proof root; the context admits only enumerated sealed rows, including `IMAGE_DOCKERFILE`, `pyproject.toml`, and `uv.lock`. It verifies reuse only of compatible Release primitives and no selected-N, candidate-suite, promotion, or retirement precondition. It verifies that the Skill is complete before selector publication, that the selector is the only activation point, and that the direct Action Journal contains the actual installation effects required by CA-O-180. Failure assertions cover stale, absent, partial, obsolete, source-mismatched, unresolved, conflict-dependent, colliding, or changed-snapshot compiled Methodology; preexisting selector, release, or Skill; file, symlink, non-directory, or nonempty initial carrier; incomplete package or Skill; unrelated or label-only image, tag, altered build context, failed canary, missing or mismatched image labels; missing/changed proof records, output bytes, or derived private location; selected-N, candidate-suite, promotion, or retirement precondition; Skill or selector publication failure; and Journal-terminal failure. Planning and startup must only read-verify preexisting compiled input/output evidence and must not run a compiler or build an image. A partial carrier may remain as explicit recovery evidence, but it cannot be selected as the active runtime or asserted as a completed installation.
