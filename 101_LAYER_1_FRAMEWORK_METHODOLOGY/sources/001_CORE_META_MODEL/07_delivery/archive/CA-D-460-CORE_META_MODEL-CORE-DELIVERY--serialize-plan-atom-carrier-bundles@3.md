---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Plan/Authoritative Carrier Bundle"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan/Carrier/Stem"
    - "File Carrier"
    - "Directory Carrier"
version: 3
updated_at: "2026-09-22 23:02:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1578", "CA-D-469"]}
---
# Summary

Serialize Plan Atom Carrier Bundles

## Claim

a Plan Atom Carrier Bundle **must** consist of **`=1`** Markdown File Carrier **and** **`<=1`** optional matching Directory Carrier using the same canonical stem under CA-D-469.

- the Markdown file carries the Plan's own Properties **and** follows CA-D-470, including its mandatory Definition of Done.
- a matching directory organizes related Plan Carriers; it neither creates another Atom **nor** replaces the mandatory Markdown file.
- the file **and** optional directory represent the same identity, Summary, Label, **and** Status, checked under CA-D-480.
- related Plan files carry independent Atoms; they are **not** additional Carriers of the Hub's Claim.
