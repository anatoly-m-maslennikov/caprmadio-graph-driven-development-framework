---
atom_id: CA-P-1349
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Reconcile F04 replacement and loss preserving lineage"
  depends_on: [Operations, "Methodology Sources"]
version: 3
updated_at: "2026-10-04 13:34:31 +0000"
relations:
  is_decomposition_of: [CA-P-1130]
  blocks: [CA-P-1131, CA-P-1156]
---
# Summary

Reconcile F04 replacement and loss preserving lineage

## Objective

Composite family reconciliation: preserve all37 unassigned/unrepresented primary entry references from F04 and roll up exact intent-group decisions in CA-A-1067. Whole-family review is not estimated as <=15 minutes. One assigned Agent per executable child; the first child below is estimated <=15 minutes. Preparation does not execute it.

### Complete family input and bounded decomposition

Use `.caprmedio_caprmedio/02_analysis/CA-A-1063-ANALYSIS_RPRT--consolidate-the-closed-corpus-candidate-register.md` source_entry_assignments for F04: every NEEDS_RECONCILIATION primary row is bound below; not merely the first-ten frontier. Markdown ordinals are1-based and JSON indices0-based. Read complete saved clauses only; no native collection.
| Entry | Saved locator | Ordinal/index | Candidate | Cross-family refs | Packet |
| --- | --- | --- | --- | --- | --- |
| R0018 | S004 | 1 | H909-C1 | F08 | first CA-P-1401 |
| R0021 | S004 | 4 | H909-C4 | F08 | first CA-P-1401 |
| R0039 | S007 | 2 | H913-C2 | none | first CA-P-1401 |
| R0041 | S008 | 2 | unnamed | F08 | first CA-P-1401 |
| R0061 | S013 | 2 | C02 | F08 | first CA-P-1401 |
| R0081 | S017 | 5 | C05 | F01, F08 | first CA-P-1401 |
| R0110 | S024 | 4 | OP04 | F08, F07 | first CA-P-1401 |
| R0115 | S025 | 5 | C05 | F08, F10, F07 | first CA-P-1401 |
| R0116 | S025 | 6 | C06 | F03, F08, F10, F07 | first CA-P-1401 |
| R0126 | S027 | 4 | unnamed | F08, F10, F07 | first CA-P-1401 |
| R0153 | S035 | 3 | C03 | F08 | first CA-P-1401 |
| R0154 | S035 | 4 | C04 | none | first CA-P-1401 |
| R0185 | S044 | 6 | unnamed | F08, F07 | first CA-P-1401 |
| R0187 | S045 | 2 | unnamed | F01, F15, F08, F10, F07 | first CA-P-1401 |
| R0193 | S046 | 6 | unnamed | F15 | first CA-P-1401 |
| R0209 | S051 | 2 | unnamed | F08, F10, F07 | first CA-P-1401 |
| R0226 | S056 | 1 | unnamed | F10 | first CA-P-1401 |
| R0228 | S056 | 3 | unnamed | F01, F10 | first CA-P-1401 |
| R0248 | S060 | 3 | unnamed | F08 | CA-P-1409 |
| R0264 | S063 | 1 | unnamed | F08, F10 | CA-P-1409 |
| R0265 | S063 | 2 | unnamed | F08 | CA-P-1409 |
| R0271 | S064 | 3 | unnamed | F08, F10, F07 | CA-P-1409 |
| R0282 | S066 | 3 | unnamed | F08, F10, F07 | CA-P-1409 |
| R0288 | S067 | 4 | unnamed | F08, F07 | CA-P-1409 |
| R0297 | S069 | 3 | unnamed | F08, F10 | CA-P-1409 |
| R0300 | S069 | 6 | unnamed | F08, F10 | CA-P-1409 |
| R0311 | S071 | 6 | unnamed | none | CA-P-1409 |
| R0317 | S072 | 5 | unnamed | F08, F07 | CA-P-1409 |
| R0336 | S077 | 3 | G03 | F08 | CA-P-1409 |
| R0365 | S083 | 3 | G3 | F17, F08, F10 | CA-P-1409 |
| R0385 | S087 | 3 | G4 | F08 | CA-P-1409 |
| R0392 | S089 | 1 | unnamed | none | CA-P-1409 |
| R0393 | S090 | 0 | G1 | F17, F08 | CA-P-1409 |
| R0402 | S091 | 4 | G4 | F17, F10 | CA-P-1409 |
| R0409 | S093 | 2 | G2 | F10, F07 | CA-P-1409 |
| R0418 | S095 | 1 | G1 | none | CA-P-1409 |
| R0440 | S100 | 4 | G4 | F17, F10 | CA-P-1410 |

Saved locator bindings (not copied source text):

- S004: `.caprmedio_caprmedio/02_analysis/CA-A-909-ANALYSIS_RPRT--harvest-the-first-final-partition-session-packet.md` → `Reusable candidates and provisional destinations`.
- S007: `.caprmedio_caprmedio/02_analysis/CA-A-913-ANALYSIS_RPRT--harvest-the-second-third-partition-main-session-packet.md` → `Provisional reusable Operations candidates`.
- S008: `.caprmedio_caprmedio/02_analysis/CA-A-914-ANALYSIS_RPRT--harvest-the-second-final-partition-session-packet.md` → `Provisional reusable candidates`.
- S013: `.caprmedio_caprmedio/02_analysis/CA-A-920-ANALYSIS_RPRT--harvest-the-subsequent-second-partition-session-packet.md` → `Provisional reusable candidate groups`.
- S017: `.caprmedio_caprmedio/02_analysis/CA-A-924-ANALYSIS_RPRT--harvest-the-later-second-partition-session-packet.md` → `Provisional reusable candidate groups`.
- S024: `.caprmedio_caprmedio/02_analysis/CA-A-931-ANALYSIS_RPRT--harvest-the-next-first-partition-session-packet.md` → `Provisional reusable operational candidates`.
- S025: `.caprmedio_caprmedio/02_analysis/CA-A-932-ANALYSIS_RPRT--harvest-the-next-second-partition-remainder.md` → `Provisional reusable candidate groups`.
- S027: `.caprmedio_caprmedio/02_analysis/CA-A-934-ANALYSIS_RPRT--harvest-the-later-final-partition-session-packet.md` → `Provisional reusable candidate groups`.
- S035: `.caprmedio_caprmedio/02_analysis/CA-A-948-ANALYSIS_RPRT--harvest-the-final-original-second-partition-packet.md` → `Provisional reusable candidate groups`.
- S044: `.caprmedio_caprmedio/02_analysis/CA-A-966-ANALYSIS_RPRT--harvest-the-final-readme-session-evidence.md` → `Provisional capability groups`.
- S045: `.caprmedio_caprmedio/02_analysis/CA-A-970-ANALYSIS_RPRT--harvest-the-final-tool-session-opening.md` → `Provisional capability groups`.
- S046: `.caprmedio_caprmedio/02_analysis/CA-A-974-ANALYSIS_RPRT--harvest-the-whole-final-testing-policy-report.md` → `Provisional capability groups`.
- S051: `.caprmedio_caprmedio/02_analysis/CA-A-982-ANALYSIS_RPRT--harvest-the-first-final-partition-worker-source.md` → `Four provisional overlapping candidate groups`.
- S056: `.caprmedio_caprmedio/02_analysis/CA-A-988-ANALYSIS_RPRT--harvest-the-subsequent-second-partition-continuation-packet.md` → `Candidate groups and decision handling`.
- S060: `.caprmedio_caprmedio/02_analysis/CA-A-998-ANALYSIS_RPRT--harvest-the-first-final-partition-worker-bundle.md` → `Six provisional overlapping candidate groups`.
- S063: `.caprmedio_caprmedio/02_analysis/CA-A-1009-ANALYSIS_RPRT--harvest-the-next-subsequent-second-partition-continuation-packet.md` → `Candidate groups and frontier`.
- S064: `.caprmedio_caprmedio/02_analysis/CA-A-1010-ANALYSIS_RPRT--harvest-the-subsequent-third-partition-evaluation-continuation-packet.md` → `Six provisional grouped candidates`.
- S066: `.caprmedio_caprmedio/02_analysis/CA-A-1012-ANALYSIS_RPRT--harvest-the-following-second-partition-continuation-packet.md` → `Five provisional grouped refinements`.
- S067: `.caprmedio_caprmedio/02_analysis/CA-A-1013-ANALYSIS_RPRT--harvest-the-following-third-partition-evaluation-and-authority-packet.md` → `Five provisional grouped refinements`.
- S069: `.caprmedio_caprmedio/02_analysis/CA-A-1016-ANALYSIS_RPRT--harvest-the-next-third-partition-same-sample-repair-packet.md` → `Human chains, supersession and provisional candidates`.
- S071: `.caprmedio_caprmedio/02_analysis/CA-A-1018-ANALYSIS_RPRT--harvest-the-next-second-partition-actor-and-authority-packet.md` → `Source-supported refinements and supersession`.
- S072: `.caprmedio_caprmedio/02_analysis/CA-A-1018-ANALYSIS_RPRT--harvest-the-next-second-partition-actor-and-authority-packet.md` → `Five provisional grouped refinements`.
- S077: `.caprmedio_caprmedio/02_analysis/CA-A-1022-ANALYSIS_RPRT--harvest-the-next-second-partition-presentation-and-review-packet.md` → `Provisional reusable refinements`.
- S083: `.caprmedio_caprmedio/02_analysis/CA-A-1027-ANALYSIS_RPRT--harvest-the-next-second-partition-policy-and-lifecycle-packet.md` → `Provisional reusable refinements`.
- S087: `.caprmedio_caprmedio/02_analysis/CA-A-1030-ANALYSIS_RPRT--harvest-the-ninth-final-partition-worker-bundle.md` → `json fence 0: provisional_groups`.
- S089: `.caprmedio_caprmedio/02_analysis/CA-A-1033-ANALYSIS_RPRT--harvest-the-third-partition-framework-name-and-lifecycle-plan-packet.md` → `Literal chains and provisional groups`.
- S090: `.caprmedio_caprmedio/02_analysis/CA-A-1034-ANALYSIS_RPRT--harvest-the-tenth-final-partition-worker-bundle.md` → `json fence 0: provisional_groups`.
- S091: `.caprmedio_caprmedio/02_analysis/CA-A-1035-ANALYSIS_RPRT--harvest-the-following-second-partition-review-boundary-packet.md` → `Provisional reusable refinements and overlap`.
- S093: `.caprmedio_caprmedio/02_analysis/CA-A-1037-ANALYSIS_RPRT--harvest-the-first-second-partition-worker-bundle.md` → `Provisional refinements and uncertainty`.
- S095: `.caprmedio_caprmedio/02_analysis/CA-A-1038-ANALYSIS_RPRT--harvest-the-earliest-third-partition-worker-bundle.md` → `Provisional reusable groups`.
- S100: `.caprmedio_caprmedio/02_analysis/CA-A-1044-ANALYSIS_RPRT--harvest-the-next-second-partition-worker-bundle.md` → `Provisional refinements`.

Current Operation starting owners; exact metadata does not imply semantic equivalence:

- CA-O-051 v6: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-051-CORE_META_MODEL-ACTION--persist-atom-replacement-through-ordered-carrier-transitions.md`.
- CA-O-058 v6: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-058-CORE_META_MODEL-ACTION--assess-revision-impact-through-lineage.md`.
- CA-O-067 v6: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-067-CORE_META_MODEL-ACTION--assess-atom-update-identity.md`.

At execution verify live revisions and read each compared current carrier fully; name any different actual owning source before relying on it. Do not force non-operational model/representation/instance instructions into O or redesign ontology. Current P1117 v2 / P1119 v2 / P1130 v5, Goal v13 and all14 active Project Principles govern at inherited90% confidence. Reuse unchanged verified full reads; read changed authority. Current R1589 v4 / R1580 v4 / D479 v6 / D461 v6 govern binding, explicit readiness, body layout and status placement. No new native harvesting; A1043 remains excluded.

First-five reuse / representation receipts:

- R0083 (F04 primary; cross F08) remains assigned to CA-P-1342; reuse only its exact reviewed proposition from `.caprmedio_caprmedio/02_analysis/CA-A-1060-ANALYSIS_RPRT--reconcile-replacement-and-lineage-preservation.md`, not whole-family acceptance.
- R0389 (F04 primary; cross F08, F10) remains assigned to CA-P-1342; reuse only its exact reviewed proposition from `.caprmedio_caprmedio/02_analysis/CA-A-1060-ANALYSIS_RPRT--reconcile-replacement-and-lineage-preservation.md`, not whole-family acceptance.
- Retained alias links, not new primary work: R0322 → R0317, R0342 → R0336, R0372 → R0365, R0414 → R0409, R0446 → R0440. Compare any distinct qualifiers before claiming reuse.

### First executable packet and exact remainder

CA-P-1401 at `.caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/02-CA-P-1119-TASK--reconcile-and-author-methodology-operations/01-CA-P-1130-TASK--reconcile-candidates-with-current-authority/10-CA-P-1349-TASK--reconcile-f04-replacement-and-loss-preserving-lineage/01-CA-P-1401-TASK--reconcile-f04-first-intent-packet.md` compares all independent clauses of the first18 exact rows (R0018, R0021, R0039, R0041, R0061, R0081, R0110, R0115, R0116, R0126, R0153, R0154, R0185, R0187, R0193, R0209, R0226, R0228) and saves CA-A-1121. The first batch includes all family primary rows in its selected whole saved sections and coalesces repeated intent groups rather than creating per-form tests. The other19 rows explicitly marked exact unbound remainder remain owned by this composite, not promised as a executable leaf; root/next authorized preparation must bind subsequent <=15-minute children from those exact refs before closure. Reuse completed intent groups only after checking every remaining qualifier; repeated forms need not create new Operations/tests. No automatic fifty-six-Plan expansion.

Own this composite and reserved family rollup `.caprmedio_caprmedio/02_analysis/CA-A-1067-ANALYSIS_RPRT--reconcile-f04-replacement-and-loss-preserving-lineage.md` only. Child Agents own their Plans/results. This composite and its first child both BLOCK P1131/P1156. First-child completion does not unlock authoring or mark this family Done; all primary refs and retained alias/receipt qualifications require disposition and required independent review.

### Remaining execution now bound

- CA-P-1409: 18 exact references; carrier `.caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/02-CA-P-1119-TASK--reconcile-and-author-methodology-operations/01-CA-P-1130-TASK--reconcile-candidates-with-current-authority/10-CA-P-1349-TASK--reconcile-f04-replacement-and-loss-preserving-lineage/02-CA-P-1409-TASK--reconcile-f04-intent-packet-2.md`; output CA-A-1129; prepared/unexecuted, one Agent, <=15-minute estimate.
- CA-P-1410: 1 exact references; carrier `.caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/02-CA-P-1119-TASK--reconcile-and-author-methodology-operations/01-CA-P-1130-TASK--reconcile-candidates-with-current-authority/10-CA-P-1349-TASK--reconcile-f04-replacement-and-loss-preserving-lineage/03-CA-P-1410-TASK--reconcile-f04-intent-packet-3.md`; output CA-A-1130; prepared/unexecuted, one Agent, <=15-minute estimate.

These children partition every formerly unbound family reference exactly. No child is completed by preparation. The earlier first-child estimate remains separate; all required outputs precede family rollup. No harvesting is reopened.

## Details

### Definition of Done

CA-A-1067 accounts for all37 bound primary refs with current-source intent-group dispositions and exact destinations, aggregates actual completed child outputs, preserves first-five/alias boundaries and has actual verification. Any unfinished exact remainder or required child/review falsifies Done. No O/RMED/implementation or full-stage completion is claimed.
