---
subjects:
  declared:
    continuant:
      - routing
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 7
updated_at: 2026-08-23 16:16:20 +0400
---
# Provide a Tool router CLI

The framework must provide one deterministic CLI Tool router that accepts an LLM-selected intent, classifies it as a read-only `finder` intent or a mutating or materializing `doer` intent, resolves it through as many registered routing steps as required, returns every applicable Tool option without silently selecting or executing one, and, after the LLM selects an option, returns sufficient machine-readable how-to guidance to invoke that Tool correctly, including its command shape, required and optional inputs, admissible values, preconditions, effects, success checks, failure modes, and representative examples.
