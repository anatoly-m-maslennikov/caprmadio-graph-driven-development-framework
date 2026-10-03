# CA-P-962 Core Carrier authority repair

Non-authoritative execution evidence for CA-P-962@2. Result: **PASS**. All 34 admitted Core dispositions are applied; Task lifecycle remains with the coordinating agent.

The current slice has 52 surviving Core owners: 19 new, 26 revised, and 7 reused unchanged. 12 predecessor identities retired. The five reference-only consumers and all changed owners have independent field/hash checks. 45 exact Archives preserve original or intermediate prior bytes across 64 recorded source operations.

## Required reference ordering

| Consumer | Current Revision | Verified mapping |
| --- | --- | --- |
| CA-E-427 | @7 | CA-R-1304 → CA-D-379; CA-R-1369 → CA-D-353 |
| CAPRMEDIO-GOV-EVAL-006 | @17 | CAPRMEDIO-GOV-REQU-294 → CAPRMEDIO-GOV-REQU-294, CA-D-383; CAPRMEDIO-GOV-REQU-302 → CAPRMEDIO-GOV-REQU-302, CA-D-387 |
| CAPRMEDIO-GOV-EVAL-009 | @13 | CAPRMEDIO-GOV-REQU-299 → CAPRMEDIO-GOV-REQU-299, CA-D-386 |
| CAPRMEDIO-GOV-REQU-761 | @12 | CAPRMEDIO-GOV-REQU-760 → CA-D-393 |
| CAPRMEDIO-GOV-REQU-762 | @9 | CAPRMEDIO-GOV-REQU-760 → CA-D-393 |

All seven mappings have successor → consumer repair → extraction/retirement operation sequences in verification.json. Consumer Claims remain byte-exact. GOV302 also canonicalizes its existing semantic relates_to value for GOV294 while retaining that relation.

## Preserved boundaries and corrections

- R1415 retains positive integer Version and monotonic increase; R1416 retains exactly one unambiguous Updated At date-time. Existing D270 remains unchanged. R1372 remains derived from the latest accepted Journal entry with no new persisted field.
- D353 retains generic >=1 Structural Entity Carrier cardinality and stricter =1 for Epic. M275 preserves nonempty uppercase letter-or-digit tokens and single underscores. Shared D owners are reused once, and the seven Core retain owners are byte-unchanged.
- General tier is preserved on R1415/R1416; the other changed Core owners retain omitted Standard. Source ownership and current Claim Scope are preserved. No selected Settings or Journal location was changed.
- Exact admitted Claim text is preserved apart from registered-operator bold rendering and general sentence/cell-start capitalization. Three current Subject assignments are narrowed or aligned using existing Entities: R981 Navigational Order Number; GOV296 Implementation Type with identity, Governance Origin and existing provenance prerequisite; GOV299 Priority with its comparison/Settings/Operator prerequisites. Their exact changes and rationale are recorded in mapping.json.
- Root found an overbroad article-case normalization that changed the unquoted Analysis identity letter A to a in D378@1. Work paused; every actual-versus-design Claim diff and literal token sequence was audited. D378@1 is preserved exactly, and corrected D378@2 restores uppercase A. The helper now limits article normalization to sentence/cell starts. A separate GOV296@10→@11 correction restores existing lowercase provenance Subject spelling. All original operation hashes and intermediate Archives remain recorded.

## Verification and handoff

Independent Ruby Psych parsing and field checks pass for all 50 current changed Atoms. The whole two-owner frontier is exactly accounted for, with every unaffected source SHA unchanged. A fresh scan of source and 806 active Project RMED Carriers finds no retired identity mention requiring an active target.

CA-P-962-local-handoff.json gives the exact current path, Version, SHA-256, prior Archive, and repaired links for Local GOV761, GOV762 and GOV-EVAL006. CA-P-963 must refresh those sanctioned Revisions, preserve the links and archive the intermediate bytes before its own changes; the CA-P-960 snapshot is only the original allocation baseline.

Generated/installed and historical mentions remain nonblocking downstream reconciliation. No Task/lifecycle, Project authority outside the source owners, selected Settings, pending Epic005 issue, source ownership, Tools/install/runtime, Journal, Git index, commit or push was changed.

Reproduce verification from repository root with:

`python3 -B .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/03_plan/02-CA-Epic-006-FRAMEWORK_METHODOLOGY-align-carrier-claims-with-delivery/execution_evidence/CA-P-962-verify.py`

Verification regenerates only CA-P-962 evidence through apply_patch and reads source bytes. It does not mutate source Atoms.
