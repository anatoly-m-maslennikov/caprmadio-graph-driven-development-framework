---
cce_version: cce_1
cce_form: placement
subjects:
  governs: "Atom/Content Role: Plan/Carrier Placement"
  depends_on:
    - "Atom/Content Role: Plan/Status"
    - "Atom/Content Role: Plan/Authoritative Carrier Bundle"
version: 2
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1539", "CA-R-1540", "CA-R-1541"]}
---
# Place Plan Carriers by Status

**every** Plan Carrier Bundle **must** encode its Status relative **to** its own local Plan container: the Directory Carrier of the Plan it decomposes, **or** its Scope Unit's `03_plan` **when** it has no such Plan.

- Active: directly **in** that local container.
- Backlog: **in** its `001_backlog` subdirectory.
- Done: **in** its `done` subdirectory.
- Canceled: **in** its `canceled` subdirectory.
- Archived: **in** its `archived` subdirectory.

reserved Status directories are **not** Plan nodes. resolve a nested Plan's Status from the placement of its own Bundle relative **to** that local container, **not** from a Status directory above its Hub Bundle. moving a Hub **must not** silently change descendant Status; a status cascade requires an explicit authorized change for **every** affected Plan.
