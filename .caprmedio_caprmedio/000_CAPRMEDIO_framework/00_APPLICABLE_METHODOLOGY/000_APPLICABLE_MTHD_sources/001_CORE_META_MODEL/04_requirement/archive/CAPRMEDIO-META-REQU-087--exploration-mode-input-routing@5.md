---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - development-flow
version: 5
updated_at: 2026-08-29 01:16:37 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-199--exploration-mode-defers-artifact-creation
    - CAPRMEDIO-META-REQU-212--question-input-enters-exploration-mode
    - CAPRMEDIO-META-REQU-213--idea-input-enters-exploration-mode
  child_of:
    - CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop
---
# Requirement — Route uncertain input through Exploration Mode

Exploration Mode permits brainstorming, discussion, research, analysis, comparison, terminology work, **and** structural modeling **without** creating **or** changing governed artifacts.

CAPRMEDIO enters Exploration Mode **when** the operator's input primarily:

- asks for information, explanation, comparison, critique, alternatives, **or** a recommendation; **or**
- introduces an idea, explores it, **or** asks for feedback on it.

An explicit operator request to create **or** change governed state takes precedence over question-shaped wording. **otherwise**, Exploration Mode ends **only** **when** the operator explicitly accepts a conclusion **or** requests its promotion. CAPRMEDIO **then** emits **only** the minimum artifacts required to preserve the accepted meaning. A Projection **may** refresh **only** **after** its declared source Atoms exist.

Whether a mode transition is announced is a downstream interaction-reporting choice **and** does **not** change this routing.

## Primary claim

Question **and** idea input stays non-persistent **in** Exploration Mode **until** explicit operator acceptance authorizes the minimum durable artifacts.
