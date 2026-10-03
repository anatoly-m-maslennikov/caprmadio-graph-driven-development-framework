# Requirement connections and delta — DSET 0.3

Already accepted behavior is not redefined in this Change. The table connects
the implementation scope to its current layer-owned Requirement owners.

| Capability | Current Requirement owners |
|---|---|
| Framework-first self-hosting and bounded recursion | `CAPRMEDIO-REQUIREMENT-OPS-003`, `CAPRMEDIO-REQUIREMENT-TOOL-004` |
| Repository-owned rules, fail-closed ownership, customization, and one owner | `CAPRMEDIO-REQUIREMENT-GOV-014..017` |
| Separate test/eval proof | `CAPRMEDIO-META-REQU-185--separate-test-and-evaluation-proof` |
| Thin wrappers, local-rule following, lifecycle-mode entrypoints, runs, budget, continuity, shared runtime, and selectable implementation preparation | `CAPRMEDIO-REQUIREMENT-SKILL-002..009`, `CAPRMEDIO-SPEC-SKILLS-REQU-568--shared-skill-runtime`, `CAPRMEDIO-SPEC-SKILLS-REQU-570--implementation-mode-setting` |
| Release transaction, RC/final gate, and coordinated version identity | `CAPRMEDIO-REQUIREMENT-OPS-004..007` |
| Intake routing and stable layer-qualified IDs | `CAPRMEDIO-REQUIREMENT-GOV-018..019` |
| Neutral repository or Work Area scope | `CAPRMEDIO-META-REQU-189--work-area-scope` |
| Atomic authority, compiled projections, absorption, commit provenance, and session provenance | `CAPRMEDIO-REQUIREMENT-GOV-020..022` |
| Governance constitution, dependency/precedence separation, and authority/evaluation boundary | `CAPRMEDIO-REQUIREMENT-GOV-023` |
| Generated project health and portable Markdown rendering | `CAPRMEDIO-REQUIREMENT-GOV-024`, `CAPRMEDIO-REQUIREMENT-TOOL-018` |
| Independent external review packet/report and explicit finding reconciliation | `CAPRMEDIO-REQUIREMENT-GOV-025` |
| One explicit or inherited priority for every governed artifact | `CAPRMEDIO-REQUIREMENT-GOV-026` |
| Workflow-independent Problem, Question, and Conflict semantics | `CAPRMEDIO-REQUIREMENT-GOV-027` |
| Recommended optional rationale for Decisions and other atomic artifacts | `CAPRMEDIO-REQUIREMENT-GOV-028` |
| Independent MECE artifact classification and Analysis Report boundaries | `CAPRMEDIO-REQUIREMENT-GOV-029` |
| Type-first artifact names and independently selectable subtype-name capability | `CAPRMEDIO-GOV-REQU-396--artifact-naming-setting` |
| Medium/high immutable-artifact admission strictness | `CAPRMEDIO-GOV-REQU-397--artifact-creation-setting` |
| Hidden control-plane root, one settings/manifest carrier, distinct ignored runtime state, disposable host scratch, explicit path bases, and direct ownership roots | `CAPRMEDIO-GOV-REQU-401--control-runtime-and-scratch-boundaries` |
| Current-only project control plane with inert historical aggregates and completed migrations outside skill discovery | `CAPRMEDIO-GOV-METH-037--keep-the-control-plane-current` |
| Repository legal files outside `.caprmedio`, with deterministic legal-only provenance resolution | `CAPRMEDIO-GOV-METH-002--keep-legal-files-outside-the-control-plane` |
| Executable product contracts in TOOL, development realization in IMPL, and post-implementation operation in OPS | `CAPRMEDIO-GOV-METH-039--place-executable-methodology-by-role`, `CAPRMEDIO-REALIZATION-METH-062--terminal-profile-features`, `CAPRMEDIO-FIELD-METH-075--operate-without-backward-implementation-authority` |
| Selected Local Python Tools environment, coding, QA-implementation, portability, dry-run, diagnostics, and visible documented-constant rules | `CAPRMEDIO-REALIZATION-REQU-582--local-python-tools-profile..003` |
| Repository text-byte configuration and portable code/path/Test realization | `CAPRMEDIO-SPEC-TOOLS-METH-052--portable-text-byte-policy`, `CAPRMEDIO-REALIZATION-METH-058--canonical-health-path-order..005` |
| Visibly ordered layer directories with stable logical layer IDs | `CAPRMEDIO-GOV-REQU-402--numbered-layer-directories` |
| Horizontal feature Contracts and forward-only layer authority | `CAPRMEDIO-GOV-REQU-403--forward-only-layer-authority` |
| One-level-down project/group/feature/layer architecture views | `CAPRMEDIO-GOV-REQU-389--multilevel-architecture-views` |
| Narrowest-common-scope ownership for project, group, feature, and layer truth | `CAPRMEDIO-GOV-REQU-390--project-scope-ownership` |
| Parent-to-child artifact inheritance, local implementation/cancellation, and direct fallback | `CAPRMEDIO-GOV-REQU-391--artifact-inheritance` |
| Many-to-many child-owned lineage and derived reverse/transitive traceability | `CAPRMEDIO-GOV-REQU-392--artifact-lineage` |
| Six flat Version lifecycle subtypes | `CAPRMEDIO-REQUIREMENT-OPS-013` |
| Role-aware handling for every governed conflict pairing, with priority selection only where permitted | `CAPRMEDIO-REQUIREMENT-TOOL-019` |
| Evidence-derived TypeScript candidate profile and promotion boundary | `CAPRMEDIO-SPEC-TOOLS-REQU-551--typescript-candidate-profile` |
| Framework-reference versus project-applied TypeScript profile authority | `CAPRMEDIO-SPEC-TOOLS-REQU-552--typescript-profile-instantiation` |

The canonical text lives in the accepted META, GOV, TOOL, SKILL, IMPL, and OPS
evergreen package fragments under `.caprmedio/100_LAYER_1_META/` through
`.caprmedio/600_LAYER_6_FIELD/`. This Change
owns implementation and proof for those accepted requirements, not duplicate
normative prose.

Connected accepted IDs are `CAPRMEDIO-META-REQU-185--separate-test-and-evaluation-proof`,
`CAPRMEDIO-META-REQU-189--work-area-scope`, `CAPRMEDIO-REQUIREMENT-TOOL-004`,
`CAPRMEDIO-REQUIREMENT-GOV-014`, `CAPRMEDIO-REQUIREMENT-GOV-015`,
`CAPRMEDIO-REQUIREMENT-GOV-016`, `CAPRMEDIO-REQUIREMENT-GOV-017`,
`CAPRMEDIO-REQUIREMENT-GOV-018`, `CAPRMEDIO-REQUIREMENT-GOV-019`,
`CAPRMEDIO-REQUIREMENT-GOV-020`, `CAPRMEDIO-REQUIREMENT-GOV-021`,
`CAPRMEDIO-REQUIREMENT-GOV-022`, `CAPRMEDIO-REQUIREMENT-GOV-023`,
`CAPRMEDIO-REQUIREMENT-GOV-024`, `CAPRMEDIO-REQUIREMENT-GOV-025`,
`CAPRMEDIO-REQUIREMENT-GOV-026`, `CAPRMEDIO-REQUIREMENT-GOV-027`,
`CAPRMEDIO-REQUIREMENT-GOV-028`,
`CAPRMEDIO-REQUIREMENT-GOV-029`,
`CAPRMEDIO-GOV-REQU-389--multilevel-architecture-views`, `CAPRMEDIO-GOV-REQU-396--artifact-naming-setting`,
`CAPRMEDIO-GOV-REQU-397--artifact-creation-setting`,
`CAPRMEDIO-GOV-METH-037--keep-the-control-plane-current`,
`CAPRMEDIO-GOV-METH-002--keep-legal-files-outside-the-control-plane`,
`CAPRMEDIO-GOV-METH-039--place-executable-methodology-by-role`,
`CAPRMEDIO-GOV-REQU-401--control-runtime-and-scratch-boundaries`, `CAPRMEDIO-GOV-REQU-402--numbered-layer-directories`,
`CAPRMEDIO-GOV-REQU-403--forward-only-layer-authority`,
`CAPRMEDIO-GOV-REQU-390--project-scope-ownership`,
`CAPRMEDIO-GOV-REQU-391--artifact-inheritance`,
`CAPRMEDIO-GOV-REQU-392--artifact-lineage`,
`CAPRMEDIO-REQUIREMENT-TOOL-018`,
`CAPRMEDIO-REQUIREMENT-TOOL-019`,
`CAPRMEDIO-SPEC-TOOLS-REQU-551--typescript-candidate-profile`,
`CAPRMEDIO-SPEC-TOOLS-REQU-552--typescript-profile-instantiation`,
`CAPRMEDIO-REQUIREMENT-SKILL-002`, `CAPRMEDIO-REQUIREMENT-SKILL-003`,
`CAPRMEDIO-REQUIREMENT-SKILL-004`, `CAPRMEDIO-REQUIREMENT-SKILL-005`,
`CAPRMEDIO-REQUIREMENT-SKILL-006`, `CAPRMEDIO-REQUIREMENT-SKILL-007`,
`CAPRMEDIO-REQUIREMENT-SKILL-008`, `CAPRMEDIO-REQUIREMENT-SKILL-009`,
`CAPRMEDIO-SPEC-SKILLS-REQU-568--shared-skill-runtime`, `CAPRMEDIO-SPEC-SKILLS-REQU-570--implementation-mode-setting`,
`CAPRMEDIO-SPEC-TOOLS-METH-052--portable-text-byte-policy`,
`CAPRMEDIO-REALIZATION-METH-062--terminal-profile-features`, `CAPRMEDIO-REALIZATION-METH-058--canonical-health-path-order`,
`CAPRMEDIO-REALIZATION-METH-059--platform-native-verification-placeholder`, `CAPRMEDIO-REALIZATION-METH-060--canonical-filesystem-path-boundary`,
`CAPRMEDIO-REALIZATION-METH-061--deterministic-git-fixture-bytes`, `CAPRMEDIO-REALIZATION-REQU-582--local-python-tools-profile`,
`CAPRMEDIO-REALIZATION-REQU-583--portable-dry-run-and-diagnostics`, `CAPRMEDIO-REALIZATION-REQU-584--place-and-explain-settings-and-constants`,
`CAPRMEDIO-FIELD-METH-075--operate-without-backward-implementation-authority`,
`CAPRMEDIO-REQUIREMENT-OPS-003`, `CAPRMEDIO-REQUIREMENT-OPS-004`,
`CAPRMEDIO-REQUIREMENT-OPS-005`, `CAPRMEDIO-REQUIREMENT-OPS-006`,
`CAPRMEDIO-REQUIREMENT-OPS-007`, and `CAPRMEDIO-REQUIREMENT-OPS-013`.

## ADDED — CAPRMEDIO-SPEC-SKILLS-REQU-570--implementation-mode-setting Selectable implementation preparation

Public skills accept a desired outcome rather than requiring the operator to
invoke every prerequisite skill manually. Repository-local lifecycle rules own
entry criteria, allowed prerequisite workflows, exit criteria, and stops. Each
transition must satisfy a missing criterion and re-read authority; no progress,
repeated state, cycles, ambiguity, failure, or a new authorization boundary
stops the finite closure.

`.caprmedio/caprmedio_settings.toml` selects `workflows.implement.mode`. Lazy mode invokes
`decisions` first, conditionally prepares separate Test/Evaluation and
implementation plans, and implements only after all entry criteria are
satisfied. Strict mode performs implementation only and stops on missing
accepted prerequisites. Session history is candidate evidence rather than
authority, so reconciliation never invents acceptance or edits immutable atoms.

## ADDED — CAPRMEDIO-REQUIREMENT-GOV-029 MECE artifact classification

Every governed carrier must have one primary artifact type and at most one
allowed direct artifact subtype, independently from the four semantic Types.
The project-local artifact-type registry owns the eleven development roles,
their primary questions, direct subtypes, fallback behavior, and path rules.
Analysis Report is non-authoritative and permits Solution Landscape,
Root-Cause Analysis, Proposal, Technical Investigation, and External Audit
Analysis. Unknown, mismatched, nested, missing, or ambiguous classifications
fail closed.

Roadmap, Version Scope, Change, Release Plan, Readiness Record, and Release
Record are direct subtypes of Version and share the `VERSION` identity
sequence for newly emitted carriers.

**Scenario CAPRMEDIO-SCENARIO-GOV-030:** A Proposal recommends one candidate; a
separate Decision accepts it; Specification/Design compiles it; Evidence Record
captures a Test run; Verification assesses the evidence; and Readiness Record
makes the explicit release gate disposition without any workflow-derived
reclassification.

## ADDED — CAPRMEDIO-GOV-REQU-390--project-scope-ownership Structural-scope ownership

Every claim and compiled artifact belongs to the narrowest common structural
scope containing all affected owners and subjects. Project-level truth owns
only genuinely cross-child or whole-project concerns—shared outcomes and
requirements, Contracts and semantics, end-to-end QA, cross-cutting policy,
integration architecture, release/readiness, and cross-owner unresolved work.
High-level wording does not promote a child-owned claim, and parents link rather
than duplicate child detail.

## ADDED — CAPRMEDIO-GOV-METH-023--typed-artifact-relations Typed artifact relations

Consequential forward edges use `child_of`, `analysis_of`, `projection_of`,
`implementation_of`, `check_of`, `evidence_for`, `resolution_of`,
`override_of`, `replacement_of`, or fallback `relates_to`. Reverse edges are
derived and never authored. One source-target pair has one primary relation;
`child_of`, scoped `override_of`, and complete `replacement_of` never overlap.

Evergreen `projection_of` normally records one semantic-Type/exact-scope range
through a globally ordered immutable `ATOMIC-RECORD` frontier. A newer
applicable atom makes the projection stale. Sealed legacy `child_of` remains
compatibility input; new artifacts use `relations`.

## ADDED — CAPRMEDIO-REQUIREMENT-OPS-012 Integration delivery is the default

Every applicable DSET project must use its configured local integration branch,
remote integration branch, and integration-to-protected release PR as the base
delivery flow. A Change may opt into a separate branch-backed worktree when
parallelism, risk, or conflicting work needs stronger isolation. That branch
must integrate into the configured integration branch before release. Workspace
mode never changes Change identity, scope, authorization, or proof ownership.

**Scenario CAPRMEDIO-SCENARIO-OPS-013:** This repository works locally on `dev`,
pushes remote `dev`, and opens PR `dev` to `main`. A parallel high-risk Change
selects `branch-worktree`, reviews that branch into `dev`, and then participates
in the same protected release flow without creating a permanent layer branch.

## ADDED — CAPRMEDIO-REQUIREMENT-GOV-020 Artifact roles

DSET must classify durable artifacts as atomic authority sources, evergreen
compiled projections, transactional context/evidence, or implementation-layer
artifacts so reviewers do not confuse rationale, evidence, code, or generated
views with accepted source truth.

**Scenario CAPRMEDIO-SCENARIO-GOV-021:** An accepted Decision owns its atomic choice,
the spec and proof plans compile the current consequences, and implementation
cites the Decision without becoming authority. If projection and Decision
differ, the Decision wins and the projection is stale.

## ADDED — CAPRMEDIO-REQUIREMENT-GOV-021 Atomic-source compilation

Accepted, active, applicable Requirements, Contracts, Decisions, and other
normative atoms must compile their current behavioral consequences into the
owning evergreen specs, plans, runbooks, or governing rules. Atomic artifacts
are immutable; later state is append-only. A new atom may explicitly and
acyclically absorb older ones while preserving or replacing every applicable
consequence. Only a fully retired atom may move byte-for-byte to `archive/`.

**Scenario CAPRMEDIO-SCENARIO-GOV-022:** A resolved Question produces a Decision, the
Decision compiles into the relevant projection, and review rejects a code-only
change that leaves the spec stale. A successor Decision explicitly absorbs its
immutable predecessor rather than winning because it is newer.

## ADDED — CAPRMEDIO-REQUIREMENT-GOV-022 Commit and session provenance

Commits that change evergreen truth or implementation artifacts must cite the
Decision or Decisions they implement. A Problem, Question, QA atom, or Change
may be cited as additional provenance but never substitutes for authorizing
Decision authority. Newly emitted atomic artifacts and
append-only lifecycle events expose explicit unique host-prefixed
`llm_session_ids` when an LLM helped produce them, or an explicit empty/`none`
disposition for human-only work. Review, correction, and status changes emit
linked records instead of revising atoms. Missing provenance is invalid. The
rule applies to Changes, intake items, Decisions, promoted proofs, skill-run
records, and session checkpoints.

**Scenario CAPRMEDIO-SCENARIO-GOV-023:** A commit body contains
`Implements: CAPRMEDIO-GOV-METH-011--artifact-classes-compilation-and-provenance`, and the Decision artifact records the
Codex session IDs that produced or materially revised it.

## ADDED — CAPRMEDIO-REQUIREMENT-GOV-023 Governance constitution

`CAPRMEDIO-RULE-ARCHITECTURE` remains the sole dependency-free governance root.
Every rule declares separate acyclic dependency and conflict-precedence
relations. Rule authority comes from accepted active atomic sources compiled
into the applicable current local governing document; a mismatch selects the
source and makes the projection stale. Active Decisions explain and authorize
changes, provenance identifies origin, and tests/evals/reviews/evidence assess
evaluation without becoming authority.

**Scenario CAPRMEDIO-SCENARIO-GOV-024:** A precedence cycle or missing precedence
owner fails closed. Stale evidence leaves the affected evaluation claim stale
and blocks its relying gate without silently erasing the applicable rule.
