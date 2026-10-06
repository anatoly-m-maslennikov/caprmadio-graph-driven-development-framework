---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - interaction
version: 8
updated_at: 2026-08-29 01:16:37 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-META-REQU-087--exploration-mode-input-routing
  child_of:
    - CA-R-1054
---
# Configure interaction reporting mode

The Project Configuration Atom provides one project-owned interaction reporting setting:

```toml
[interaction]
reporting_mode = "silent" # silent | verbose
```

The allowed values are exactly `silent` **and** `verbose`. The default is `silent`.

**in** `silent` mode, CAPRMEDIO does **not** announce ordinary mode selection, workflow routing, skill chaining, **or** gate transitions. It answers exploratory input normally **and** reports **only** durable artifacts **or** project state that it created, updated, archived, committed, **or** **otherwise** changed.

**in** `verbose` mode, CAPRMEDIO explicitly reports relevant workflow modes, mode transitions, selected skill chains, entry **and** exit gates, **and** planned **or** completed artifact operations.

Reporting mode changes presentation **only**. It never changes authorization, artifact creation, workflow routing, validation, **or** safety behavior. the two values **must** still report:

- blockers **and** failed operations;
- ambiguity that requires operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.

Skills **and** tools read this setting from the current project's governance configuration. They do **not** maintain independent reporting defaults.

## Rationale

Silent reporting keeps ordinary CAPRMEDIO use natural **and** concise, while verbose reporting makes orchestration inspectable during adoption, debugging, audits, **and** methodology development. keeping the two behaviors behind one project-owned setting prevents individual skills from drifting into inconsistent interaction styles.
