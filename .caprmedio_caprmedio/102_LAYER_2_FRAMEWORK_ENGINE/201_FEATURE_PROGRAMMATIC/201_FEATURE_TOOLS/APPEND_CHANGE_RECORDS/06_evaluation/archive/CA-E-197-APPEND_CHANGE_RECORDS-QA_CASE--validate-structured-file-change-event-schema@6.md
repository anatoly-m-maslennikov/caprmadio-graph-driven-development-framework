---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CAPRMEDIO-GOV-REQU-339--register-work-journal-events
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
  check_of:
    - CA-D-009-DELIVERY-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--deliver-change-record-appender-script
---
# Validate the structured file-change event schema

## Claim checked

Every completed `governed_file_change` event has canonical structured LLM-session and occurrence-time provenance and does not duplicate that provenance, prior state, or the projected Git message.

## Test case

Validate one event for each action type against the registered schema, then inject an absent or malformed `llm_session.app`, `llm_session.uuid`, or timezone-qualified `occurred_at`, a pre-rendered combined session string, another absent required field, an invalid state-dependent field, `action_message`, `before_path`, and `before_sha256` in separate runs.

## Acceptance criteria

Each valid event passes and can derive `<app>:<uuid>:<occurred_at>` from structured fields; each malformed event fails with a stable field-specific diagnostic; `sources` is ordered; `result` is singular; and forbidden duplicated fields are rejected.

## Failure disposition

Reject the Journal record when its structure or LLM-session provenance is incomplete, ambiguous, action-inconsistent, or duplicates derivable state.
