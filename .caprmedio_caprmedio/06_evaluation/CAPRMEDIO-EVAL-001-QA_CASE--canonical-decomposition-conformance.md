---
version: 8
updated_at: "2026-09-17 16:19:27 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-M-001
    - CAPRMEDIO-REQU-642-CORE-REQUIREMENT--govern-canonical-decomposition-conformance
  child_of:
    - CAPRMEDIO-REQU-642-CORE-REQUIREMENT--govern-canonical-decomposition-conformance
subjects:
  governs: "Project/decomposition"
  depends_on:
    - "Project"
    - "Atom/Content Role: Concern"
cce_version: cce_1
cce_form: evaluation
---
# Canonical decomposition conformance

## Claim checked

**every** canonical decomposition satisfies CA-M-001 **and** CAPRMEDIO-REQU-642.

## Check

for **every** declared axis:

- enumerate the bounded universe; **and**
- classify **every** admissible member.

report **any**:

- missing universe **or** axis declaration;
- unclassified member;
- multiple same-axis assignments; **or**
- forced near match.

the check **must not** change the governed decomposition.

## Acceptance

pass **only** **when** no conformance issue is found.

## Failure

record **every** issue as a Concern against the narrowest owning scope.
