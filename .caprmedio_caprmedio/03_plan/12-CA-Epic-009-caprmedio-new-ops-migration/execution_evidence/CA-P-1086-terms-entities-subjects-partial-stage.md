# Terms, Entities, and Subjects

Non-authoritative source-change evidence. Updated 2026-09-14 04:00:22 +0400. CA-P-1086 remains Active.

## Accepted distinction

- Entity: the canonical model object identified by a qualified path.
- Subject: the GOVERNS or DEPENDS_ON Relation from an Atom to its canonical target, not the target or a separately identified intermediate node.
- Term: each named component used to construct the target path. Defining Claims, not path occurrences, own Term meanings.

In `Atom/Content Role: Requirement/Type: Demand`, the five named components reference Terms, the complete path identifies one target, and a source Atom's GOVERNS link to that target is one Subject. Slash and colon retain their existing graph-qualified structural interpretation; they are not Term names. Reusing a target from two Atoms creates two Subject Relations, not two copies of the target.

Existing Action and Process target domains remain separate from Entities and remain permitted. The Operator's Entity example does not remove them or create Entity duplicates.

## Revised source Atoms

| Responsibility | Revised Atoms |
|---|---|
| Subject is the Relation; Subjects Property records links | R1275 v8; R1198 v8 |
| Governed Subject is the GOVERNS link; splitting counts governed targets | R1363 v6; R1203 v7 |
| Paths identify targets and use named Term components | R1321 v6; R1194 v8 |
| Definition Claims own meanings; Subjects identify defined targets | R1279 v8 |
| Assign links and write qualified target paths | M125 v15; M228 v8 |
| Extract every referenced Term without inventing definitions | M114 v15 |
| Subject links are graph edges, not target or intermediate nodes | R1281 v6; M232 v8 |
| Separate Relation, target, path, and Term validation | E246 v14; E383 v7; E444 v6 |
| Existing YAML keys encode Relation Kinds; values encode target paths | D269 v8 |

R1318's existing Term definition and R1248's existing Entity definition already support the distinction and remain unchanged. R1279 retains exact target/terminal-name alignment for Definition Atoms; M114 must confirm it against the defining Claim instead of treating an arbitrary terminal name or all path components as definitions. The other components reference their own defining Claims.

Ordinary English remains allowed in prose; an ordinary word cannot silently substitute for a required Term reference in a named Subject Path component. Missing defining authority is a gap to report, not authority to synthesize a definition. Scope Unit names, identifiers, and syntax outside that component context do not automatically become Terms.

R1363's obsolete dependency on R1195 was removed. This does not execute the separately assigned retirement of all temporal-axis authority. GOVERNS/DEPENDS_ON cardinalities and graph-qualified Relation Kind ownership remain unchanged. No new Subject ID, wrapper, target-kind field, Entity alias, Relation Kind, or dictionary source was introduced.

## Verification

- 16 source revisions and 16 byte-identical previous-revision archives.
- All 16 Summary/H1 values and assigned Atom IDs are unchanged.
- Live YAML parses, Evaluation targets resolve, and whitespace checks pass.
- 1,563 other active source Atoms, 53 excluded Drafts, and 18 prior source maps are unchanged.
- Active source frontier remains 1,579.
- Target/Relation conflation patterns were checked across active methodology source content.
- The Evaluation Atoms now include the Operator's five-component example and failures for conflating links, targets, complete paths, and Terms.

These checks validate the source amendment, not runtime enforcement or complete validity of every existing Subject value.

## Boundaries and remaining work

No Tool changes, compilation, installation, Settings changes, Journal appends, commits, or pushes. The existing Tool files, Journal, and Git index retain their baseline bytes. Canonical materialization stays deferred under the Operator's meta-model-first decision; this report and map are not an alternative authoritative Journal and claim no historical completion events.

Existing Subject values are not bulk-migrated in this amendment. Broader M/O role extraction remains with its existing Tasks. CA-P-1086 records this bounded update at v13 and remains Active; M114's selected terminology-source disposition is addressed, while nine other reserved sources and final consistency checks remain. Other Tasks are not executed or closed.
