---
subjects:
  governs: "Carrier"
  depends_on:
    - "Logging Policy"
version: 6
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
---
# Serialize Structured Production Log Records

**every** structured production log record **must** include, **where** applicable:

- UTC timestamp, severity, **and** a stable event name;
- component, environment, **and** deployed version;
- run, request, job, workflow, session, correlation, **or** trace identity;
- relevant domain entity identity **and** lifecycle state;
- outcome, duration, attempt number, **and** retry disposition;
- stable error code **and** exception class for failures; **and**
- a concise human-readable message with sanitized diagnostic context.
