---
atom_id: CA-D-575
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 16:58:11 +0400"
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

The first Framework package **must** occupy `.caprmedio_runtime/framework/releases/<manifest_sha256>/` with `manifest.toml`, `FRAMEWORK_ENGINE/`, `METHODOLOGY/`, and `SKILLS/ca/`; `.agents/skills/ca/` **must** contain the same complete hook-free Skill payload before `.caprmedio_runtime/framework/current.toml` selects that package. Docker inspection **must** show the selected immutable image ID carries `org.caprmedio.framework.package_manifest_sha256` equal to that package manifest SHA-256 and `org.caprmedio.framework.source_context_sha256` equal to the manifest's sealed source-context SHA-256.

## Details

The selector identifies the manifest digest, selected release root, Framework Engine root, Methodology root, and immutable image ID. The canonical started-Run input binds `requested_run_id`, package-manifest SHA-256, sealed source-context SHA-256, and immutable image digest. A `requested_run_id` cannot start a changed intent: a changed binding permits only existing-Run inspection or recovery and creates neither another started evidence entry nor a second source ledger. The manifest's sealed source-context SHA-256 is the SHA-256 of canonical UTF-8 rows `(source_path, sha256, mode)`, ordered by `source_path`, for every inventoried package source. It is the sole activation carrier and is written only after a complete Skill publication; separate-directory writes are not treated as one atomic transaction. Package and Skill contents are regular, project-contained carriers with their manifest digests; no secret-shaped carrier, hook, global configuration, permanent bootstrap setting, source mutation, or second registry is delivered. The Action writes its started and terminal evidence only through the canonical Work Journal; runtime carriers do not become a second Journal.

### Bootstrap-to-N+1 compatibility

The subsequent Release Version reader keeps its regular N proof: a retained package manifest's `candidate_snapshot_manifest_sha256` equals selected N. The one first-install exception is not a success flag: it is proved only by the actual retained bytes. Its selector is closed to the first-install fields: integer `schema_version = 1`; `manifest_sha256` and `release` equal N; `selected_release_root`, `framework_engine_root`, and `methodology_root` are the exact N package and child paths; and `image_digest` is an immutable digest. The SHA-256 of that package's exact `manifest.toml` bytes equals N. In that exact shape only, the package manifest's `candidate_snapshot_manifest_sha256` is a lowercase 64-hex bootstrap sealed source-context SHA-256 and supplies N for the next N-to-N+1 workflow. Any absent, additional, inconsistent, or changed selector/package byte rejects prior ownership.
