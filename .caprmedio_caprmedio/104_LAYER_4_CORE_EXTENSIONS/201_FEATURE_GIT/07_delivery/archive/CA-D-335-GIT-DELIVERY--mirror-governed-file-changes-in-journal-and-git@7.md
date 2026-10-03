---
cce_version: cce_1
cce_form: atomicity
subjects:
  governs: "Governed File Change Materialization"
  depends_on:
    - "Journal/Record"
    - "Git Commit"
    - "Carrier"
version: 7
updated_at: "2026-09-15 21:31:49 +0000"
relations: {}
---
# Mirror Governed File Changes in Journal and Git

**when** the Git Extension is selected, materialize **every** approved atomic change set as follows:

- create **=1** Git Commit containing **all** **and** **only** the approved changes; the change set **may** contain **>=1** File Carriers.
- retain **=1** canonical Journal file-change Event for **every** changed File Carrier, including **every** successor **and** predecessor Carrier changed by replacement.
- preserve the correspondence between the committed change set **and** its individual Journal Events; Git **must not** become another authoritative Journal.

successor **and** predecessor Carrier changes **may** share the approved atomic change set. their individual Journal Events **must not** require separate Git Commits.
