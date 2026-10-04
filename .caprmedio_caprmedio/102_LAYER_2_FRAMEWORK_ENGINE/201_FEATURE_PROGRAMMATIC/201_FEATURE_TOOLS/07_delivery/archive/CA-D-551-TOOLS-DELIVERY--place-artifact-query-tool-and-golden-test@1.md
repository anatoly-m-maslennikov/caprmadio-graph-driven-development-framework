---
atom_id: CA-D-551
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:00:00 +0400"
subjects:
  governs: FIND_AND_FETCH_ARTIFACTS
  depends_on: [Tool, Workflow, Action, Journal, Implementation]
relations:
  delivery_for: [CA-R-1849, CA-R-1850, CA-M-330, CA-E-569]
---
# Summary

Place Artifact query Tool and golden test

## Scope

Delivery placement only; no implementation or registration is performed by
this Atom.

## Claim

FIND_AND_FETCH_ARTIFACTS **must** be delivered at
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/`
with its golden test at
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/tests/test_find_and_fetch_artifacts.py`,
and must import the shared RUN_SUPPORT/Work Journal library rather than create
route-local Run or Journal storage.

## Details

The delivery implements CA-O-158 through CA-O-160 and CA-R-1849, CA-R-1850,
CA-M-330, and CA-E-569. It remains read-only and has no MCP registration, source relocation,
Projection result carrier, credentials/secrets reader, or independent Journal.
Any persistent Journal access uses the configured canonical
`.caprmedio_<project name>/_journal/` root through CA-D-527 to CA-D-529; the
known physical carrier migration remains permission-blocked and this Delivery
does not bypass it.
