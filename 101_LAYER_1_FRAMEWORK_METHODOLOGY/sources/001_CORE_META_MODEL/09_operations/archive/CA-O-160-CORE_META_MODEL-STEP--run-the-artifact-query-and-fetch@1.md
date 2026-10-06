---
atom_id: "CA-O-160"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
type: "Step"
version: 1
updated_at: "2026-10-05 00:00:00 +0400"
subjects:
  governs: "Artifact query and fetch execution"
  depends_on: [Workflow, Action, Artifact, Markdown, Journal]
relations:
  part_of: [CA-O-158]
  invokes: [CA-O-159]
---
# Summary

Run the Artifact query and fetch

## Step

This Step **must** validate the read-only request, seal its source snapshot,
and invoke CA-O-159 once with that snapshot and the requested filter, fetch
selection, page limit, and cursor.

## Details

The Step returns CA-O-159's result without mutation or retry substitution. It
does not dispatch another Workflow, infer an ID from a filename, admit an
unselected source root, or write query results as a Projection. It passes an
actual execution through the shared RUN_SUPPORT/Work Journal contract only as
defined by CA-D-527, CA-D-528, and CA-D-529; preview and every rejected request
have no Run or Event identity.
