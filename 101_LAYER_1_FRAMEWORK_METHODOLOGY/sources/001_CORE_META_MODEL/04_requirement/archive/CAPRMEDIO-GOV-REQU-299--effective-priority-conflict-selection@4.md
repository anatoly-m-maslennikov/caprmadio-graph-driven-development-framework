---
subject_scopes:
  - priority
version: 4
updated_at: 2026-08-21 03:22:46
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-414--derive-effective-priority-during-comparison
    - CAPRMEDIO-GOV-REQU-415--configure-conflict-selection-mode
    - CAPRMEDIO-GOV-REQU-419--three-level-priority-vocabulary
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Effective priority conflict selection

Concern Atoms and action-point Plan Atoms store exactly one `priority` value: `high`, `medium`, or `low`. Tier-classified `action_policy` Plan Atoms and every other Content role omit `priority`. `highest` is a virtual comparison result and is never stored.

During direct comparison of two Concern or action-point Plan Atoms:

1. start with each artifact's stored priority;
2. add one level when its scope is a strict ancestor of the competing scope; and
3. cap the result at virtual `highest`.

An unrelated or incomparable scope receives no scope increment.

The Project Configuration Atom exposes exactly two selection modes:

- `ask_always`, the default, explains the conflict and asks the operator; and
- `auto_by_effective_priority`, which may select only one uniquely eligible
  winner.

Ties, incomparable structure, uncertainty, or multiple winners always ask.
Mutually unsatisfiable external obligations stop for operator or external
resolution. PRMEDO tier precedence, deterministic replacement, explicit scoped
override, stale-view routing, and implementation drift follow their own
semantics rather than this selection mode.
