---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - commit-automation
    occurrent:
      - realization
version: 2
updated_at: 2026-08-30 16:44:07 +0400
autonomous_confidence_threshold: 95
---
# Realize durable asynchronous commit automation

WHEN asynchronous commit-automation authority is current, THE Assignee MUST replace the blocking Hook-driven implementation with durable asynchronous intake, one independently supervised repository service, one pure decision manager, a mechanical recoverable Scheduler, atomic non-deciding workers, and one serialized Git pipeline.

## Scope

(Atom ID IN (CA-R-802, CA-R-803, CA-R-804, CA-R-805, CA-R-812, CA-R-856, CA-R-857, CA-M-087, CA-M-103, CA-M-104, CA-M-182, CA-E-169, CA-E-194, CA-E-217, CA-E-227, CA-E-234, CA-E-235, CA-E-300, CA-D-006, CA-D-007, CA-D-012) OR Path BELOW 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS WHERE Component IN (COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, COMMIT_CHANGE_SET, INSTALL_TOOLS, START_BACKGROUND_SERVICES, COMMIT_AUTOMATION, shared-runtime))

## Definition of Done

THE Task is NOT DONE IF (a Codex command can still wait for automatic provenance work before dispatch OR automatic commit intake uses PreToolUse, SessionStart, or Stop OR an accepted event can be lost when the Hook, manager, Scheduler, service, or host session ends OR a manager performs I/O OR a worker chooses downstream work OR the Scheduler advances an undeclared transition OR COMMIT_CHANGE_SET imports or orchestrates a peer Tool OR more than one Git-mutating pipeline can run per repository OR accepted work is deleted by pause, resume, stop, start, or reload OR failure budgets and circuits are not inspectable OR missed external changes cannot be reconciled OR installation, fresh runtime operation, recovery, and latency Evaluations have not passed against the exact installed release).

## Details

Use one asynchronous Codex PostToolUse command Hook only for atomic Runtime inbox acceptance. Treat Hook events as wake-ups and provenance observations, not repository truth. The repository-local COMMIT_AUTOMATION service owns reconciliation and scheduling but no RMED authority. Its pure manager defines the execution graph; the Scheduler persists and mechanically advances it; workers execute atomic effects. Preserve the fixed peer-Tool pipeline COMMIT_CONTEXT -> APPEND_CHANGE_RECORDS -> COMMIT_CHANGE_SET and the independent real-change and Journal-only commit classes.

Implement status, pause, resume, stop, start, and reload without deleting accepted work. Measure the applicable surfaces before selecting queue, timeout, lease, crash, cooldown, restart, and recovery budgets. Automatically retry only classified transient pre-mutation failures. Require explicit Operator recovery for governance, Journal, staging, ambiguous Git, lease-integrity, or exhausted-budget outcomes.

Do not claim completion from static validation, an installed-status result, or a dry run. Record fresh end-to-end evidence that one installed event returns without host-visible command delay, survives interruption, reaches the correct independent Journal and Git outcomes, and remains recoverable from every declared safe phase.
