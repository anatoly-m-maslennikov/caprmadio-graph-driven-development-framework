---
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Require production logging policies

Every production-relevant component must define a Logging Policy that supports
its Evaluation Controls and is referenced by its Production Evaluation Checklist.
The policy identifies the events and context required to understand normal
operation, detect failure, correlate distributed work, and investigate real
production issues.

## Severity policy

The policy uses these four operational levels:

| Level | Required meaning |
|---|---|
| `ERROR` | An operation failed, correctness or availability may be affected, or explicit retry or intervention is required |
| `WARNING` | Behavior was unexpected or degraded but recovered, fell back, or remains within an accepted tolerance |
| `INFO` | A material lifecycle, business, or operational milestone occurred, including start, stop, acceptance, state transition, completion, or summarized progress |
| `DEBUG` | Sanitized internal state or decision detail is useful for bounded investigation but is unnecessary during normal production operation |

An `ERROR` or `WARNING` record must be actionable: it identifies the failed or
degraded condition, affected scope, expected operator or automated response,
and whether retry is safe. High-frequency success, polling, and progress events
must not create unbounded `INFO` noise; they are aggregated, sampled, or emitted
as `DEBUG` where appropriate.

Production `DEBUG` logging is disabled by default. Temporary enablement must be
scoped by component, subject, run, entity, or another bounded selector, have an
automatic expiry, and preserve the same redaction rules as every other level.

## Structured record policy

Each structured production log record includes, where applicable:

- UTC timestamp, severity, and a stable event name;
- component, environment, and deployed version;
- run, request, job, workflow, session, correlation, or trace identity;
- relevant domain entity identity and lifecycle state;
- outcome, duration, attempt number, and retry disposition;
- stable error code and exception class for failures; and
- a concise human-readable message with sanitized diagnostic context.

Logs record material state transitions and boundary outcomes rather than every
internal tick. An exception is emitted once at the boundary responsible for
handling or escalating it; lower layers preserve structured context without
duplicating the same stack trace at every call boundary.

## Safety and lifecycle policy

Logs must never contain passwords, API keys, access tokens, session secrets,
cookies, private keys, complete credentials, or unredacted secret-bearing
payloads. Personal, customer, and commercially sensitive data is omitted,
masked, hashed, tokenized, or otherwise minimized according to the applicable
boundary.

The policy defines retention, access, sampling, rotation, maximum size,
back-pressure, unavailable-sink behavior, and disk-pressure behavior. Logging
must not make the primary operation silently fail, and loss or suppression of
required records must itself produce an observable failure signal.

Production logs use the deployment environment's governed logging sink.
Governed CAPRMEDIO workflow and local project-control Journals use append-only
NDJSON carriers in their applicable `.caprmedio` role folders; they are not a
substitute for the production system's log platform.

Important health counters, thresholds, and service-level signals receive
explicit monitors. A production evaluation decision must not depend solely on
parsing free-form log prose.

## Rationale

Logs are production Ops records, but their required coverage, structure,
severity, safety, and retention must be governed before failures occur. A
component-specific policy provides that evaluation boundary while leaving the
logger implementation and emitted records in their proper artifact roles.
