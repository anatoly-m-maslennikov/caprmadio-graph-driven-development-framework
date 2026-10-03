---
cce_version: cce_1
cce_form: permission
subjects:
  governs: "Implementation Binding"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Claim"
version: 1
updated_at: "2026-09-17 11:52:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Keep Evaluation implementation coverage explicit

coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:

- **=1** Evaluation Atom **may** be realized by multiple distinct implementations.
- **=1** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.

a shared implementation **must not** make its covered Claims **or** their result attribution implicit. this Claim governs coverage, **not** a new Carrier **or** a second implementation registry.
