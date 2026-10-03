# CA-P-961 lossless Carrier authority disposition design

Non-authoritative evidence for CA-P-961@2. Result: **PASS**. All 50 candidates have explicit dispositions at the effective threshold of 99. This completes design evidence only; the coordinating agent owns Task lifecycle disposition.

The exact current 698-source frontier and every captured SHA-256 still match CA-P-960. `78` surviving owner records contain complete proposed Claims; `30` new identities are proposals, globally checked against repository content and filenames, and remain unreserved. Exact prior-source bytes and Archive paths/hashes are recorded for every changed or retired existing owner. No source or Archive was changed.

## Decisions retained

- R165 retires only after existing R1415 contains positive integer Version increasing monotonically across successive Revisions, R1416 contains one unambiguous Updated At date-time, and D270 remains the field encoding owner.
- R1372 stays semantic: exactly one derived Journal Revision Updated At from the latest accepted entry; no new persisted field is proposed.
- R963 becomes proposed M275 naming/formatting authority; D284/D302 keep their physical filename domains. R1369 exact-one Epic Directory Carrier qualification is added to D353 before retirement.
- The Operator approved each registered Journal placement: D328 dedicated `.caprmedio_caprmedio/work_journal/` and D339 Implementation Content Role directory remain unchanged. D406 covers only the remaining original governed workflow/local-control NDJSON domain. No new storage or migration action is authorized.
- GOV315 retains its Logging Policy and receives the matching existing Logging Policy Subject; generic evaluation is not its primary governed Entity. D396 governs generic Carrier so streamed/network production logs are not excluded. New owner Subjects reuse existing Entities, declare genuine prerequisites, and do not infer Temporal Form from Content Role.
- GOV337 preserves all stage meanings and forward-only dependency semantics. Mermaid relation maps are illustrative consumer-ready examples, not an independent mandatory format. D388 owns explicit stage prefixes and NDJSON/TOON encoding.
- GOV752 token spellings come from its exact bound source contribution. Type admission remains R; Carrier token authority is D. Source ownership and Core/General/omitted Standard tier decisions remain independent; no tier or source-owner migration is proposed.

## Incoming-reference handoff

The complete text scan includes ignored paths: 9,303 occurrences across 1,356 consumers, with 11 active RMED occurrences. Every occurrence is classified; every active RMED consumer has a complete-Claim mapping rationale. There are zero external blocking repairs.

| Timing | Consumer | Required mapping |
| --- | --- | --- |
| Before retirement | CA-E-427 | R1304 → D379; R1369 → revised D353 |
| Before retirement | Local GOV761 and GOV762 | GOV760 → D393, replacing each whole decorated target value |
| Before extraction | Core GOV-EVAL-009 | Retain GOV299; add D386 for storage/omission checks |
| Before extraction | Local GOV-EVAL-006 | Retain GOV294/GOV302; add D383/D387 for parsed Settings encoding |

These repairs are in the two permitted source owners and must be verified before dependent extraction/retirement; CA-P-962 can perform the necessary cross-owner reference slice. GOV314 retains its Type-admission relation without an unnecessary optional D link. External ENGINE561 still consumes the retained stage vocabulary; CA-M-163 still consumes retained severity semantics and already delegates Carrier encoding to D. Historical/Journal records remain exact; generated/installed and other non-RMED mentions are downstream follow-ups.

**Revision handoff:** CA-P-962 must repair GOV761/GOV762 and GOV-EVAL-006 in Local Configuration before the affected Core extraction/retirement. CA-P-963 must preserve those references, refresh the sanctioned newer Revisions, and archive each intermediate Revision it changes. It must never overwrite those newer Revisions with the CA-P-960 snapshot; use that snapshot only as the original allocation evidence.

## Verification and boundary

`CA-P-961-verification.json` records source membership/hashes, complete substantive original-text allocation, owner resolution, Archive safety, global ID availability, Subject cardinality/duplicate checks, semantic qualifier guards, admission and reference-review status. Semantic review supplies the role/Scope decisions; these checks corroborate it and do not claim automated proof of equivalence.

All writes stayed under `execution_evidence/CA-P-961-*` through `apply_patch`. No source Atom, Task/lifecycle file, selected Settings, Journal, Git state, Tool/compiler/install/runtime or generated Projection was changed. Pending Epic005 R1224/R1225/R1227 Settings, R1222 placement and source-owner decisions remain excluded. This approved boundary is not a task blocker.

Reproduce from repository root with `python3 -B .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/03_plan/02-CA-Epic-006-FRAMEWORK_METHODOLOGY-align-carrier-claims-with-delivery/execution_evidence/CA-P-961-design.py`. The script refreshes only this task's evidence through `apply_patch` and fails the verification result if the source frontier, ID availability, coverage or mapping conditions no longer hold.
