---
atom_id: CA-D-566
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:58:19 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate snapshot manifest encoding"
  depends_on: [Tool, Manifest, Digest, Artifact, Revision, Project Structure, Framework Settings]
relations:
  delivery_for: [CA-R-1876, CA-R-1877, CA-R-1878, CA-R-1879, CA-M-331, CA-M-332]
---
# Summary

Encode sealed candidate Snapshot Manifest

## Scope

The canonical, effect-free `candidateSnapshotManifest` representation and its candidate identity digest.

## Claim

Release Version **must** encode one `caprmedio.release_version.candidate.v2` `candidateSnapshotManifest` as canonical UTF-8 JSON with object keys sorted, compact separators, `ensure_ascii=false`, and `allow_nan=false`; it **must** normalize every row in ascending `(destination_path, source_path, source_sha256)` order and set `sha256` to the lowercase SHA-256 of that normalized object with its own `sha256` member omitted.

## Details

The manifest has exactly these top-level members: `schema`, `sha256`, `executing_release`, `candidate_release`, `canonical_source_snapshot_ref`, `canonical_source_snapshot_digest`, `project_structure_digest`, `framework_settings_digest`, `source_frontier_digest`, `nested_source_recursive_sha256_before`, `expected_derived_source_copy_sha256`, `expected_compiled_output_sha256`, `full_suite_environment`, `skill_target`, `candidate_image`, and `source_inventory_rows`. `expected_derived_source_copy_sha256` and `expected_compiled_output_sha256` are future-output expectations only; no `actual_*_sha256`, successful gate, installed selection, image execution, or after-effect source digest belongs in this pre-effect manifest.

`source_inventory_rows` is the complete actual candidate input inventory, not an Engine-Tools subset. Each row has exactly `resource` (`FRAMEWORK_ENGINE`, `METHODOLOGY`, `SKILL`, or `IMAGE_INPUT`), safe repository-relative `source_path`, lowercase 64-hex `source_sha256`, `source_mode`, and safe package-relative `destination_path`. `source_mode` is the observed source permission bits masked to `0o777`; it is not caller-selected policy. Rows include all selected Framework Methodology source delivery files, required Engine components, every canonical `ca` Skill payload file, and candidate image inputs. Destination paths are unique; all input paths, digests, and modes are obtained from the locally read sealed snapshot before this encoding.

`full_suite_environment` has `runner`, nonempty ordered `command`, and safe `working_directory`; `skill_target` is `.agents/skills/ca`; and `candidate_image` has the fixed Dockerfile path, its source digest, and a bounded candidate reference. The manifest may name D561's source-copy and child-materialization plan, but never changes canonical authority, replaces a source ancestor, or treats a derived copy as the source root. It is untrusted request data until D567's locally derived authority and compilation handoff validate it.
