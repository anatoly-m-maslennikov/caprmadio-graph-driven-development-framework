---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - interaction
version: 11
updated_at: 2026-09-04 04:05:44 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-META-REQU-087--exploration-mode-input-routing
  child_of:
    - CA-R-1054
---
# Configure interaction reporting mode

the Framework Instance Settings Artifact provides one framework-instance interaction reporting setting:

```toml
[interaction]
reporting_mode = "silent" # silent | verbose
```

the allowed values are exactly `silent` **and** `verbose`. the default is `silent`.

**in** `silent` mode, CAPRMEDIO does **not** announce ordinary mode selection, workflow routing, skill chaining, **or** gate transitions. it answers exploratory input normally **and** reports **only** durable Artifacts **or** Project state that it created, updated, archived, committed, **or** **otherwise** changed.

**in** `verbose` mode, CAPRMEDIO explicitly reports relevant workflow modes, mode transitions, selected skill chains, entry **and** exit gates, **and** planned **or** completed artifact operations.

reporting mode changes presentation **only**. it never changes authorization, artifact creation, workflow routing, validation, **or** safety behavior. the two values **must** still report:

- blockers **and** failed operations;
- ambiguity that requires operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.

skills **and** Tools read this setting from the Framework Instance Settings Artifact. they do **not** maintain independent reporting defaults.

## Rationale

silent reporting keeps ordinary CAPRMEDIO use natural **and** concise, while verbose reporting makes orchestration inspectable during adoption, debugging, audits, **and** methodology development. keeping the two behaviors behind one framework-instance setting prevents individual Skills from drifting into inconsistent interaction styles.
