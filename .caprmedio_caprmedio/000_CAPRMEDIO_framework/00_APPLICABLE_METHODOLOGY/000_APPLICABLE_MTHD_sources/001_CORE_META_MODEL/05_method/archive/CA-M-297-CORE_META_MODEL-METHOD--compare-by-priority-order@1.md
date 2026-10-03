---
version: 1
updated_at: "2026-09-17 02:26:06 +0000"
relations:
  child_of:
    - CA-R-1487
  method_for:
    - CA-R-1487
subjects:
  governs: "Project/lexicographic selection"
  depends_on:
    - "Operator"
    - "Project/priority model application"
    - "Atom/Content Role: Method"
cce_version: cce_1
cce_form: method
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Compare by priority order

**when** the Operator selects comparison by priority order, the comparison of admissible alternatives **must** use the resolved order of active, applicable criteria as follows:

- an earlier criterion takes precedence over a later criterion.
- for alternatives tied on **all** earlier criteria, the first criterion that distinguishes them determines their relative preference.
- later criteria **must not** override a preference established by an earlier criterion.
- alternatives tied on **all** applicable criteria remain tied.
- an incomplete criterion order **or** an incomparable result at the current deciding criterion leaves the comparison unresolved; a later criterion **must not** bypass that gap.

this Method defines the comparison technique, **not** priority activation, alternative-selection execution, **or** escalation.
