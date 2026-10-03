# CA-P-1079 — Governed Terms Graph authority

Non-authoritative execution evidence. Completed 2026-09-13 03:29:18 +0400. Scope: current admitted CORE_META_MODEL authority reserved by CA-P-1078; no later Task executed.

## Result

Done: the Task Definition of Done falsifier is false. Three source changes resolve G01/G02 from the P1078 inventory. The generic Terms Graph remains the same graph kind; governed-only is a requested selection view, not a new Entity, Term, graph-kind identity or independent source of truth.

| Atom | Version | Current SHA-256 |
|---|---|---|
| CA-R-1435 | 2 -> 3 | bc01b93c1f23faa5b18efb1760d45e817c7b699a929304ed20789b9ae3178233 |
| CA-E-382 | 10 -> 11 | 4d29bf7bad708983cc9d4f5a97852be8064ac526c162e247bc3c02a5cc322f13 |
| CA-R-1454 | new -> 1 | 32c6d2f4740c024cbf4bb9f3de4f03b11836fef3f0bb8917069b146ef35c646b |

- R1435: replace Entity-only classification with definition-supported implication about the same lowercase general-language referent. Terms naming Actions/Processes do not require Entity duplicates. Graph ownership, direction and exclusion of Property ownership/allowed-value membership are preserved.
- R1454: one General-tier Requirement for all-and-only selected Governed Terms and explicitly declared selected-source edges with included endpoints. Reuses R1319/M114 admission, R1335 graph identity and R1437 source authority. Exact node/edge Claim and revision traceability is required. No full-Project selection or implicit dependency closure is imposed.
- E382: enforce explicit declaration and supported implication rather than empty-instance reasoning; reject both under-inclusion and over-inclusion, missing/conflicting definitions, fabricated edges and missing exact provenance. An excluded endpoint makes an edge ineligible. Filtering a parent does not establish canonical Root Term status; insufficient evidence remains unresolved instead of importing outside sources.

Two exact pre-edit source Carriers are retained in their existing role archive directories at R1435@2 and E382@10. Three changed/new source Carriers use the accepted scalar governs and unique depends_on list. Their old temporal carriers are preserved in the exact archives, not rewritten. Author omission retains the declared default under D274; version and Project-time updated_at follow D270.

## Reuse and scope discipline

All 16 reserved sources were read; 14 remain unchanged. R126/R1318/R1319 own Term admission and one defining authority; R1335 remains the generic graph-kind definition. R1244/R1345/R1347 retain multi-parent, acyclic and Root Term rules. R1279/R1322/R1324/R1325 retain definition naming and composite-expression boundaries. M114 remains the existing name/meaning extraction mapping; M229 remains rendering authority. Their wider role/carrier review is not speculatively executed here. Shared E444 is unchanged and supplies the Project-specific-versus-general-language and target-versus-wording fixtures.

The selected-view Requirement is an independently adjustable constraint and therefore a separate Atom, not extra responsibility hidden inside R1335. General tier follows R1431 (derived-set constraints); no representation or particular reusable operational Process is specified. R1454 is the next unreused R identity after R1453, checked against governed source/Project/archive/Journal files and Git history names before allocation.

Project Principles read: all 13 current Principle Carriers. DRY (M002), necessary complexity (M005), coherence (M006), checkability (E001), Operator authority (P033) and graph-of-graphs (R1407) support source reuse, domain separation, explicit provenance, visible uncertainty and no invented edges. No Principle changed. Confidence for these bounded repairs is at least the Task threshold of 99%; no unresolved Operator decision is hidden by Task closure.

## Semantic fixtures

These are explicit synthetic authority scenarios reviewed against the listed current Claims, not a run of a Project graph generator or an assertion of executable implementation conformance. Operational-vocabulary examples declare their hypothetical definitions and edges only inside the fixture; they add no real source Atoms or taxonomy. All 26 have determinate expected outcomes supported by the updated/reused authority. Mechanical checks additionally verified current Claim anchors, YAML syntax, scalar/list Subjects, link targets, revision increments, exact archives and all preservation hashes.

| ID | Synthetic input | Reviewed disposition | Authority |
|---|---|---|---|
| F01 | Two uniquely defined Terms with an explicitly declared, definition-supported hierarchy edge. | Accept | R1435, R1454, E382 |
| F02 | Unrelated Terms have no observed Entity instances; a hierarchy edge is proposed from that absence. | Reject; absence is not implication evidence | R1435, E382 |
| F03 | Synthetic Finder Term is explicitly defined as an Action with a finding contribution; an explicit Finder-to-Action edge is declared. | Accept without creating an Entity duplicate | R1435, R1248, R1452, E382 |
| F04 | Synthetic Review Process is explicitly defined as a Process with a bounded review flow; its Term hierarchy edge to Process is declared. | Accept without creating an Entity duplicate | R1435, R1248, R1453, E382 |
| F05 | Every observed A instance currently also satisfies B, but A and B definitions do not imply this. | Reject hierarchy admission | R1435, E382 |
| F06 | Two active Definition Atoms give a displayed Term conflicting Project-specific meanings. | Reject; identify conflicting source definitions | R126, R1319, E382, E444 |
| F07 | A displayed Project-specific Term has no active Definition Atom. | Reject; report missing defining authority | R1319, E382 |
| F08 | An ordinary English word has consistent general usage but no Project-specific definition. | Exclude from governed-only view; general usage remains valid | M114, E444, R1454 |
| F09 | A capitalized word occurs in Subjects but no defining Claim establishes Project-specific meaning. | Do not admit as a Governed Term | M114, E444 |
| F10 | A complete composite Subject Path is proposed as one vocabulary Term. | Reject that Term admission | R1325, M114, E444 |
| F11 | Definitions support an implication, but no source Atom declares its hierarchy edge. | Do not display an authored hierarchy edge | R1437, R1454, E382 |
| F12 | An Entity bearer edge or allowed-value admission edge is inserted as a Terms Graph relation. | Reject wrong graph-kind ownership | R1246, R1435, E382 |
| F13 | A Term has two explicitly supported narrower-than parents and no cycle. | Accept; single-parent tree is not required | R1244, R1345, E382 |
| F14 | The hierarchy contains a self-loop or a multi-node directed cycle. | Reject | R1345, E382 |
| F15 | Source evidence establishes zero direct hierarchy parents for a uniquely defined Term. | Accept isolated Root Term | R1347, E382 |
| F16 | Requested selection excludes a separately defined out-of-selection Term and its source facts. | Accept omission; no forced full-Project graph | R1454, E382 |
| F17 | An eligible in-selection Term or eligible explicit in-selection edge is omitted. | Reject under-inclusion | R1454, E382 |
| F18 | A displayed node or edge has no exact source Claim/revision trace. | Reject | R1454, R1437, E382 |
| F19 | Two Atoms share Subjects; the display invents a Term hierarchy edge from that sharing. | Reject invented edge | R1435, R1454, E382 |
| F20 | A separately admitted expansion Relation Kind belongs to Terms Graph and satisfies its governing authority. | Do not reject merely for being an expansion | R1246, E382 |
| F21 | The view acquires independent vocabulary authority or a new graph-kind identity merely because selection is governed-only. | Reject | R1335, R1454, R1437 |
| F22 | An outside-selection Definition Atom is silently imported to add its Term node. | Reject over-inclusion | R1454, E382 |
| F23 | Both endpoint Terms are selected, but the displayed explicit edge is sourced outside selection. | Reject outside-selection edge | R1454, E382 |
| F24 | An in-selection Relation declaration has an excluded endpoint; its edge is omitted. | Accept omission; edge is not eligible | R1454, E382 |
| F25 | A parent is filtered out and its visible child is labeled canonical Root Term solely from display isolation. | Reject classification; retain known source classification or leave unresolved | R1347, E382 |
| F26 | A requested dependency closure is explicitly added to the declared source selection before derivation. | Evaluate that explicit selection; never silently enlarge it | R1454, E382 |

## Preservation and completion

- Reconstructed the admitted source frontier from P976 plus P977/P978/P979 and sealed P980-direct-Subjects maps. Before: 1,559 sources / 677 Core. After: 1,560 sources / 678 Core; only R1435/E382 changed and R1454 was added. The other 1,557 source bytes remain unchanged.
- All 53 excluded Drafts, 8,358 pre-existing archive Carriers, 17 prior evidence files and 109 other Tasks are unchanged. This Task alone moves Active v2 to done v3 with exact @2 archive.
- No Settings values, runtime, Tool implementation, generated Applicable Methodology, other scopes, prior maps, or later Task changes. No new D format or graph relation identity is invented.
- Raw Git index remains `54ec1294d1bd71d296f56bbef952eed63fe84f8d498bd4e1b93d04257db14e1b`; no staging, unstaging, commit or push. Git materialization remains pending separately.
- Append-only Journal events bind exact source/archive/evidence/Task results. Missing old-event provenance is recovered at current observation time from exact preserved bytes, never fabricated as past authorship/time. Receipts are returned separately after append, with prior Journal bytes preserved.

## Handoff

Execute only CA-P-1080 next, in its own dedicated subagent. Consume this source map after the sealed P980 map. P1080 owns general vocabulary and unresolved-candidate indexes; P1081 owns Entity qualification; P1082 owns backlinks; P1083 owns composition/registry; P1084 owns D; P1085 closes this sub-Epic. P980's Operation flow schema remains paused until that closure and parent review. P984 temporal authority retirement and later bulk Carrier migration are untouched.
