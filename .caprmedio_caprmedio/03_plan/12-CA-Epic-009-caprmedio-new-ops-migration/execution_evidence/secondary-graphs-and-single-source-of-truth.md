# Secondary graphs and Single Source of Truth

Source-only amendment implementing the Operator's approved distinction between authoritative sources and secondary graph Projections. This is derived change evidence, not an authoritative Journal event or a Task completion record.

## Decisions represented

- Single Source of Truth is now explicitly defined per independently maintained fact and applicable context. The existing DRY Principle and project Core Method remain unchanged.
- Atoms carry governing Claims and declared source Relations; Structural Entities and Journals retain authority for their own structural and recorded historical facts.
- Secondary graphs are non-authoritative Projections. Their connections may be internal, cross-graph, or directed to authoritative sources, subject to admitted Relation Kind authority.
- Every Relation Kind retains one graph-kind owner. Referencing another graph does not transfer that ownership or silently import its nodes.
- An authored Relation fact has one source declaration. A permitted derived Relation traces to its derivation authority and authoritative input facts, without inventing a direct declaration for its computed result.
- Terms/Entities Graph selection and Evaluation rules distinguish native membership from admitted external references. Explicit NARROWER_THAN source declarations, graph-specific checks, and selection limits remain required.
- A Graph of Graphs describes composition; it does not by itself require an additional generated overview Artifact.
- No concrete Relation Kind names, new YAML relation carriers, generators, or Tools were introduced.

## Changed Atoms

| Atom ID | Change | Current version | Summary |
|---|---|---|---|
| CA-R-1470 | Added | 1 | define single source of truth |
| CA-R-1471 | Added | 1 | keep secondary graphs derived from source authority |
| CA-R-1472 | Added | 1 | admit typed secondary graph connections |
| CAPRMEDIO-META-REQU-657 | Revised | 12 | define projection artifact form |
| CA-R-1246 | Revised | 7 | keep relation vocabularies graph specific |
| CA-R-806 | Revised | 17 | register complete relation kind metadata |
| CA-R-1437 | Revised | 2 | keep one source for each relation fact |
| CA-R-1408 | Revised | 3 | define graph of graphs |
| CA-R-1335 | Revised | 8 | define terms graph |
| CA-R-1438 | Revised | 3 | define entities graph |
| CA-R-1454 | Revised | 3 | derive governed terms views from selected authority |
| CA-R-1456 | Revised | 3 | derive entities views from selected authority |
| CA-M-120 | Revised | 10 | compile the direct relation registry |
| CA-E-382 | Revised | 14 | validate terms graph |
| CAPRMEDIO-GOV-EVAL-005 | Revised | 13 | canonical relation validity |
| CA-E-466 | Added | 1 | validate single source of truth in secondary graphs |

## Verification

- All 16 current source Carriers parsed and matched the intended content.
- All 12 prior versions were archived byte-for-byte.
- Existing Atom identities and Summary values were preserved.
- Changed Atom IDs resolve to one active source Carrier each; new authority references resolve.
- The other 11,699 checked files and the Git index remained unchanged from the current-turn baseline; `.DS_Store` files were ignored.
- Whitespace checks passed.
- Evaluation cases were added or revised as source authority. This does not claim that runtime validators implement or pass them.

The [change map](secondary-graphs-and-single-source-of-truth.projection.json) contains exact source/archive paths and digests.

## Remaining boundaries

The deferred cardinality Concern CA-C-108 was not changed or resolved. Generic source uniqueness does not establish a universal number of R/D Atoms per Entity.

Applicable Methodology outputs, source-selection snapshots, runtime Tools, installed hooks, settings, existing Journal records, and Task/Epic status were not changed. Follow-up compilation and Tool alignment remain separate work. This report does not replace authoritative historical recording or assert retrospective completion events.
