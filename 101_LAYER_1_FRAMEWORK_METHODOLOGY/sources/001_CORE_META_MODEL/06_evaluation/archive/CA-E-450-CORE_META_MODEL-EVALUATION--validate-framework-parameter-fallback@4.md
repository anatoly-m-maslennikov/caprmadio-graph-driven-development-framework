---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Framework Instance Settings/parameter resolution validation"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Project"
    - "Operator"
version: 4
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  evaluation_for:
    - "CA-R-1441"
    - "CA-M-279"
    - "CA-D-407"
    - "CA-D-408"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate framework parameter fallback

the Evaluation **must** reject framework parameter resolution **if** **any** of the following falsifying conditions holds:

- a valid explicit parameter loses **to** a Default Settings value;
- a missing parameter fails **to** inherit its available valid default, including **when** another parameter **in** the same section is explicit;
- a valid explicit `false`, `0`, **or** empty value is mistaken for an absent parameter;
- an invalid explicit value is accepted **or** replaced by a fallback value;
- an invalid selected default is accepted, **or** a required parameter missing from Framework Instance Settings **and** Default Settings receives an invented value;
- an optional parameter absent from Framework Instance Settings **and** Default Settings is rejected solely for its absence;
- resolution reads another Project's instance selections **or** writes inherited values back as explicit selections;
- unchanged input values resolve differently on a repeated read;
- Default Settings uses an unregistered Carrier location **or** a parameter representation that differs from its registered Framework Instance Settings representation.

use the registered parameter constraints for the cases; **when** the current parameter catalog lacks a Boolean, zero-valued, **or** empty-valued example, use isolated test-fixture parameters **without** adding them **to** authoritative Settings.
