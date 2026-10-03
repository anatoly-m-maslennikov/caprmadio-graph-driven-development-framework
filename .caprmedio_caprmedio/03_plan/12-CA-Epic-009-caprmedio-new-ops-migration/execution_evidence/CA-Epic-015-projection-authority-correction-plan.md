# CA-Epic-015 — Source and Projection correction

Non-authoritative plan-change evidence, 2026-09-13 04:38:30 +0400. Planning only; no source Atom or Task execution is included.

The Operator corrected the model: source Atoms remain authoritative for the model facts; the Entities Graph is itself a Projection. Multiple graph views and other Projections may derive from the same source, including through another Projection, without becoming independent sources of truth. Claims about a Projection must govern the appropriate Projection Entity, not merely the Entity represented in it.

## Sequence

P1081 Done -> P1086 correction -> P1082 Subject links -> P1083 composition -> P1084 Carriers -> P1085 closure -> parent review -> remaining P980.

Added P1086 as the first unexecuted Task. It reviews the specific R1438/R1456 issue and analogous Terms Graph, terminology, Subject Projection and composed-view authority. It resolves exact Subject Paths rather than guessing a new taxonomy and records any transfer from the frozen P1078 ownership inventory. The earlier completion reports/maps remain immutable evidence of their original execution, not proof that this later correction has already been applied.

P1082 now depends on P1086 and requires fresh review of its unexecuted proposal. P1084 consumes the correction when specifying Carriers. P1085 explicitly fails closure if the source-versus-Projection confusion survives. P1083 changes navigation prefix only. The resulting main Epic has 111 Tasks and one chain of 110 prerequisite edges; no Task is executed or marked Done here.

The proposed per-Entity R/D limits and M/E cardinalities remain undecided. This plan does not turn the rejected misclassification example into cardinality authority, introduce artificial Entities to meet a quota, or approve the separate M232 commit-before-archive exception. No source, generated Projection, settings, Tool, runtime implementation, prior evidence or previous archive is changed. All current admitted source hashes and prior unrelated files are checked against the verified P1081 baseline. Exact prior Task versions are archived; Journal records this administrative change separately. Git index and existing staged changes remain untouched.
