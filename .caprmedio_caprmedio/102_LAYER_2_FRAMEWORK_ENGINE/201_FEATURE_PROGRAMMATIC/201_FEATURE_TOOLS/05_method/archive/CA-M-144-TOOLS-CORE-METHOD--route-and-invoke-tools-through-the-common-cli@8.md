---
subjects:
  declared:
    continuant:
      - routing
version: 8
updated_at: 2026-08-23 17:53:53 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-1063
    - CA-R-1064
    - CA-R-1065
    - CA-R-1066
    - CA-R-1067
---
# Route and invoke Tools through the common CLI

Use this flow for every Tool invocation:

1. The LLM declares the intended capability without naming an implementation; the router classifies it as `finder` or `doer` and may refine it to a registered subtype such as `checker`.
2. The router resolves as many registered decision steps as required and returns every applicable Tool with identity, purpose, inputs, preconditions, effects, success checks, failure modes, command shape, and representative examples.
3. After the LLM selects one Tool, pass either composable structural-unit, Type, and subtype filters or explicit canonical Atom filenames through the common target selector and return the resolved target set before execution.
4. Execute the selected Tool from its selected immutable release under `.caprmedio_install`. Use `.caprmedio_runtime` only for mutable execution state, caches, logs, service state, and other reconstructible outputs; it must not supply executable Tool implementation. Every Finder, including every Checker, receives no Atom-write capability, while every Doer first returns a complete mutation-free dry run and then writes only its declared authoritative source or derived output after explicit application.
5. Return the common result envelope, stable diagnostics, exit status, resolved targets, observed effects, and applicable currentness information.
