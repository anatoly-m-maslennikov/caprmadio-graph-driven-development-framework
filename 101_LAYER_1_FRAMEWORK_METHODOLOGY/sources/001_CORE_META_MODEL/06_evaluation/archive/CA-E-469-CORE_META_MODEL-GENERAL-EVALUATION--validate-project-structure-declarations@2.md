---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Project Settings"
    - "Framework Instance Settings"
    - "Carrier"
version: 2
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  evaluation_for:
    - "CA-R-1483"
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-M-291"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Project Structure declarations

the Evaluation **must** reject Project Structure **if** its registered Carrier schema is invalid, a Scope Unit Name is duplicated **or** invalid, a parent is unresolved **or** self-referential, parentage contains a cycle, a parent refers **to** another Project, a retained Structural Level disagrees with parent depth, **or** a declaration assigns an invalid Type, Label, order, navigation value, Authority Mode, **or** Carrier binding. Ordered siblings **must not** share structural Local Order; Navigational Order Number duplicates alone **must not** fail validation. an Unordered unit **must not** carry structural Local Order. Label **must not** determine Type. retained readable fields **must** agree with governing source fields **and** admitted Carrier exceptions. lexical **and** resolved-path collisions, traversal outside the authorized repository boundary, **and** ambiguous unit lookup **must** fail. the Evaluation **must** test a valid declaration **and** a falsifying example for **every** applicable condition, with explicit failures for unknown fields **or** unsupported schema versions.
