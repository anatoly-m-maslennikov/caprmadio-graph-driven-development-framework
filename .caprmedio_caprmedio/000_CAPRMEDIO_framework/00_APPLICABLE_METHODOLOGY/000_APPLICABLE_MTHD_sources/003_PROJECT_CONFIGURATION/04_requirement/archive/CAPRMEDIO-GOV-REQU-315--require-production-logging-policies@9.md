---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - "Logging Policy"
  depends_on:
    continuant:
      - "Evaluation Control"
      - "Production Evaluation Checklist"
version: 9
updated_at: "2026-09-11 22:30:02 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal
---
# Require production logging policies

**every** production-relevant component **must** define a Logging Policy that supports its Evaluation Controls **and** is referenced by its Production Evaluation Checklist. the policy identifies the events **and** context required **to** understand normal operation, detect failure, correlate distributed work, **and** investigate real production issues.

## Severity policy

the policy uses these four operational levels:

| Level | Required meaning |
|---|---|
| `ERROR` | an operation failed, correctness **or** availability **may** be affected, **or** explicit retry **or** intervention is required |
| `WARNING` | Behavior was unexpected **or** degraded but recovered, fell back, **or** remains within an accepted tolerance |
| `INFO` | a material lifecycle, business, **or** operational milestone occurred, including start, stop, acceptance, state transition, completion, **or** summarized progress |
| `DEBUG` | Sanitized internal state **or** decision detail is useful for bounded investigation but is unnecessary during normal production operation |

an `ERROR` **or** `WARNING` record **must** be actionable: it identifies the failed **or** degraded condition, affected scope, expected operator **or** automated response, **and** whether retry is safe. High-frequency success, polling, **and** progress events **must not** create unbounded `INFO` noise; they are aggregated, sampled, **or** emitted as `DEBUG` **where** appropriate.

production `DEBUG` logging is disabled by default. Temporary enablement **must** be scoped by component, subject, run, entity, **or** another bounded selector, have an automatic expiry, **and** preserve the same redaction rules as **every** other level.

## Structured record policy

the Carrier content of structured production log records follows CA-D-396.

Logs record material state transitions **and** boundary outcomes rather than **every** internal tick. an exception is emitted once at the boundary responsible for handling **or** escalating it; lower layers preserve structured context **without** duplicating the same stack trace at **every** call boundary.

## Safety and lifecycle policy

Logs **must** never contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads. Personal, customer, **and** commercially sensitive data is omitted, masked, hashed, tokenized, **or** **otherwise** minimized according **to** the applicable boundary.

the policy defines retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink behavior, **and** disk-pressure behavior. Logging **must not** make the primary operation silently fail, **and** loss **or** suppression of required records **must** itself produce an observable failure signal.

production logs use the deployment environment's governed logging sink. Governed CAPRMEDIO workflow **and** local project-control Journals are **not** a substitute for the production system's log platform.

Important health counters, thresholds, **and** service-level signals receive explicit monitors. a production evaluation decision **must not** depend solely on parsing free-form log prose.

## Rationale

Logs are production Ops records, but their required coverage, structure, severity, safety, **and** retention **must** be governed **before** failures occur. a component-specific policy provides that evaluation boundary while leaving the logger implementation **and** emitted records **in** their proper artifact roles.
