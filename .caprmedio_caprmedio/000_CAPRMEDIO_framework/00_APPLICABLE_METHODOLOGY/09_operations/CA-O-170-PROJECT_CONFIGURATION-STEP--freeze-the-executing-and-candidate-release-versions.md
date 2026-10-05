---
atom_id: CA-O-170
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: freeze"
  depends_on: [Workflow, Step, Action, Version, Journal]
version: 1
updated_at: 2026-10-05 06:13:05 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-165]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-170-PROJECT_CONFIGURATION-STEP--freeze-the-executing-and-candidate-release-versions.md
  source_atom_id: CA-O-170
  source_atom_revision: 1
  source_sha256: 621cd9c836bdf1398594723e456f1155f9f8725c780d88b47fbc92b92f1c14e5
  original_relations_sha256: 23a87cc05c9a57ff0a893fb5e597c91ca05039fd92e4aa31fdf1be3e3e0caa1c
---
# Summary

Freeze the executing and candidate release Versions

## Step

This Step invokes CA-O-165 once with phase `freeze`, binding the selected current N and separate candidate N+1 identities, source revisions/digests, current runtime and rollback evidence. It returns that exact result unchanged.

## Details

Missing, equal, mutable, stale or unjournalable version boundaries stop before any delivery effect. This Step neither validates destinations nor copies, compiles, installs, tests, builds, promotes, retires or retries. Its Step Run and referenced Action Run retain their exact parent, input and Journal evidence.
