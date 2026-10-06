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
---
# Summary

Freeze the executing and candidate release Versions

## Step

This Step invokes CA-O-165 once with phase `freeze`, binding the selected current N and separate candidate N+1 identities, source revisions/digests, current runtime and rollback evidence. It returns that exact result unchanged.

## Details

Missing, equal, mutable, stale or unjournalable version boundaries stop before any delivery effect. This Step neither validates destinations nor copies, compiles, installs, tests, builds, promotes, retires or retries. Its Step Run and referenced Action Run retain their exact parent, input and Journal evidence.
