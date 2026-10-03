---
subjects:
  - carrier-format
version: 8
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CA-R-1057
    - CA-R-1054
    - CA-R-888
---
# Compose readable Atom class short names

GOVERNANCE derives each lowercase `snake_case` typed-Atom class short name by splitting its canonical Type name into words, replacing every registered word with its canonical short form, preserving every unregistered word in full, and joining them with underscores. The filename `<ATOM_TYPE>` token projects that registered short name to uppercase ASCII without changing its words or underscores.

| Canonical word | Short form |
|---|---|
| `external` | `ext` |
| `implementation` | `impl` |
| `evaluation` | `eval` |
| `report` | `rprt` |
| `control` | `cntrl` |
| `record` | `rec` |

Every admitted typed-Atom class resolves to exactly one unique short name within its owning Content role; no fixed character width or unregistered ad hoc contraction is permitted. Canonical class short names include `analysis_rprt`, `ext_analysis_rprt`, `conflict_analysis_rprt`, `impl_decision`, `eval_cntrl`, and `incident_rec`; their filename projections are `ANALYSIS_RPRT`, `EXT_ANALYSIS_RPRT`, `CONFLICT_ANALYSIS_RPRT`, `IMPL_DECISION`, `EVAL_CNTRL`, and `INCIDENT_REC`.
