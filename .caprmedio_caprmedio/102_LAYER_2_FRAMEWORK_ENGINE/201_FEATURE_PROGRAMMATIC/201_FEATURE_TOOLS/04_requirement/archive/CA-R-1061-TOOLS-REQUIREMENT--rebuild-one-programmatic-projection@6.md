---
subjects:
  declared:
    continuant:
      - projection-pipeline
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 6
updated_at: 2026-08-23 16:16:20 +0400
---
# Rebuild one programmatic Projection

The framework must provide one deterministic Tool that rebuilds one registered programmatic Projection from its declared sources, writes `updated_at` and `source_frontier`, replaces the output atomically, and records the rebuild through the Work Journal Tool.
