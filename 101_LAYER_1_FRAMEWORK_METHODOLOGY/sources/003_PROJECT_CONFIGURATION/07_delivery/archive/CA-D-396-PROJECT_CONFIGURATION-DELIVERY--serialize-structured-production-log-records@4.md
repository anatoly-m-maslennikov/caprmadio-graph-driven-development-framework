---
atom_id: CA-D-396
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Carrier"
  depends_on:
    - "Logging Policy"
version: 4
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
