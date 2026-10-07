---
atom_id: CA-D-575
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 22:43:16 +0000"
subjects:
  governs: "Tool/FRAMEWORK_INITIALIZATION/Runtime and Skill carriers"
  depends_on: [Tool, Framework Package, Runtime, Skill, Manifest, Docker Image, Journal]
relations:
  delivery_for: [CA-R-1881, CA-M-338]
---
# Summary

Bind initial Framework runtime and project Skill carriers

## Scope

The first content-addressed Framework package, active selector, and project-local Skill carriers.

## Claim

The first Framework package **must** occupy `.caprmedio_runtime/framework/releases/<manifest_sha256>/` with `manifest.toml`, `FRAMEWORK_ENGINE/`, compiler-current `METHODOLOGY/`, and `SKILLS/ca/`; `.agents/skills/ca/` **must** contain the same complete hook-free Skill payload before `.caprmedio_runtime/framework/current.toml` selects that package. A retained private bootstrap-image evidence carrier **must** prove a fixed isolated build context contains that exact package, its Docker build produced the selected immutable image ID, and its fixed complete-package/MCP canary executed against that ID. The evidence's inspected image has `org.caprmedio.framework.package_manifest_sha256` equal to that package manifest SHA-256 and `org.caprmedio.framework.source_context_sha256` equal to the manifest's sealed source-context SHA-256.

## Details

### Compiler-currentness proof

The compiler-currentness carrier contains the exact compiler input source-context digest, compiled-tree digest, compiler entrypoint identity, canonical compiled root, `source_snapshot_is_current` results before and after verification, complete zero-conflict selected frontier from canonical `compile_report`, and exact `projection_bytes` reconstruction from canonical `output_plan` for every compiled output at its planned `role_directory`/`basename` and source-relative path. The complete compiled-tree path set, payload hashes, generated-tree digest, source hashes, and metadata each equal that read-only reconstruction before package planning. An unresolved, conflict-dependent, colliding, or changed-snapshot selection rejects. This proves a current mechanical projection, not that a compiler Run occurred.

### Bootstrap-image proof and locations

The bootstrap-image evidence contains exactly the package manifest SHA-256, source-context SHA-256, immutable image digest, fixed-context digest, `bootstrap_proof_key`, canonical private proof location, canonical private fixed-context location, three immutable canonical command records, and canary result; `bootstrap_proof_key` is SHA-256 of canonical UTF-8 rows `(package_manifest_sha256, immutable_image_digest)`, ordered in that stated field order. The proof is at `.caprmedio_runtime/framework/bootstrap-image-evidence/<bootstrap_proof_key>/evidence.toml` and its fixed context at `.caprmedio_runtime/framework/bootstrap-image-evidence/<bootstrap_proof_key>/context/`; these private locations are derived, never caller inputs. It is private retained Tool evidence, never a D566 member, selector field, public request field, Workflow, Run, Journal schema, or mutable success flag.

### Fixed inputs and command-output carriers

Its context contains only the sealed package, the existing fixed `IMAGE_DOCKERFILE`, the exact sealed `pyproject.toml` and `uv.lock` rows required by that producer, and fixed canary carriers; every member is an enumerated sealed row. The records respectively cover build, immutable-ID inspection, and canary and each contains exact argv, exit status, start and finish times, plus exact relative paths and SHA-256 values for immutable byte carriers `commands/<build|inspect|canary>/stdout` and `commands/<build|inspect|canary>/stderr` beneath the proof root. The fixed build reuses the existing Release fixed canary and bounded pure build, command-record, and image-inspection primitives only where compatible with bootstrap labels; package-driven adapters may not invoke selected-N, candidate-suite, promotion, or retirement preconditions. The fixed build produces only a local immutable image ID: it applies exactly the two labels named in the Claim and neither tags, pushes, selects, nor deletes an image. The immutable-ID inspection and canary must independently match those labels and the package bytes.

### Selector and Journal intent

The initializer internally reopens the derived retained proof and re-inspects the image before an installation effect; it does not rerun producer effects. The selector identifies the manifest digest, selected release root, Framework Engine root, Methodology root, and immutable image ID. The canonical started-Run input remains `requested_run_id`, package-manifest SHA-256, sealed source-context SHA-256, and immutable image digest. A `requested_run_id` cannot start a changed intent: a changed binding permits only existing-Run inspection or recovery and creates neither another started evidence entry nor a second source ledger. The manifest's sealed source-context SHA-256 is the SHA-256 of canonical UTF-8 rows `(source_path, sha256, mode)`, ordered by `source_path`, for every inventoried package source. It is the sole activation carrier and is written only after a complete Skill publication; separate-directory writes are not treated as one atomic transaction. Package and Skill contents are regular, project-contained carriers with their manifest digests; no secret-shaped carrier, hook, global configuration, permanent bootstrap setting, source mutation, second registry, caller-selected build input, or image tag is delivered. The Action writes its actual installation started and terminal evidence only through the canonical Work Journal; runtime carriers and private image evidence do not become a second Journal.

### Bootstrap-to-N+1 compatibility

The subsequent Release Version reader keeps its regular N proof: a retained package manifest's `candidate_snapshot_manifest_sha256` equals selected N. The one first-install exception is not a success flag: it is proved only by the actual retained bytes. Its selector is closed to the first-install fields: integer `schema_version = 1`; `manifest_sha256` and `release` equal N; `selected_release_root`, `framework_engine_root`, and `methodology_root` are the exact N package and child paths; and `image_digest` is an immutable digest. The SHA-256 of that package's exact `manifest.toml` bytes equals N. In that exact shape only, the package manifest's `candidate_snapshot_manifest_sha256` is a lowercase 64-hex bootstrap sealed source-context SHA-256 and supplies N for the next N-to-N+1 workflow. Any absent, additional, inconsistent, or changed selector/package byte rejects prior ownership.
