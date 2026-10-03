# CA-P-960 complete-Claim audit

Non-authoritative execution evidence for CA-P-960 version 2. This report admits no source disposition or mutation. The inventory is the complete per-source handoff to CA-P-961.

## Coverage and result

All 698 active RMED Markdown sources were reviewed in full: Core Meta-Model 466 R / 41 M / 35 E / 106 D; Local Configuration 35 R / 0 M / 1 E / 14 D. Discovery refreshed the actual source frontier; 698 was the resulting count, not a fixed input. Drafts, Archives, non-RMED sources, generated Applicable Methodology, Project-level normalization, selected Settings, source-owner migration, Tools and installed artifacts were excluded. Every source's complete body was read, including supporting sections; two truncated display batches were reread for the missing ranges before classification.

| Audit disposition | Core | Local | Total |
| --- | ---: | ---: | ---: |
| Carrier specification outside D | 10 | 2 | 12 |
| Mixed role/Carrier Claim | 23 | 14 | 37 |
| Unresolved classification | 1 | 0 | 1 |
| Existing D authority | 106 | 14 | 120 |
| Justified non-D contribution | 508 | 20 | 528 |

`CA-P-960-inventory.json` contains exact repository-relative source path, canonical identity and identity basis, Version, SHA-256, byte count, observed source owner and Content Role, filename tier marker, complete frontmatter, complete Claim/body, complete source text, reviewed digest, grounded per-identity rationale, confidence, and relevant existing authority/overlap references. The repository root is `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework`.

The 120 existing-D entries include D-located semantic Carrier definitions as well as physical contracts. That category records existing ownership; it does not certify every existing D Claim as correctly classified or authorize moving semantic definitions merely because they mention Carriers.

The source verifier returned **PASS** for exact membership, all 698 independent identity/Version/path/digest checks, full source/body/frontmatter equality, complete reviewed evidence, and preservation of all 465,991 source bytes. No source Atom, Task lifecycle, Settings, Journal, Git index, commit, runtime or generated-methodology mutation was performed by this audit. Generated evidence changes used `apply_patch` and remained in this directory under the CA-P-960 prefix.

## Candidate index

The 12 Carrier specifications outside D are CA-R-1304, CA-R-1305, CA-R-1369, CA-R-737, CAPRMEDIO-GOV-REQU-297, CAPRMEDIO-GOV-REQU-362, CAPRMEDIO-GOV-REQU-373, CAPRMEDIO-GOV-REQU-383, CAPRMEDIO-GOV-REQU-760, CAPRMEDIO-GOV-REQU-764, CAPRMEDIO-GOV-REQU-323, and CAPRMEDIO-GOV-REQU-676.

The 37 mixed Claims are CA-R-1372, CA-R-165, CA-R-728, CA-R-978, CA-R-981, CA-R-997, CAPRMEDIO-GOV-REQU-290, CAPRMEDIO-GOV-REQU-294, CAPRMEDIO-GOV-REQU-296, CAPRMEDIO-GOV-REQU-299, CAPRMEDIO-GOV-REQU-302, CAPRMEDIO-GOV-REQU-337, CAPRMEDIO-GOV-REQU-353, CAPRMEDIO-GOV-REQU-355, CAPRMEDIO-GOV-REQU-381, CAPRMEDIO-GOV-REQU-750, CAPRMEDIO-META-REQU-086, CAPRMEDIO-META-REQU-098, CAPRMEDIO-META-REQU-119, CAPRMEDIO-META-REQU-122, CAPRMEDIO-META-REQU-166, CAPRMEDIO-META-REQU-174, CAPRMEDIO-META-REQU-730, CA-R-293, CA-R-825, CAPRMEDIO-GOV-REQU-315, CAPRMEDIO-GOV-REQU-748, CAPRMEDIO-GOV-REQU-749, CAPRMEDIO-GOV-REQU-751, CAPRMEDIO-GOV-REQU-752, CAPRMEDIO-GOV-REQU-754, CAPRMEDIO-GOV-REQU-755, CAPRMEDIO-GOV-REQU-761, CAPRMEDIO-GOV-REQU-762, CAPRMEDIO-GOV-REQU-763, CAPRMEDIO-META-REQU-103, and CAPRMEDIO-R-793-REQUIREMENT-BSEED_GOVERNANCE.

Type meaning/admission and Carrier-token clauses were reviewed separately. The explicit legacy IDs `CAPRMEDIO-R-791-REQUIREMENT-BSEED_METAMODEL` and `CAPRMEDIO-R-793-REQUIREMENT-BSEED_GOVERNANCE` remain authoritative; mutable modern filename fields were not appended to CA-R-number identities. All abbreviated GOV seeds resolve to the exact CAPRMEDIO-GOV-REQU identities above.

## Existing owners and lossless comparisons for CA-P-961

| Candidate or overlap | Existing owner evidence and preserved distinction |
| --- | --- |
| CA-R-165@11 | CA-D-270@5 already owns YAML `version`/`updated_at`; CA-R-1415@3 owns one positive integer Version and CA-R-1416@3 one date-time. Neither R Claim explicitly preserves monotonic Version, and R1416 does not explicitly preserve unambiguity. Do not retire R165 merely because its keys are covered. |
| CAPRMEDIO-META-REQU-166@10 | CA-D-310@5 owns Projection `updated_at`, latest completed rebuild and the no-timestamp-only-currentness guard. Preserve the candidate's unambiguous timestamp, rebuild procedure/configuration and job-specific provenance/no-blanket-frontier clauses. |
| CAPRMEDIO-GOV-REQU-362@12 | Timestamp format and timezone TOML syntax must be reconciled with D270/D310's Project-time encoding; D340's timezone-qualified Occurred At is an Event field, not automatically the same timestamp. |
| CA-R-1369@4 | D353@3 provides at least one Directory Carrier per Structural Entity; D263@5 provides one represented Structural Entity Revision per directory. R1369's exactly-one Epic Carrier is stricter and must survive. D355@3 confirms that cardinality qualifying a concrete Carrier binding is a D contract. |
| CA-R-1304 / CA-R-1305 | D293 owns Epic directory naming and D294/D350 own Task/Objective filenames. Distinguish Epic Identifier from directory Work Sequence and mutable scope/summary; compare exact domains before reuse. |
| CA-R-728 / CA-R-737 / GOV-764 | D283/D284/D291/D302 own surrounding filename/token representation; D376 owns the configured prefix field. These do not by themselves duplicate every Atom-ID grammar or immutable-identity clause. |
| META-122 / META-730 | D281/D282 own H1/Summary-slug serialization and D283/D291 filename composition. D304 preserves identity, meaning, Scope and relations under recoding; preserve semantic revision/impact duties separately. |
| GOV-353 | D329 owns exact YAML `proof_frontier_refs`. The body's abbreviated `GOV REQU 010` is not an approved exact current relation target. |
| GOV-381 / META-174 / META-119 | D268 owns direct relation frontmatter encoding; retain relation endpoint/meaning, binding ownership and explanatory-authority boundaries. |
| GOV-373 / GOV-383 | D333 owns projection generation metadata, D343 the Project graph TOML carrier, D374 the Settings authority-mode encoding, and D375 Project name encoding. Consuming Projection fields are not automatically duplicates of Settings fields. |
| GOV-315 | D328 owns Project Work Journal placement; D339 owns scope Implementation Journal NDJSON placement; D340 owns Event properties. The older blanket role-folder Journal statement must not erase their different domains. |
| CA-R-293 / GOV-761 | Both spell Carrier token `constraint`; retain external-limitation meaning and non-default external Type admission separately. |
| D268 / D272 | Potential existing-D overlap: general direct relation encoding versus Task-specific dependency encoding. Unique Task prerequisite qualification must survive any consolidation. |
| D363 / D364 | Potential existing-D overlap: Project Settings filename grammar versus its identical basename in the full authoritative path. Preserve exact lowercase Project name, root placement and exactly-one Carrier obligations. |

The full inventory includes every other D owner; this table highlights handoff comparisons rather than claiming whole-Claim equivalence or approving retirement. Incoming-reference repair/retirement ordering and exact before-to-after allocations remain CA-P-961 work.

## Unresolved design questions and safeguards

Six records remain below the effective threshold of 99; they are reviewed evidence, not approved admission decisions:

- **CA-R-1372 (97):** latest accepted Journal entry supplies a semantic derived Revision timestamp; decide whether literal `updated_at` is an independently authoritative encoding clause and locate its exact D owner. D340's Event Occurred At is not interchangeable.
- **CA-R-963 (98, unresolved category):** global Scope Unit Name spelling can be reusable naming syntax in M; serialized filename reference tokens are D302/D284. Do not infer D solely from capitalization or grammar.
- **CA-R-978 (98):** separate Operator-controlled navigation-label meaning from possible decimal-rendering choice.
- **CA-R-997 (98):** separate positive unique local ordinal meaning from possible decimal token encoding.
- **CAPRMEDIO-META-REQU-119 (98):** decide whether embedded-Rationale/backlink omission is an independent Carrier contract or a coherent explanatory-ownership guard.
- **CAPRMEDIO-GOV-REQU-752 (97):** the Carrier clause references existing lowercase tokens without enumerating their exact map; resolve existing admitted token authority before allocating the clauses.

M authoring procedures (including M229/M235) and E fixtures/checks remain justified non-D even when they use concrete syntax or test Carriers. The live R1339–R1342 definitions and current Project Principles guided whole-contribution review. D285@5 was read to correct the audit metadata interpretation: omitted ordinary tier means Standard; General is explicit. Source tier/owner changes were not inferred from role classification.

The pending R1224/R1225/R1227 Settings issue, source placement differences under D317/D325, and source/consumer lifecycle issues are recorded as boundaries, not permission to expand this Epic or prerequisites invented from directory order.

## Repeatable source verification

From repository root:

```sh
python3 .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/03_plan/02-CA-Epic-006-FRAMEWORK_METHODOLOGY-align-carrier-claims-with-delivery/execution_evidence/CA-P-960-audit.py verify
```

The command reads source Atoms and compares them with the captured inventory; it writes only `CA-P-960-verification.json` evidence through `apply_patch`. `CA-P-960-snapshot.json` preserves the captured bytes; `CA-P-960-reviews.json` contains the manually entered per-identity judgments. Any intervening source change must be reviewed and refreshed before the affected record is used in CA-P-961.
