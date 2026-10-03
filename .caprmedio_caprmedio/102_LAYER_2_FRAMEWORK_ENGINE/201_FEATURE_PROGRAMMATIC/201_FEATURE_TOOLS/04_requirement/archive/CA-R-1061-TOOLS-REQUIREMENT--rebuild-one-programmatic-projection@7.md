---
subjects:
  governs:
    continuant:
      - projection-pipeline
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 7
updated_at: 2026-08-30 16:44:07 +0400
---
# Rebuild one programmatic Projection

The framework must provide one deterministic Tool that rebuilds one registered programmatic Projection from its declared sources, writes `updated_at` and `source_frontier`, replaces the output atomically, and records the rebuild through the Work Journal Tool.
