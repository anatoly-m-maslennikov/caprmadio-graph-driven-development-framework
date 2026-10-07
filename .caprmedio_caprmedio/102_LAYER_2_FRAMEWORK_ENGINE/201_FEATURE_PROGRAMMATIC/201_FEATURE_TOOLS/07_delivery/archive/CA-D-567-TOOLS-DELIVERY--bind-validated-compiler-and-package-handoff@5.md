---
atom_id: CA-D-567
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-06 20:26:51 +0000"
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

The completed `SealedSourceCopy` handoff is also the predecessor-only source-copy proof when a later phase fails, blocks, or remains unpromoted. Its fixed source-copy target is exactly `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`; the proof must bind the old frozen candidate manifest, expected and actual old copy SHA-256 values, the same executing N, and a complete old-tree inventory of safe fixed-path files, bytes/SHA-256 values, and modes. The proof is usable only after the canonical Journal record and the exact Action/Run and CA-D-574 sealed checkpoint/proof are authenticated; arbitrary retained JSON, a missing/unrecorded proof, unknown member, tampered bytes, unsafe path, mode drift, or identity/wrong-N mismatch is a strict block. This predecessor proof does not authorize a new candidate, reuse old output, or replay old authorization. A new candidate independently revalidates its current source/settings/frontier/authority and performs the normal fresh copy, requiring its new actual copy SHA-256 to equal its new expected value; old and new source/frontier/settings digests are not required to match.

## Details

`SealedAuthority` is internal context, never a request member. It contains the locally read executing release selection, candidate release identity, canonical source snapshot digest, Project Structure digest, Framework Settings digest, source-frontier digest, nested-source recursive digest, and expected D566 manifest SHA-256. Currentness is established by those local facts and exact comparisons, not by caller assertion or refresh-in-place.

Before compiler or package staging, the internal handoff records the safe derived source-copy root and `actual_derived_source_copy_sha256` from the complete delivered copy, then requires equality with D566's `expected_derived_source_copy_sha256`; a missing, partial, mismatched, stale, or uncertain copy blocks both stages. After a successful compiler invocation, `SealedCandidateCompilation` contains exactly the validated `candidate_snapshot_manifest_sha256`, the `SealedAuthority` binding, source-copy root, expected and actual derived-source-copy SHA-256 values, compiler entrypoint identity, compiler frontier digest, `expected_compiled_output_sha256`, `actual_compiled_output_sha256`, child materialization root, and destination-ordered `package_rows`. `actual_compiled_output_sha256` is captured from the compiler's materialized bytes only after that effect succeeds and must equal the manifest expectation; its absence, mismatch, compiler failure, stale local input, or uncertain result blocks staging. It is not required, inferred, or prefilled by the candidate manifest.

Each derived `package_row` has `resource`, safe repository-relative `source_path`, safe package-relative `destination_path`, actual `sha256` from the locally read source bytes, and `mode` from that source file's observed `stat().st_mode & 0o777`. The package adapter re-reads each source immediately before copy and requires both digest and observed mode to match the handoff; it never accepts a caller permission override. The rows must cover the complete D562 Framework package and D563 `ca` payload, remain uniquely destination-bound, and preserve N while staging retained N+1.

The handoff is an internal validation boundary, not a claim of compiler, package, installation, image, promotion, retirement, or Journal success. It preserves D561's canonical authority and nested source subtree byte-for-byte: source-to-derived copy never becomes an authority switch, source-ancestor replacement, or permitted mutation.

### Current predecessor trust registrations

Under the existing CA-P-1117 autonomy envelope, Release Version may admit historical source-delivery evidence prospectively through this source-authoritative private carrier. It is a current admission, not retroactive sealing and not proof that mutable bytes were unchanged at the historical run time. The following fenced object is the one locally verified N13 registration, retained as current evidence:

```json
{
  "schema_version": 1,
  "registrations": [
    {
      "action_result_path": ".caprmedio_install/workflow_orchestrator/runs/release-epic-resume-20261006-N13/release-epic-resume-20261006-N13:step:3:action:1.json",
      "action_result_sha256": "c987d48feaa14ae96359d2dfc48a881bab3235171f80e1220983d0a89555c681",
      "actual_derived_source_copy_sha256": "006b9a62f9369dfa716cc14c16f652fab81075ad6b97aaf9c49b904db427b207",
      "authorization_ref": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md",
      "basis": "current admission of historical delivery evidence",
      "candidate_snapshot_manifest_sha256": "1945f7bf7b02b8550c04a39b57d6e39ead4a4ea3a45b317f4580a7d0bf3713f3",
      "checkpoint_path": ".caprmedio_install/workflow_orchestrator/runs/release-epic-resume-20261006-N13/release_action_run.json",
      "checkpoint_sha256": "2e6de8f08a25c9859c987688b934eb961ae2c5f08969c9880d50195db6d915f2",
      "effect_ref": "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources#sha256=006b9a62f9369dfa716cc14c16f652fab81075ad6b97aaf9c49b904db427b207",
      "event_digest": "df1285a2c385c8203b09ef98a72620a6db674ab121e7c1655a6aec65d62426b4",
      "event_id": "event-86d57f70-db81-4884-b98f-540d082b9a09",
      "executing_release": "6f2e3a615a4f4d6da0f16831800f9e4b7ff84f89b89faeefc359f51711d28c57",
      "expected_derived_source_copy_sha256": "006b9a62f9369dfa716cc14c16f652fab81075ad6b97aaf9c49b904db427b207",
      "journal_path": ".caprmedio_caprmedio/_journal/run-support-2026-10-06-part-3.ndjson",
      "persistent_inventory_sha256": "d55b798c51811e02acfdfe4f3f82e00109e978ec55eca21da47244d6ee4dc6f8",
      "registered_at": "2026-10-06T20:26:51Z",
      "registration_id": "current-n13-source-copy-20261006",
      "source_copy_root": "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources"
    }
  ]
}
```

The current reader accepts only an object with exactly `schema_version` and `registrations`, exact integer `schema_version = 1`, and exactly one applicable record with no missing or unknown member. The record keys are exactly `registration_id`, `basis`, `authorization_ref`, `registered_at`, `journal_path`, `event_id`, `event_digest`, `effect_ref`, `action_result_path`, `action_result_sha256`, `checkpoint_path`, `checkpoint_sha256`, `candidate_snapshot_manifest_sha256`, `executing_release`, `source_copy_root`, `expected_derived_source_copy_sha256`, `actual_derived_source_copy_sha256`, and `persistent_inventory_sha256`. `basis` must equal `current admission of historical delivery evidence`; all referenced paths must be safe, the executing release must equal current N, and `source_copy_root` must be exactly `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`. Every pinned byte/value is re-read and must have exactly one current authoritative match across the authorization, Journal event, Action result, CA-D-574 checkpoint, candidate manifest, occupied source-copy tree, and inventory; lowercase 64-hex digests and current modes are required. Malformed, unknown, duplicate, ambiguous, tampered, wrong-N, stale, or unsafe records are refused.

`persistent_inventory_sha256` is the SHA-256 of canonical UTF-8 bytes from `json.dumps(..., sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')` with no newline, using exactly `{"directories":[{"path":...,"mode":...}],"files":[{"path":...,"mode":...,"sha256":...}]}`; both arrays are sorted by path, every decimal `mode` is `stat().st_mode & 0o777`, directories include `.` and every non-transient directory including empty directories, and the shared Release inventory exclusions apply while symlinks and special entries are refused. The current inventory must revalidate the registered expected and actual source-copy values; otherwise the registration is blocked. This registration only permits retaining or replacing exactly the occupied predecessor copy during a new candidate's independent current sealing and normal fresh delivery. It never authorizes reuse, replay, or promotion of old output or authorization, and it adds no public request, route, graph, or Journal schema member.
