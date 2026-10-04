---
atom_id: CA-C-324
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Harvest proof schema assumptions"
  depends_on:
    - "Artifact"
version: 2
updated_at: "2026-10-04 11:48:37 +0000"
relations:
  concern_about:
    - CA-P-1118
    - CA-A-1036
    - CA-P-1305
    - CA-A-1023
    - CA-P-1306
    - CA-A-1024
    - CA-P-1308
    - CA-A-1026
---
# Summary

Correct harvest proof schema assumptions

## Concern

The root's bounded native/saved proof initially expected original_parts in every future selected binding record. P1308 correctly binds those records by exact native metadata while retaining full required antecedents and first/following originals. A conditional repair of the proof then produced an invalid Python semicolon before if.

## Evidences

The first proof returned nonzero after the independently successful P1301 proof, raising KeyError for a future metadata-only selected record. The syntax-invalid attempt returned nonzero without any executed proof. Neither failed attempt was counted as a worker proof or source-reading pass.

The corrected proof requires complete original_parts/full_text for every saved A1024 source record and all full saved contexts; it permits exact metadata-only future selected records and opens each directly from its frozen native source. It verifies raw/text/role/time fingerprints, prefix hashes, per-source/global aggregates, all98 substantive dispositions, current/next disjointness and full following frontier. Both the current98/context2 and next60/context2 native/saved proofs then passed. No missing source originals or Tool implementation defect was inferred.

## Blast radius

The first checkpoint 93 recovered-state preparation used an over-escaped numeric Version regex and stopped before any Journal append with an AttributeError. Replacing the ephemeral regex with an explicit digit class recovered all 47 actual Version values. The existing Journal API then appended exactly 47 sealed recovered-state events; predicted receipts, reopened NDJSON records/digests and actual saved bytes versus commit fc6e569608a40cfc8499ca84f6f4cf77df3e4174 all matched. No failed invocation was a receipt, save-Tool completion or delivered Tool change.

The checkpoint 93 save whitelist comparison initially counted Git's rename-collapsed listing as 47 paths against 51 explicit old/new paths and stopped before committing. The exact staged paths are correct: disabling rename detection exposes all 51 owned paths, including four former Active carriers and their Done destinations. That comparison passed with no unrelated staged paths. No unstage, reset, discarded change or false commit receipt occurred.

Checkpoint 93 metadata preparation used an incorrect frontmatter delimiter position, so the ephemeral inventory command returned a traceback rather than JSON; the caller rejected it with a JSON parse error. No proof or absence was inferred. The corrected lookup separates the opening delimiter explicitly and verifies the unique current path, status, Version and registered Details heading for all twenty assigned/current-next leaves and five shared parents. The complete shared registered-Carrier gate independently passed 167 Plans and 139 supporting Carriers without exclusions.

A later root preparation lookup for A1023 assumed every JSON fence was a mapping and raised AttributeError on its valid list-shaped authority ledger. The root rejected that failed lookup, added explicit mapping/list classification and reopened the entire non-evidence prose and JSON shapes successfully. The actual P1305/A1023 current8/context2, actual next1/context4, full native/raw/parts/text/metadata/prefix/aggregate and all23 current governing fingerprints passed. No saved schema change or source omission was inferred from the failed lookup.

Root integration for P1308/A1026 initially asserted literal equality between the metadata-only Plan selection and its completed Analysis binding, which correctly adds original_parts/full_text to all60 current selected records. The comparison failed before any proof was counted. A bounded schema comparison confirmed those are the only differences. The corrected diagnostic compares the identical selection metadata separately, then verifies the Analysis's complete originals directly against native sources; it does not remove originals, change evidence or infer a delivered Tool defect. The actual current60/context2 and next23/context8 native/saved parts/text/metadata/prefix/aggregate/disposition/disjointness/Done proof and34 current governing fingerprints passed. This is saved provenance, not another semantic recheck stage.

A post-restart report-shape lookup again assumed that the first JSON block was a mapping. A1036 correctly starts with its list of21 individual dispositions, so the lookup stopped with AttributeError before establishing any aggregate or proof. Explicit mapping/list classification recovered the metadata lookup and exposed each completed report's actual selected-record schema. The root did not rewrite the reports, count contexts or future bindings, or infer a framework Tool defect from this ephemeral failure. The shared registered-Carrier check passed165Plans/134supporting Carriers while the explicitly excluded unfinished leaves and Concerns retained their pending states; that scoped pass was not reported as a full-round pass.

Root integration provenance preparation/checking for P1305/A1023, P1306/A1024 and their actual next bindings. The saved source evidence and coverage did not change. This repairs ephemeral schema assumptions; it does not implement a framework Tool, add a semantic recheck stage, reset a leaf clock or hide an overrun.
