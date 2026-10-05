---
atom_id: CA-O-182
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: run host-capable Candidate E2E"
  depends_on: [Workflow, Step, Action, Test, Docker Image, Journal]
version: 2
updated_at: "2026-10-05 21:41:23 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-181]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-182-PROJECT_CONFIGURATION-STEP--run-host-capable-candidate-e2e.md
  source_atom_id: CA-O-182
  source_atom_revision: 2
  source_sha256: f9ad4960f3215f3af3c833cc95cc2fd18b16b67fdd9ed3981b5f93153933d3ce
  original_relations_sha256: e1cb11d250a76c80b8669cc121020a27006ec8f2fa42a169212b5fab6fff7a19
---
# Summary

Run host-capable Candidate E2E

## Step

This Step invokes CA-O-181 once after CA-O-186's immutable image canary, binding the exact candidate/package/image/N identity and explicit host-capable controller authorization.

## Details

Absent host capability is non-pass, not a fallback to the frozen Docker worker. Failed, partial, stale, unsafe or missing-recording results stop before Full Gate aggregation, promotion and retirement without replay.
