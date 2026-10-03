---
subject_scopes:
  - framework-engine-software
  - observability
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Provide correlated structured diagnostic records

Deliver one neutral structured diagnostic record schema with timestamp, severity, component, operation, outcome, and canonical action or event correlation. Keep a concise human rendering at the CLI boundary and allow replaceable exporters behind the neutral schema.

Do not require OpenTelemetry as the default runtime dependency while the built-in logging delivery is sufficient. An OpenTelemetry adapter may be added when external correlation or a telemetry backend becomes an accepted need.

Candidate alignment: CA-D-001, CA-D-002, CA-M-002, CA-M-005, CA-O-003.

## Sources

- [Python Logging HOWTO](https://docs.python.org/3.14/howto/logging.html)
- [OpenTelemetry: logs](https://opentelemetry.io/docs/concepts/signals/logs/)
- [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)
