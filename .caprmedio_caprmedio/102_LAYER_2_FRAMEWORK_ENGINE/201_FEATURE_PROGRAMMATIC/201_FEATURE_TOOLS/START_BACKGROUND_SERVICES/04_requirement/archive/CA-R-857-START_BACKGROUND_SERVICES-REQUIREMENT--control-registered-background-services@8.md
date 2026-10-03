---
subjects:
  governs:
    continuant:
      - feature-boundary
version: 8
updated_at: 2026-08-30 16:44:07 +0400
---
# Control registered background services

START_BACKGROUND_SERVICES must be one Doer Tool owned immediately by TOOLS as an unordered_unit at Structural level 4, addressed by 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/START_BACKGROUND_SERVICES, and realized under that path. It MUST read one machine-readable registry from the selected installed release and expose status, pause, resume, stop, start, and reload for every enabled service.

Every command MUST preserve accepted inbox, queue, action, receipt, circuit, and dead-letter state. pause stops new dispatch without deleting accepted intake. stop stops admission and reaches a declared safe shutdown boundary. start resumes admission and drains accepted work. reload reaches a safe boundary, re-resolves the selected installed release, restarts, and reconciles preserved work. No command may force termination across an unrecoverable mutation critical section.

The Tool MUST use dry-run unless apply is explicit, treat an empty registry as a successful no-op, reject duplicate or unsafe declarations before mutation, permit framework implementation only from .caprmedio_install, and write mutable state only below .caprmedio_runtime. Repeated apply MUST be idempotent. Automatic restart and retry MUST remain within declared measured budgets. Exhausted budgets, governance failures, Journal failures, staging failures, ambiguous Git outcomes, and lease-integrity failures MUST open the circuit or pause autonomous dispatch and require explicit Operator recovery.
