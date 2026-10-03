---
atom_id: CAPRMEDIO-GOV-REQU-294
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - interaction
  depends_on:
    continuant:
      - Framework Instance Settings
      - Operator
version: 15
updated_at: "2026-09-11 18:06:22 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-META-REQU-087
  child_of:
    - CA-R-1054
---
# Configure interaction reporting mode

the Framework Instance Settings Artifact provides one framework-instance interaction reporting setting.

the allowed values are `silent` **and** `verbose`. the Operator **must** select the instance default through Framework Instance Settings; the Meta-Model defines the allowed values **and** their behavior **without** fixing the selected default.

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
