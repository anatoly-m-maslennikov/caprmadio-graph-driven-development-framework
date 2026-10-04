---
atom_id: CA-E-580
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 01:20:00 +0400"
subjects:
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/Run evidence"
  depends_on: [Tool, Workflow Run, Action Run, Journal, Evaluation]
relations:
  evaluation_for: [CA-R-1867]
---
# Summary

Verify actual query Run journaling through shared support

## Claim

The Tool creates shared RunJournal evidence only for an actual admitted query execution and creates none for preview or denied requests.

## Test case

Run preview, denied execute, and admitted execute against a source whose
byte-prefix is captured before workflow/action-start recording.

## Acceptance criteria

Preview and denial have no Run/Event identity; admitted execute has truthful Workflow/Step/Action lineage and cannot affect its result snapshot.

## Failure disposition

Reject fake Runs, preview Events, competing logs, or snapshot mutation.
