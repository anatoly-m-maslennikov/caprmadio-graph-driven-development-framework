---
atom_id: CA-D-588
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 17:27:56 +0000"
subjects:
  governs: "MCP/selected source pin refresh"
  depends_on: [MCP, Projection, Workflow, Action, Operator, Journal, Atom, Source Carrier]
relations:
  relates_to: [CA-P-1800]
---
# Summary

Register the prepared successor binding refresh

## Scope

the exact admitted selected-source revision refresh under the current Epic.

## Claim

the selected-source refresh registration **must** use the closed serialization below for this exact prepared-successor authority revision.

## Details

the **only** registration is the JSON object under `### Accepted source revision`. its keys and nested pin shapes are exact; duplicate or unknown fields are invalid. version, occurrence count and schema version are strict integers. paths are safe regular Project-relative carriers with no symlink ancestry.

the current Requirement and Action pins, exact prior Action archive and exact input binding bytes **must** all match. the eight old pin occurrences appear **only** in the four listed existing routes. no other route field, admission, registry pin or graph edge is replaced. the refreshed candidate retains the existing canonical schema and recalculates its two derived digests.

the private reader is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_source_refresh.py`. it feeds the existing `release_manifest_publisher.py` refresh boundary, trusted Operator context, intent, atomic write, readback and Journal receipt. no new public MCP route or caller-supplied registration is introduced.

### Accepted source revision

```json
{
  "schema_version": 1,
  "registration_id": "prepared-successors-o128-v4-20261006",
  "authorization_ref": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md",
  "repair_task_id": "CA-P-1799",
  "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
  "input_manifest_sha256": "5ca6c9907a4dffbe84319b7d4e391c6242e1969cfea5902845e50f0bd8ae3012",
  "input_canonical_manifest_sha256": "c0edfd130a32386258397da81796d9efab6c1154b17666419edc988d76efc9ba",
  "routes": [
    "create_atom",
    "update_atom",
    "replace_atom",
    "change_atom_status"
  ],
  "pin_occurrences": 8,
  "prior_pin": {
    "atom_id": "CA-O-128",
    "version": 3,
    "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md",
    "digest": "b5d052e97bae6ada98849380199e5c67cbf090900beb33ca202f7872d56301e8"
  },
  "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes@3.md",
  "current_pin": {
    "atom_id": "CA-O-128",
    "version": 4,
    "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md",
    "digest": "ea36b940a171676977507d366daca9400825e8685018d9c201c15fc5b97eea1c"
  },
  "requirement_pin": {
    "atom_id": "CA-R-1041",
    "version": 8,
    "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REPLACE_ATOM/04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md",
    "digest": "45a87fc9dbb416111b66b22875c844abcce0cd362f0a421190406897413bd9bc"
  }
}
```

