---
subject_scopes:
  - routing
version: 7
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-098
    - CA-M-099
---
# Select the least costly sufficient execution mechanism

For one requested operation, first establish the required outcome, applicable
non-negotiable constraints, available source inputs, acceptance conditions,
candidate execution mechanisms, their capability limits, and the effective
Operator priority order. Do not select automatically when any of these inputs
is absent, contradictory, or insufficient to distinguish the candidates.

Classify a candidate operation as **deterministically specifiable** only when
its accepted inputs, transformation, decision rules, and acceptance conditions
are explicit enough that the same admitted inputs require the same result
without interpretation, judgment, or open-ended planning. Select a sufficient
deterministic mechanism for that operation whenever one is available. An LLM
may prepare or interpret work around such an operation, but it must not replace
the deterministic execution of the bounded operation itself.

When the operation requires interpretation, judgment, or open-ended
orchestration, use an LLM only for that irreducibly interpretive boundary and
keep every fully specifiable sub-operation deterministic. From the remaining
sufficient candidates, apply the effective Operator priority order, including
declared human-effort and external-expense priorities, to choose the least
costly acceptable mechanism. Equal-ranked candidates require a declared
deterministic tie-breaker; incomparable candidates, an unavailable required
mechanism, or an unresolved cost estimate return the choice to the Operator
without execution.

Stop at that boundary. Record the unresolved input or comparison as a
diagnostic; do not guess a deterministic rule, silently substitute an LLM, or
claim that an LLM result establishes deterministic sufficiency.
