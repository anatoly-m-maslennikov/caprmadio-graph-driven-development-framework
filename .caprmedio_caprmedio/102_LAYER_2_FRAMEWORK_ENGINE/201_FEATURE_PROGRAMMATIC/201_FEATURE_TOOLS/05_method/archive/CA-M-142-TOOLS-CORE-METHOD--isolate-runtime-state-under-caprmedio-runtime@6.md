---
subject_scopes:
  - runtime
version: 6
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---

# Isolate runtime state under caprmedio runtime

Place CAPRMEDIO-owned reconstructible execution state under the current
project's caprmedio runtime root whenever the host platform and invoked
dependency permit it. Use native temporary or cache locations only for the
minimum transient adapter state required by that host, never as governed
authority, and reconcile it when the owning operation ends.

Keep the runtime tree non-authoritative: deleting it may lose resumable
progress or caches, but cannot lose a governed artifact.

Do not place installed executable releases, shared implementation libraries,
machine-readable implementation registries, stable launchers, or Hook carriers
in the runtime tree. Those reconstructible but executable installation
carriers belong under `.caprmedio_install`.
