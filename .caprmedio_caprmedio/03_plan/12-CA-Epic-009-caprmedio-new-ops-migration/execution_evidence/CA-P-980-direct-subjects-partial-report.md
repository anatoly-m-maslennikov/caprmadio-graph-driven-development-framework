# CA-P-980 direct Subjects: partial implementation

This is non-authoritative execution evidence for the approved direct Subjects subset. CA-P-980 remains Active: its full Definition of Done is not met. Graph ownership and Process composition/control-flow relations remain unresolved. This stage does not execute CA-P-981, CA-P-984 or CA-P-992.

The Operator accepted `subjects: {governs: Subject1, depends_on: [Subject2, Subject3]}` after the explanation that this shape directly references canonical Entity, Action or Process targets, with no intermediate Subject/Entity or Subject/Reference Property and no repeated target-kind field. The exact approval was “yes. continue”. This supersedes the previously proposed Subject/Reference rename. The previous flow-graph correction remains in force: “not just ordered, it's flow diagram, each node is some action - doer, finder, checker/test, quality gate eval, ect”.

All 13 live Project Principles were read. DRY (M002), necessary complexity (M005), coherence (M006), original Operator authority (P033), and checkable commitments (E001) support the implemented direct-reference subset. The settled subset is at 99% confidence; these Principles do not determine the remaining exact graph-kind and flow-relation names.

## Implemented authority

R1198 defines Subjects as the Atom Property containing direct GOVERNS and DEPENDS_ON references. R1275 defines Subject as the canonical target referred to by one such link; being a Subject creates no separate link-object identity or bearer dependency on its Atom. R1199 retains governance and R1200 retains non-governing dependency. Subject DEPENDS_ON does not establish Process execution order and remains distinct from `relations.depends_on`, the Artifact/Task prerequisite relation.

R1201 retains exactly one direct GOVERNS target. R1278 permits zero or more distinct direct DEPENDS_ON targets. R1202 retains the independent integrity rule that every direct value resolves to exactly one canonical target in the Entity, Action or Process domain, and now governs Atom/Subjects instead of the redundant Atom/Subjects/Subject/Entity path. R1276 constrains the direct relation kind, without a Property on a separate Subject object. No source identity is retired or replaced; five misleading Summary/filename slugs change with their existing identities preserved.

R1248 explicitly excludes Action and Process identities from Entity. This changes neither Actor nor Carrier classification and does not exclude all operational things from Entity. R1194/R1321 admit the three direct target domains while retaining registered qualification constraints. M228 preserves bearer and allowed-value semantics for qualified Subject Paths; it does not authorize arbitrary Property paths on Actions or Processes. Terms remain Project-specific words or phrases under unchanged R1318; they neither replace Subject targets nor become executions.

R1203/R1279/R1280/R1363/R1014 and M114/M125/M232 reconcile their selected Entity-only or link-object wording with the approved model. R1014's pre-existing `child_of: CA-R-1013` edge was removed because R1013 is present only as an Archived prior rule requiring one or more Subjects; the valid R919 parent remains. R1363 still has its existing R1195 temporal-authority parent. That remaining dependency is explicitly deferred to P984's temporal retirement.

D269 defines the flat representation for every new or migrated Markdown Atom Carrier: `subjects.governs` is one scalar Subject Path; `subjects.depends_on` is an unordered collection of unique scalar Subject Paths and may be omitted when empty. Existing unmigrated temporal Carriers are admitted only until their separately assigned carrier-migration Task executes. This exception is migration-limited, not a second canonical representation. Only the 24 selected source Carriers adopt flat Subjects here. The P980 Task administration Carrier retains its existing compatibility encoding. Temporal classification carriers and all bulk conversions remain with their later Tasks.

E240/E246/E444 reconcile scoped validation and terminology checks. The no-duplicate-kind rule applies to Atom Subjects source encoding; a Projection may derive target classification from canonical authority when its own Spec requires it, without independently maintaining that classification. The reusable Action and Process definitions R1452/R1453 remain byte-identical; target references reuse their canonical meanings. This stage does not define actual executions, Journal responsibilities, Actor policies, or reusable operational procedures.

## Validation and preservation

Twenty-one non-authoritative semantic fixtures passed in a local deterministic fixture harness. The harness uses an explicit sample canonical-target registry to check the approved shape and target-domain rules; it does not claim an implemented framework validator, runtime support, or full graph-schema conformance.

| Fixture | Expected result |
|---|---|
| Entity direct target | accept; passed |
| Action direct target | accept; passed |
| Process direct target | accept; passed |
| Qualified Entity target | accept; passed |
| Missing GOVERNS | reject; passed |
| Multiple GOVERNS values | reject; passed |
| Unresolved target | reject; passed |
| Ambiguous target | reject; passed |
| Entity and Action share one identity | reject; passed |
| Term substituted for target | reject; passed |
| Execution substituted for definition | reject; passed |
| Intermediate Entity wrapper | reject; passed |
| Intermediate Reference wrapper | reject; passed |
| Repeated target kind | reject; passed |
| Duplicate DEPENDS_ON value | reject; passed |
| Scalar DEPENDS_ON value | reject; passed |
| Legacy carrier without migration compatibility | reject; passed |
| Legacy carrier with migration compatibility | accept; passed |
| Flat and legacy direct facts are identical | equal; passed |
| Dependency list order never supplies Process flow | equal without execution order; passed |
| Different Atoms reuse one canonical Action identity | same identity; passed |

Manual source review confirms distinct claims, one governed target per selected Atom, preserved Term/Actor/Carrier boundaries, and unchanged Task prerequisite completion semantics. Qualified paths remain subject to their existing graph relation endpoint rules. Process flow loops and forbidden Artifact prerequisite cycles are not conflated; the new Process flow relation schema and its full fixtures remain unresolved and are not claimed as validated by this stage.

Deterministic checks confirm 24 modified Active CORE_META_MODEL sources, 1,535 unchanged sources in the 1,559-source current frontier, 677 Active CORE_META_MODEL sources, all 53 excluded Drafts unchanged, and exact prior bytes in 25 new archives (24 sources plus P980). All 8,321 pre-existing archive files in the admitted Project/source roots remain byte-identical; the count excludes ignored .DS_Store entries. The P976 freeze, TOOLS snapshot, and all P977–P979 reports/maps remain unchanged. YAML, exact identity/version preservation, valid renamed Carrier targets, direct relation target resolution, one governed target, and scoped whitespace checks pass.

P980 Version 2 preserves its identity, dependency on Done P979, Assignee, Operator and confidence threshold; its Details now state explicit Process flow and the approved direct Subjects model. It remains in its Active location. No completion move or Done status is asserted.

The immutable partial changed-source map records every before/successor/archive path, version and digest. Its own digest is bound by its canonical Journal event, avoiding self-digest recursion. The Journal batch covers 52 completed file changes and 16 honest present-time predecessor recoveries; nine exact existing sealed predecessor events are reused. Recovery times describe the current recovery observation, not historical authorship or execution times. The batch preserves all pre-existing Journal bytes and the recorded index/staged-name digests. D335 Git materialization remains pending; no staging, unstaging, commit, push, Runtime/code/Settings change or generated Applicable Methodology rebuild is claimed.

## Remaining CA-P-980 decision

GOVERNS and DEPENDS_ON still need one explicitly admitted graph-kind owner and complete graph-qualified metadata under R1246/R806. Entities Graph (R1438) admits Entity nodes, and the accepted model excludes Action/Process targets from that domain. Terms Graph (R1335) owns wording relations, while General Artifact Graph (R1409) locates governed Artifacts by Carrier; none currently supplies the required mixed-domain Subject relation owner.

The recommended next decision is a dedicated Atom Subjects Graph owning direct GOVERNS and DEPENDS_ON links from Atoms to their canonical Entity, Action or Process targets, with graph nodes retaining references to existing identities. This recommendation is not admitted authority. Process composition and control-flow graph ownership, exact relation names, endpoint domains, direction, cardinalities, contributions and full flow/cycle fixtures remain subsequent P980 work. No speculative graph kind or flow relation is created in this partial stage.
