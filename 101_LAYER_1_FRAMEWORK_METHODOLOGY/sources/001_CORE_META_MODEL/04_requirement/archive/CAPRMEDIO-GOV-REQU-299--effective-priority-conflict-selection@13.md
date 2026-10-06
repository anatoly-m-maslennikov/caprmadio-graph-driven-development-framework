---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - priority
version: 13
updated_at: 2026-09-04 04:05:44 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-414--derive-effective-priority-during-comparison
    - CAPRMEDIO-GOV-REQU-415--configure-conflict-selection-mode
    - CAPRMEDIO-GOV-REQU-419--three-level-priority-vocabulary
  child_of:
    - CA-R-1054
---
# Effective priority conflict selection

a Concern Atom stores **`=1`** `priority` value: `high`, `medium`, **or** `low`. **every** Epic, Task, Action Policy, **and** non-Concern Content Role Atom **must** omit `priority`. `highest` is a virtual comparison result **and** is never stored.

during direct comparison of two Concern Atoms:

1. start with **every** artifact's stored priority;
2. add one level **when** its scope is a strict ancestor of the competing scope; **and**
3. cap the result at virtual `highest`.

an unrelated **or** incomparable Scope receives no Scope increment.

the Framework Instance Settings Artifact exposes **`=2`** selection modes:

- `ask_always`, the default, explains the conflict **and** asks the operator; **and**
- `auto_by_effective_priority`, which **may** select **only** one uniquely eligible winner.

ties, incomparable structure, uncertainty, **or** multiple winners always ask. mutually unsatisfiable external obligations stop for Operator **or** external resolution. PRMEDO Tier precedence, deterministic replacement, explicit scoped override, stale-view routing, **and** Implementation drift follow their own semantics rather than this selection mode.
