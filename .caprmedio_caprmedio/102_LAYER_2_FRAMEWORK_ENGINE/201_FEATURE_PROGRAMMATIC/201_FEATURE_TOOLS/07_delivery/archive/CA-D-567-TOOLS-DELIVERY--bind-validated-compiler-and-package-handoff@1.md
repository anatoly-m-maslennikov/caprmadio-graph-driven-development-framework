---
atom_id: CA-D-567
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:58:19 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Validated compiler and package handoff"
  depends_on: [Tool, Manifest, Digest, Methodology, Projection, Installation, Runtime]
relations:
  delivery_for: [CA-R-1877, CA-R-1878, CA-R-1879, CA-M-332, CA-M-333]
---
# Summary

Bind validated compiler and package handoff

## Scope

The internal trusted handoff from a validated sealed candidate and successful compiler output to future package staging.

## Claim

Release Version **must** admit package staging only from one typed internal `SealedCandidateCompilation`, constructed from locally observed current selections, authority bytes, source inventory, and successful compiler output after the D566 manifest checksum and every sealed binding validate; it **must not** trust caller-provided gates, raw authority mappings, package rows, source permissions, or success evidence.

## Details

`SealedAuthority` is internal context, never a request member. It contains the locally read executing release selection, candidate release identity, canonical source snapshot digest, Project Structure digest, Framework Settings digest, source-frontier digest, nested-source recursive digest, and expected D566 manifest SHA-256. Currentness is established by those local facts and exact comparisons, not by caller assertion or refresh-in-place.

Before compiler or package staging, the internal handoff records the safe derived source-copy root and `actual_derived_source_copy_sha256` from the complete delivered copy, then requires equality with D566's `expected_derived_source_copy_sha256`; a missing, partial, mismatched, stale, or uncertain copy blocks both stages. After a successful compiler invocation, `SealedCandidateCompilation` contains exactly the validated `candidate_snapshot_manifest_sha256`, the `SealedAuthority` binding, source-copy root, expected and actual derived-source-copy SHA-256 values, compiler entrypoint identity, compiler frontier digest, `expected_compiled_output_sha256`, `actual_compiled_output_sha256`, child materialization root, and destination-ordered `package_rows`. `actual_compiled_output_sha256` is captured from the compiler's materialized bytes only after that effect succeeds and must equal the manifest expectation; its absence, mismatch, compiler failure, stale local input, or uncertain result blocks staging. It is not required, inferred, or prefilled by the candidate manifest.

Each derived `package_row` has `resource`, safe repository-relative `source_path`, safe package-relative `destination_path`, actual `sha256` from the locally read source bytes, and `mode` from that source file's observed `stat().st_mode & 0o777`. The package adapter re-reads each source immediately before copy and requires both digest and observed mode to match the handoff; it never accepts a caller permission override. The rows must cover the complete D562 Framework package and D563 `ca` payload, remain uniquely destination-bound, and preserve N while staging retained N+1.

The handoff is an internal validation boundary, not a claim of compiler, package, installation, image, promotion, retirement, or Journal success. It preserves D561's canonical authority and nested source subtree byte-for-byte: source-to-derived copy never becomes an authority switch, source-ancestor replacement, or permitted mutation.
