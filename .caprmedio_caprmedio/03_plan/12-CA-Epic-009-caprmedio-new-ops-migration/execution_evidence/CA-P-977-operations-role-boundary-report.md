# CA-P-977 Operations role boundary

Execution evidence, not source authority. This Task applies the accepted Operations boundary only to Active CORE_META_MODEL role definitions and directly conflicting classification authority admitted by CA-P-976. Its predecessor CA-P-976 is Done. Current Project Principles were read first; the accepted Operator decisions governed the changes. Confidence in this bounded application is 99%.

Fifteen source Atoms retain their identities, authority owners, paths, Content Role R, Local/Global Tiers, Subjects and relations. Each Version increases by one and each exact previous byte sequence is preserved in a newly added archive carrier. Existing archive/history bytes are not rewritten. Existing filename and Subject spelling `Ops` is retained for the later carrier phase; CA-R-1344 explicitly identifies Operations as Ops, letter O, without adding a Content Role.

| Source identity | Revision | Applied boundary |
|---|---|---|
| CA-R-1282 | 3 → 4 | Classify primary contribution; mentioning an Operation or Actor alone does not assign O; a meta-model role definition may remain R. |
| CA-R-1288 | 3 → 4 | RMED is Spec for Implementation; O definitions/policies and executions are outside that Spec. |
| CA-R-1338 | 3 → 4 | P remains intended Task or Objective content. |
| CA-R-1340 | 3 → 4 | M supplies Implementation choices and conventions, not authoritative operational sequences. |
| CA-R-1344 | 4 → 5 | O supplies reusable Action/Process behavior and Actor participation/authorization policies; definition, execution and Journal Record are distinct. |
| CA-R-855 | 9 → 10 | Principle classification reflects the accepted operational-policy boundary rather than assigning Actor permissions to P. |
| CAPRMEDIO-META-REQU-091 | 12 → 13 | The normative RMED specification targets Implementation and is distinct from O authority and executions. |
| CAPRMEDIO-META-REQU-092 | 12 → 13 | Separate RMED, O, Implementation, execution/evidence and verification authority. |
| CAPRMEDIO-META-REQU-093 | 9 → 10 | Preserve factual/interpretive separation with execution records distinguished from O definitions. |
| CAPRMEDIO-META-REQU-094 | 11 → 12 | Evaluation implementations and factual outcomes remain attributable; outcomes are Journal evidence, not O definitions. |
| CAPRMEDIO-META-REQU-095 | 10 → 11 | Preserve optional product framing and distinguish observed outcomes from reusable Operations definitions. |
| CAPRMEDIO-META-REQU-114 | 13 → 14 | Reconcile the cross-role boundary; procedural Implementation code is permitted. |
| CAPRMEDIO-META-REQU-143 | 8 → 9 | Operational events and state evidence are carried by Journal Records, distinct from Operations authority. |
| CAPRMEDIO-META-REQU-170 | 8 → 9 | Operations lifecycle concerns reusable authority; factual history remains preserved. |
| CAPRMEDIO-META-REQU-640 | 8 → 9 | Recurrence-check outcomes are recorded in the Journal, distinct from reusable behavior. |

The exact source paths, prior/new Versions and SHA-256 values, archive paths and rationale are in `CA-P-977-changed-source-map.projection.json`. This map includes the Task move/archive and this report; the map's own digest is recorded by its canonical Journal file-change event.

Semantic review of the resulting source authority passed these cases:

| Claim or artifact | Boundary result and authority |
|---|---|
| A reusable operational Action or Process behavior | O: CA-R-1344. Atomic subdivision and Process composition details remain CA-P-978/979. |
| An Actor participation or authorization policy | O: CA-R-1344 and CA-R-855; actual project policies remain unchanged for later migration. |
| One intended Task or Objective | P: CA-R-1338. No Plan-to-Process rename. |
| Library selection or code convention | M: CA-R-1340. |
| A meta-model definition describing Operations | May remain R according to primary contribution: CA-R-1282/1288. |
| A Requirement that merely mentions an Actor or Operation | Mention alone does not assign O: CA-R-1282. |
| A particular execution and its resulting state/evidence records | Execution and Journal Record remain distinct from reusable O and RMED Spec: CA-R-1344, META-REQU-092/143/170. |
| Procedural Tool Implementation | Permitted as Implementation: META-REQU-114; canonical procedure authority remains O. |

Deterministic checks passed: all 1,557 frozen entries were compared against current file bytes; precisely these 15 changed and the other 1,542 remain identical. All 53 excluded Draft digests remain identical. Every prior-version archive matches its frozen SHA-256. All 15 source frontmatters remain byte-identical after removing only Version and updated_at lines; therefore identity, Subjects, relations, Type carriers and ownership did not change. YAML syntax parsing and scoped whitespace checks pass.

All source successor paths equal their predecessor paths, so existing identity and filename references resolve to the same source carrier; no incoming reference rewrite is required. The Task moves to `done/` at Version 2 with its original Version 1 archived. Later Tasks retain their identity-based dependency on CA-P-977. No new Atom identity, O carrier or Scope Unit was created.

Deferred successors remain explicit: CA-P-978/979 define Action atomicity and Process composition; CA-P-980 defines relations; CA-P-981/982 finish Actor and Task/Tool-use authority; CA-P-983 defines the two Journal responsibilities; CA-P-984 removes temporal classification authority; CA-P-985/986 review and migrate the procedural RMED corpus; project-content and carrier phases migrate approved Actor policies and carrier fields. References to Ops evidence in that deferred corpus are not a claim that its migration is complete. Generated Applicable Methodology copies, projections, tool code, installation and settings values are untouched.

The Definition of Done falsifying condition is false for this Task's selected role-definition/classification boundary. Source/Task/evidence changes receive canonical schema-3 Journal provenance. Fifteen missing exact prior-path/hash Journal states are recovered only as observed predecessor states, grounded in the frozen CA-P-976 inventory and exact preserved bytes; prior original actor, time and intent are not fabricated. Existing sealed Journal lines are preserved. CA-D-335 Git materialization remains pending: the pre-existing index contains unrelated staged work and was not changed; no staging, unstaging, commit or push is claimed.
