## Task, scope, and boundaries

Audit every current active Method and Evaluation beneath
`.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC`
for internal coherence, conflict, duplicated authority, missing policy or
coverage, Method applicability, Evaluation falsifiability and one-case
discipline, typed subjects and relations, and recursive alignment with the
active Project Principles and Applicable Methodology.

This is Call 2 of the requested sequence. Its predecessor is
`fpf-reports/20260901T183417Z-fpf-structure-recover-recover-programmatic-me-structure.md`.
The predecessor was refreshed after CA-M-238 appeared during this review.

### Audit contract

- Target state: the live working-tree edition observed on 2026-09-01.
- Included: 98 active Methods and 315 active Evaluations, including direct
  PROGRAMMATIC authority and the TOOLS, APPS, and MCP descendants.
- Excluded: archives, drafts, Plans, code conformance, test execution, runtime
  evidence, and non-M/E repair work.
- Authority order: active Principles override lower authority; the Applicable
  Methodology governs Atom, subject, and typed-relation structure; FPF is an
  analysis lens rather than project authority.
- Verdict vocabulary: `boundedly supported`, `unsupported`, and
  `insufficient basis` only. This report does not claim that PROGRAMMATIC has
  passed implementation or runtime validation.
- Confidence rule: findings below 95% are returned to the Operator rather than
  silently decided.

### Review-campaign envelope

| Field | Value |
|---|---|
| Campaign ID | `PROGRAMMATIC-ME-20260901-v1` |
| Phase | Full post-application alignment audit |
| Semantic frontier | 413 active M/E Claim carriers |
| Carrier frontier | Selected subtree plus active Project Principles and relation definitions |
| Frontier SHA-256 | `c4fea4f8c261900b2749df4a7f9279d3431a3ebdf6963d68ab48142791cf4233` |
| Evaluation profile | Coherence, conflict, DRY, gaps, applicability, falsifiability, one-case discipline, subjects, direct typed relations, authority separation, recursive Principle alignment |
| Predecessor | `20260901T183417Z-fpf-structure-recover-recover-programmatic-me-structure.md` |
| Decision owner | Operator |
| Allowed next action | Operator disposition followed by an explicitly authorized repair campaign |

The campaign must not be repeated against the same frontier and profile unless
the Operator requests reconsideration. A changed carrier frontier requires a
new audit edition.

## High-confidence results (>=95%)

### Bounded verdict

The current PROGRAMMATIC M/E set is **not supportable as a fully coherent and
complete authority set**. The shared Python and software-engineering policy
core is now substantially coherent, but 32 active Methods and their 32 direct
Evaluations are generic placeholders, two direct relations violate their
registered target-role contracts, one new Method has no Evaluation, current
control-root authority is contradicted by active Method/Evaluation text, and
two narrower DRY defects remain.

The verdict is bounded to the active M/E authority. It says nothing about
whether the corresponding code currently works.

### Per-claim alignment matrix

The ranges below mean every existing ID in the stated range; absent numeric
IDs are not implied. Each listed Claim was evaluated individually through its
carrier, governed subject, direct relations, applicable upstream authority,
and its cohort's exact content pattern.

| Claim set | Count | Verdict | Basis |
|---|---:|---|---|
| CA-M-087, 101–104, 110, 128–129, 142–148, 150–152, 155–161, 163–182, 191–193, 220–223, 226–231, 233–234 | 60 | boundedly supported | A reusable action or policy, applicability boundary, intended outcome, and stop/non-use condition are recoverable; no contradiction was found in the audited authority surface. |
| CA-M-183–190, 196–219 | 32 | unsupported | Each carrier substitutes the same generic “resolve the current contract” boilerplate for the distinct procedure named by its H1 and Requirement. |
| CA-M-149 | 1 | unsupported | It writes current Scope Unit Graph Projections to legacy `.caprmedio` and still admits obsolete `project_graph_state` contributions. |
| CA-M-153–154 | 2 | insufficient basis | Their `.caprmedio/mrt_atoms.html` location is inside the configured legacy-migration root, but the current authority inspected here does not establish whether that non-authoritative output is an intentional exception. |
| CA-M-162 | 1 | unsupported as a DRY authority boundary | Its source-size ratchet is useful, but it restates the function/effect/object and naming rules already owned by CA-M-157, CA-M-158, and CA-M-160. |
| CA-M-232 | 1 | unsupported | It names `.caprmedio/caprmedio_project_settings.toml`; the current settings carrier and configured control root are `.caprmedio_caprmedio`. |
| CA-M-238 | 1 | unsupported | It owns `method_for: CA-E-403`, although `method_for` must target a Requirement, and it has no incoming active Evaluation. |
| CA-E-065–066, 069–163, 166, 168–205, 211–226, 231–237, 247–300, 309–311, 338–352, 354–378, 380–399, 401 | 275 | boundedly supported | Each has exactly one Test-case section and a recoverable observable pass/fail or rejection boundary; no duplicate H1 or invalid direct target was found in this set. |
| CA-E-301–308, 314–337 | 32 | unsupported | Each uses the same abstract valid/invalid fixture and does not name the input, operation, observable result, or specific falsifying condition of its target Method. |
| CA-E-164–165, 167 | 3 | unsupported | They preserve the obsolete `project_graph_state` contribution name; their governed Method also writes the outputs to the legacy control root. |
| CA-E-067–068 | 2 | insufficient basis | They require `.caprmedio/mrt_atoms.html`; whether that is an intended non-authoritative legacy-root exception is not established at >=95% confidence. |
| CA-E-227 and CA-E-400 | 2 | unsupported as independent canonical owners | Both actively own the same “Reconcile one missed external project change” check for CA-M-087. |
| CA-E-353 | 1 | unsupported relation structure | It uses `evaluation_for: CA-D-250`; the active relation definition permits only Requirement or Method targets. |

### Semantic blockers

#### PME-001 — Generic Method placeholders

Fingerprint:
`generic-method-placeholder|CA-M-183-190,CA-M-196-219|frontier-c4fea4f8`

CA-M-183–190 and CA-M-196–219 repeat the same procedure:

1. resolve a contract;
2. apply “the one shared procedure expressed by this Method”;
3. preserve generic outcomes.

The carrier never states the distinct reusable way named by its title. For
example, Search, Read, Create, Update, Move, Archive, Promote, and Upgrade have
the same body except for Requirement ID and H1. This fails the Method boundary:
the way of doing, exact inputs, operation, and result cannot be recovered from
the Method itself. It also conflicts with DRY and necessary-complexity
Principles because 32 active authority carriers reproduce one non-operative
template. **Confidence: 99%.**

#### PME-002 — Generic Evaluations cannot falsify their targets

Fingerprint:
`generic-evaluation-placeholder|CA-E-301-308,CA-E-314-337|frontier-c4fea4f8`

These 32 Evaluations all say to execute a Method with one valid and one
“contract-relevant invalid or stale precondition.” They do not identify the
input, operation, expected output, exact invalid condition, or observable
failure unique to the Method. The prose can accompany any Method unchanged;
therefore it cannot independently falsify the named Method. All 32 Methods in
PME-001 have only these generic incoming Evaluations. **Confidence: 99%.**

#### PME-003 — CA-M-238 is connected through the wrong relation and has no check

Fingerprint: `invalid-method-for-and-no-evaluation|CA-M-238|CA-E-403`

CA-M-238 owns `method_for: CA-E-403`. CA-R-1017 defines `method_for` as Method
to Requirement. CA-E-403 is an Evaluation, not a Requirement. No active
Evaluation owns `evaluation_for: CA-M-238`. The Method is therefore both
misconnected and uncovered at the Method level. A Dependency subject may name
the Evaluation it consumes, but that does not replace a valid `method_for`
Requirement edge or a check of the Method. **Confidence: 100%.**

#### PME-004 — CA-E-353 evaluates a Delivery through an inadmissible edge

Fingerprint: `invalid-evaluation-for-delivery|CA-E-353|CA-D-250`

CA-E-353 owns `evaluation_for` edges to CA-M-103, CA-M-221, and CA-D-250.
CA-R-1018 permits an Evaluation to target a Requirement or Method only. The
Delivery concern may remain in the test's evidence boundary, but the direct
typed edge cannot target CA-D-250 under current authority. **Confidence: 100%.**

#### PME-005 — Active Methods point current outputs at the legacy control root

Fingerprint:
`stale-control-root-and-graph-state-name|CA-M-149,CA-M-232,CA-E-164,CA-E-165,CA-E-167`

The current Project Settings carrier declares:

- `paths.control_root = ".caprmedio_caprmedio"`;
- `legacy_migration_roots = [".caprmedio"]`;
- current Scope Unit Graph carriers under `.caprmedio_caprmedio`.

CA-M-149 instead writes both current Scope Unit Graph Projections beneath
`.caprmedio`, and CA-M-232 reads project settings from `.caprmedio`. CA-M-149
and CA-E-164, CA-E-165, and CA-E-167 also continue to admit the superseded
`project_graph_state` contribution name after the accepted rename to
`project_scope_unit_graph`. The Method/Evaluation authority therefore points
at stale carriers and vocabulary. **Confidence: 99%.**

#### PME-006 — CA-M-162 duplicates policy owned by neighboring Methods

Fingerprint: `duplicate-function-object-effect-authority|CA-M-157,CA-M-158,CA-M-160,CA-M-162`

The accepted division itself is coherent:

- CA-M-157 owns deterministic functions;
- CA-M-158 owns objects with identity/state/invariant/resource/lifecycle or an
  adapter;
- CA-M-160 owns the decision/effect boundary and permits bounded one-shot
  effect functions;
- CA-M-162 owns the changed-source size and complexity ratchet.

But CA-M-162 restates the effect-function/object allocation and naming rules
as its own normative steps and stop conditions. It should apply the owners by
reference while retaining only the source-size, complexity, and adoption
ratchet. The present wording creates more than one canonical owner for the
same governed meaning under the Project DRY Principle. **Confidence: 97%.**

#### PME-007 — Duplicate missed-change Evaluation authority

Fingerprint: `duplicate-evaluation-owner|CA-E-227|CA-E-400|CA-M-087`

CA-E-227 and CA-E-400 have the same H1, target CA-M-087, and test recovery of
one external change missed by Hook delivery through low-frequency repository
reconciliation. CA-E-227 is the more discriminating case because it also
covers ambiguous dirty ownership and committed-state exclusion. Keeping both
active without an explicit specialization relation creates duplicate check
authority. **Confidence: 99%.**

### Structural and mechanical results

- Active frontier: 98 Methods, 315 Evaluations, 413 total.
- No active M/E drafts remain.
- No duplicate active short IDs exist in the selected subtree.
- Every carrier has at least one GOVERNS subject; no carrier has more than one
  GOVERNS value for the same temporal form.
- All 315 Evaluations contain exactly one `## Test case` section.
- 97 of 98 Methods have at least one incoming active Evaluation relation.
  CA-M-238 is the only uncovered Method.
- 32 Methods have only a generic Evaluation; relation presence therefore does
  not equal effective falsifiability.
- Apart from CA-M-238 and CA-E-353, relation targets resolve and satisfy the
  registered Method/Evaluation target-role boundaries when both project source
  and compiled Applicable Methodology are searched.
- Carrier metadata is heterogeneous: 76/98 Methods and 146/315 Evaluations
  declare `cce_version`; 27/98 Methods and 68/315 Evaluations declare
  `atom_id`. No inspected active rule proves that the remaining carriers must
  already be migrated, so this is not classified as a defect.

### Coherent areas and closed earlier findings

- CA-M-157, CA-M-158, and CA-M-160 now form a coherent function/object/effect
  policy: pure functions are the deterministic default, bounded one-shot
  effects may be functions, and objects require persistent identity or owned
  responsibility. The earlier object-only contradiction is gone.
- CA-M-110, CA-M-164, CA-M-221, and CA-M-229 correctly separate Method-owned
  technology selection from configuration/Implementation materialization,
  Delivery carriers, and Ops execution evidence.
- CA-M-163 correctly references the still-active BSEED logging authority and
  does not redefine the shared level vocabulary.
- CA-M-191–193 now contain concrete procedures, and CA-E-309–311 contain
  concrete falsifying cases. The earlier placeholder issue in that set is
  closed.
- The archived CA-M-194/CA-E-312 pair is absent from active authority.
- CA-M-221 has direct concrete coverage through CA-E-376–378; the missing-uv-
  Evaluation finding is closed.
- CA-M-162 has concrete split coverage for file size, executable-unit size,
  complexity, effects, names, and externalized mappings through CA-E-266,
  CA-E-363–368, and CA-E-354. Its remaining problem is duplicated Method
  authority, not missing Evaluation cases.

### Residual gaps and optional improvements

1. Repair blockers in dependency order: valid relation owners and targets;
   current carrier names; real Methods; concrete Evaluations; then DRY cleanup.
2. Do not normalize headings or add frontmatter merely for visual uniformity.
   The current content rules require recoverable meaning, not one publication
   template, and the necessary-complexity Principle applies.
3. If CCE migration of all active PROGRAMMATIC M/E carriers becomes an
   accepted project outcome, define its completion boundary first. The current
   mixed carrier form alone is insufficient basis for a migration mandate.

### Excluded or uninspected claims

- Whether Implementation actually realizes any Method.
- Whether any Evaluation is executable or currently passing.
- Runtime performance, logging, recovery, compatibility, or installation
  evidence.
- Requirement completeness outside the M/E relations needed for this audit.
- Archived alternatives and historical supersession correctness.
- Whether physical Tool/App carrier groups should become declared Scope Units.

### Stop and return condition

Stop the audit here. The material blockers, clean areas, unresolved boundary,
and exact repair order are recoverable. Return to the Operator before treating
the GRAPH_APP legacy-root location as a defect. After Operator disposition,
repair each finding through its narrowest owner and rerun the audit only on a
changed frontier.

## Open questions (confidence <95%)

1. Should `.caprmedio/mrt_atoms.html` remain an intentional non-authoritative
   delivery exception inside the configured legacy-migration root, or should
   CA-M-153, CA-M-154, CA-E-067, and CA-E-068 move that output to the current
   `.caprmedio_caprmedio` control root? Current inspected authority supports
   both readings only weakly, so no repair is inferred. **Confidence in either
   answer: below 95%.**

## Skills used

- `$fpf alignment audit` — audited the recovered M/E frontier and returned
  bounded findings without changing project authority.

#### FPF sources consulted (6 read; 6 used)

- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/10_11_First-Practical Entry and Pattern-Use Discoverability Discipline/01_E.11.PUA - Pattern Use in a Working Situation and First Useful Result.md` — **used**: kept the audit result-oriented and separated a useful finding from a plan, repair, or proof of runtime success.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/15_A.06.M - Module Relation Repair.md` — **used**: kept physical carrier groups, declared Scope Units, interfaces, and replaceability claims distinct.
- `FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/00_01_Holon Aggregation and Part-Whole Construction/01_B.01.01 - Dependency Structure and Relation Grounding.md` — **used**: checked relation meaning before graph shape and exposed the two invalid target-role edges.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/22_34_Structural Correspondence, Equivalence, and Morphism Adequacy/00_C.34 - Structural Correspondence, Equivalence, and Morphism Adequacy.md` — **used**: compared Method/Evaluation carriers and generated-path claims without treating similar shape as semantic equivalence.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/03_Transformer Constitution (Quartet)/01_A.03.01 - U.Method- Reusable Way of Doing with Explicit Applicability.md` — **used**: evaluated whether each Method made its reusable way, applicability, outcome, and stop boundary recoverable.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/19_CharacteristicSpace & Dynamics Hook (A.CHR-SPACE)/01_A.19.ECS - Evaluation CharacteristicSpace Construction.md` — **used**: checked Evaluation object/use fit, discriminating cases, evidence basis, falsifiability, and stop boundaries.
