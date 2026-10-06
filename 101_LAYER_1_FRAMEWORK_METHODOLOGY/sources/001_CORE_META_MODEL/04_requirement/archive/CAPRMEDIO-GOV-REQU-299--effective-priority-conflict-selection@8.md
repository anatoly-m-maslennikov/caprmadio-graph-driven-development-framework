---
cce_version: cce_1
cce_form: obligation
subjects:
  - priority
version: 8
updated_at: 2026-08-23 12:02:00
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

Concern Atoms store exactly one `priority` value: `high`, `medium`, or `low`. Every Epic, Task, Action Policy, and non-Concern Content role Atom MUST omit `priority`. `highest` is a virtual comparison result and is never stored.

During direct comparison of two Concern Atoms:

1. start with each artifact's stored priority;
2. add one level when its scope is a strict ancestor of the competing scope; and
3. cap the result at virtual `highest`.

An unrelated or incomparable scope receives no scope increment.

The Project Configuration Atom exposes exactly two selection modes:

- `ask_always`, the default, explains the conflict and asks the operator; and
- `auto_by_effective_priority`, which MAY select only one uniquely eligible winner.

Ties, incomparable structure, uncertainty, or multiple winners always ask. Mutually unsatisfiable external obligations stop for operator or external resolution. PRMEDO tier precedence, deterministic replacement, explicit scoped override, stale-view routing, and implementation drift follow their own semantics rather than this selection mode.
