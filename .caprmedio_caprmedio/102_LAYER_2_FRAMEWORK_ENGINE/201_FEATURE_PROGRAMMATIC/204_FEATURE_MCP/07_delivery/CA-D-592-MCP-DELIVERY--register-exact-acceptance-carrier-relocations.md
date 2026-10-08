---
atom_id: CA-D-592
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-08 17:31:41 +0000"
subjects:
  governs: "MCP/exact acceptance-carrier relocation admission"
  depends_on: [MCP, Projection, Operator, Run, Journal, Source Carrier]
relations:
  delivery_for: [CA-R-1899, CA-M-354, CA-E-598]
---
# Summary

Register exact acceptance-carrier relocations

## Scope

the one registered relocation of three acceptance carriers under the current Epic.

## Claim

the acceptance-carrier relocation admission **must** use the closed serialization below for its exact three-carrier authority revision.

## Details

the **only** registration is the JSON object under `### Accepted carrier relocations`. its keys and nested relocation shapes are exact; duplicate or unknown fields are invalid. version and schema version are strict integers. paths are safe regular Project-relative carriers with no symlink ancestry.

the exact canonical input bytes and all three retained current source-carrier bytes **must** match. each relocation replaces only its registered prior source path with its registered current source path; carrier identity, version and digest remain unchanged. no route, graph, registry, source digest or normal fixed-path refresh behavior is otherwise admitted for change. the resulting canonical serialization and its derived `canonical_manifest_sha256` are recomputed; the route-identical `selected_binding_digest` remains unchanged.

the private reader feeds the existing typed host publisher, trusted Operator context, lock, pending intent, atomic write, strict readback and Work Journal receipt. an interrupted pre-effect attempt may retry the same candidate once only when the exact registered original input, sealed intent and current sources still match. once the exact candidate exists, recovery is recording-only without rewrite; ambiguous bytes refuse. no public MCP route, generic relocation capability, alias or caller-supplied registration is introduced.

### Accepted carrier relocations

```json
{
  "schema_version": 1,
  "registration_id": "acceptance-carrier-relocations-p1117-20261008",
  "authorization_ref": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md",
  "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
  "input_manifest_sha256": "1381b8c41d59e7f3636ac69e37e365e41b8429469e748e9824e982a7ccdd71a9",
  "input_canonical_manifest_sha256": "2235d03cdb904942c9b26118a867769696fbe3dfc650eebb6c2e8d49b19bbc4e",
  "relocations": [
    {
      "atom_id": "CA-P-1618",
      "version": 1,
      "prior_source_path": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md",
      "current_source_path": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md",
      "digest": "bdf10c928c10c102dc489c8e3e526ffe73e8a33d492f4dabc8b5d0129c453b1f"
    },
    {
      "atom_id": "CA-P-1535",
      "version": 2,
      "prior_source_path": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md",
      "current_source_path": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md",
      "digest": "6246b46d2961d795e29eeb224f01b14979434d4ad24cf3f4913c490268cf52dc"
    },
    {
      "atom_id": "CA-P-1622",
      "version": 4,
      "prior_source_path": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/done/02-CA-P-1622-TASK--review-release-version-source-and-admission.md",
      "current_source_path": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/done/02-CA-P-1622-TASK--review-release-version-source-and-admission.md",
      "digest": "7cd6a839a190add10108bdd5e58700aeae7a89316aa721b2b5340bda865a2739"
    }
  ]
}
```
