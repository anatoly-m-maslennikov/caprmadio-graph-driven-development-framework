---
subjects:
  governs: "project-settings"
  depends_on:
    - "Project Structure"
    - "Project Settings"
    - "Framework Instance Settings"
    - "Projection"
version: 13
updated_at: "2026-09-17 21:32:16 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-M-149
    - CA-R-1070
---
# Restore direct Project Scope Unit Graph output edits

## Test case

change one value directly **in** a generated Project Scope Unit Graph **or** Sources output **without** changing **any** admitted authoritative input. retain Project Structure, Project Settings, Framework Instance Settings **and** the selected Atom, directory-observation **and** Journal evidence frontier.

## Acceptance criteria

- read-**only** validation reports the altered output stale **without** writing **any** source **or** generated output.
- a separately authorized rebuild restores the Graph **and** Sources outputs from the admitted current inputs under CA-R-1070 **and** CA-M-149, **not** from the edited output **or** an obsolete Configuration Atom.
- accepted Scope Unit declarations **and** bindings come **only** from Project Structure; observations cannot redefine them.
- authoritative inputs remain byte-identical throughout validation **and** rebuild.
