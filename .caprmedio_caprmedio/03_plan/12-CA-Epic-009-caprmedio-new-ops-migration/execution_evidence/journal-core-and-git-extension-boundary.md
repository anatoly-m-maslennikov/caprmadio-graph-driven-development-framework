# Journal Core and Git Extension boundary

Source-only amendment accepted by the Operator. This report is derived change evidence, not an Atom, an authoritative Journal event, a commit receipt, or Task completion.

## Applied boundary

- Core owns one authoritative Journal, also called an Event Log.
- Core defines Artifact Change Log and Process Log as two non-authoritative Projection Types. Both reference the same recorded events.
- Git-specific rules now have a source Scope Unit at `.caprmedio_caprmedio/104_LAYER_4_CORE_EXTENSIONS/201_FEATURE_GIT/`, with a parent-owned Goal and a Delivery binding.
- NDJSON serialization, numbered-Atom replacement payload encoding, and the concrete generated-data stages reside in PROJECT_CONFIGURATION. These choices do not require Git.
- Core replacement, revision, provenance, and settings-receipt rules no longer make Git commits the admission or persistence boundary.
- Git-specific policies moved with their existing Atom IDs and unchanged Summaries. No Extension package was installed or activated.

## Added Atoms

| Atom ID | Owner | Summary |
|---|---|---|
| CA-R-1466 | CORE_META_MODEL | keep git integration in an extension |
| CA-R-1467 | CORE_META_MODEL | define artifact change log projection |
| CA-R-1468 | CORE_META_MODEL | define process log projection |
| CA-R-1469 | CORE_EXTENSIONS | provide optional git integration |
| CA-D-436 | GIT | bind git extension delivery place |
| CA-E-465 | PROJECT_CONFIGURATION | validate replacement event schema encoding |
| CA-E-464 | CORE_META_MODEL | validate journal independence from git |

## Relocated Atoms

| Atom ID | New owner | Summary |
|---|---|---|
| CAPRMEDIO-GOV-REQU-296 | GIT | distinguish internal and external git commits |
| CA-D-384 | GIT | serialize git commit type tokens |
| CA-D-334 | GIT | serialize governed change commit messages |
| CA-D-335 | GIT | mirror governed file changes in journal and git |
| CA-D-339 | PROJECT_CONFIGURATION | serialize the shared project journal |
| CA-D-435 | PROJECT_CONFIGURATION | serialize atom replacement event references |
| CA-D-388 | PROJECT_CONFIGURATION | serialize generated data stage prefixes and formats |
| CAPRMEDIO-GOV-REQU-337 | PROJECT_CONFIGURATION | register generated data stages |

## Revised Atoms

| Atom ID | Owner | Summary |
|---|---|---|
| CAPRMEDIO-META-REQU-656 | CORE_META_MODEL | define journal artifact form |
| CAPRMEDIO-META-REQU-158 | CORE_META_MODEL | use one project journal for governed provenance |
| CA-R-1463 | CORE_META_MODEL | derive log views from the shared journal |
| CA-M-274 | CORE_META_MODEL | persist atom replacement through ordered carrier transitions |
| CA-R-1432 | CORE_META_MODEL | classify admitted atom changes by semantic effect |
| CAPRMEDIO-META-REQU-097 | CORE_META_MODEL | requirement keep provenance separate from evidence |
| CAPRMEDIO-META-REQU-099 | CORE_META_MODEL | requirement close every constitutional amendment |
| CAPRMEDIO-META-REQU-105 | CORE_META_MODEL | preserve implementation traceability in the shared project journal |
| CAPRMEDIO-META-REQU-107 | CORE_META_MODEL | bind traceability to exact claims and revisions |
| CAPRMEDIO-GOV-REQU-340 | CORE_META_MODEL | recover work journal coverage without invention |
| CAPRMEDIO-GOV-REQU-351 | CORE_META_MODEL | define self hosted governance origins |
| CAPRMEDIO-GOV-REQU-290 | CORE_META_MODEL | requirement exclude secrets from caprmedio |
| CA-D-382 | CORE_META_MODEL | place local environment injection carriers |
| CA-M-135 | CORE_META_MODEL | exclude generated only implementation edges |
| CAPRMEDIO-GOV-EVAL-010 | CORE_META_MODEL | validate generated only provenance boundary |
| CA-E-462 | CORE_META_MODEL | validate atom replacement event evidence |
| CAPRMEDIO-GOV-EVAL-003 | CORE_META_MODEL | storage boundary interpretability |
| CA-D-360 | CORE_META_MODEL | bind framework settings revisions to journal receipts |
| CA-D-365 | CORE_META_MODEL | bind project settings revisions to journal receipts |
| CA-E-458 | CORE_META_MODEL | validate authoritative framework settings artifact |
| CA-E-459 | CORE_META_MODEL | validate authoritative project settings artifact |
| CAPRMEDIO-META-REQU-090 | CORE_META_MODEL | propagate atomic revision impact through lineage |
| CAPRMEDIO-META-REQU-100 | CORE_META_MODEL | preserve external boundary obligations |
| CAPRMEDIO-GOV-REQU-302 | CORE_META_MODEL | gate atomic admission and promotion |
| CAPRMEDIO-GOV-REQU-310 | CORE_META_MODEL | classify lineage impact with four dispositions |

## Validation

- 40 current source Atom Carriers checked: 25 revisions, 8 relocations, 7 additions.
- All 33 previous Carriers archived byte-for-byte at their prior versions.
- Existing Atom IDs and Summary values preserved; updated versions incremented once.
- YAML parsed; changed Atom IDs resolve to one active source Carrier each.
- New Evaluation references resolve to current source Atoms.
- No remaining active Core imports of moved Git, NDJSON, staging, or replacement-schema authority were found in the targeted dependency scan.
- 11,633 other files were content-identical to the pre-edit snapshot, excluding `.DS_Store`.
- The Git index and authoritative Journal were unchanged.

The companion [change map](journal-core-and-git-extension-boundary.projection.json) records exact source paths, archive paths, versions, and SHA-256 digests.

## Deferred work

Generated Applicable Methodology, source-selection snapshots, runtime Tools, installed hooks, and Git Extension packaging/installation were not changed. Existing generated copies and Tool consumers may still reflect the prior Core placement or Git coupling; this report does not claim runtime alignment or implementation of the new Evaluations.

The containing migration Epic and its Tasks remain in progress. Later Journal materialization must use the actual preserved change evidence and actual recording time; this report must not be substituted for an authoritative Event or used to invent earlier completion events.
