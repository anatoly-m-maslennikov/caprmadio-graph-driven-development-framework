---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - provenance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 5
updated_at: 2026-08-23 15:00:38
relations:
  child_of:
    - CAPRMEDIO-META-REQU-169--record-every-projection-rebuild-in-a-journal
---
# Journal Projection rebuild events

Each Projection rebuild is one Work Journal action with operation `projection_rebuild`: its `started` event binds the target Projection, governed generator, configuration, and any explicit inputs required by the Projection's registered job; exactly one terminal event records the outcome; and a `completed` event additionally binds the published Projection `updated_at`, output carrier, and content digest. A rebuilt Projection becomes current only after its `completed` event is accepted.
