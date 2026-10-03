## Task, scope, and boundaries

Recover the current CAPRMEDIO normalization system for the next bounded exploration of additional normalizations. The receiving use is an authority map: it separates what source Atoms currently govern from derived carriers, identifies enforcement boundaries, and records missing structure without proposing a change.

Saved report: `fpf-reports/20260831T212448Z-fpf-structure-recover-recover-the-current-caprmedio-normalization-system-from-active-core-meta.md`

Subject: the active normalization authorities in `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/`, specifically `001_CORE_META_MODEL` and `003_LOCAL_CONFIGURATION`. State: the current source frontier on 2026-08-31 UTC. Excluded: archived and draft carriers, non-selected Installed Extensions, projection content as authority, Atom/code/plan edits, and candidate design.

Authority is the source-Atom frontier. The Applicable Methodology compiler dry run reported 633 eligible and selected source revisions: 564 Core Meta-Model plus 69 Local Configuration carriers; it reported zero diagnostics and conflicts, selected only those two contributing layers, and treated its output as `non_authoritative_dry_run`. The structural source topology also contains `002_INSTALLED_EXTENSIONS`, which the compiler requires to be empty and non-contributing in this state. Its digest was `1ee601433860e703764072cce9daecec29aff9bc6c1ae88659a37320d35fdf9e`.

A current source carrier is a regular Markdown file in a participating role directory outside `archive/` and `drafts/`. This is carrier-state evidence, not an inferred semantic status: CA-D-295 materializes Active by direct placement and a non-Active value by its status subdirectory; CA-D-336 requires active discovery to exclude non-Active status directories and fail on zero or multiple matches. The compiler independently excludes `archive` and `drafts` below source role directories.

Sources and evidence: the live source Atom carriers, the read-only compiler dry run, and the selected FPF sources listed below. The worktree already contained an unrelated modified Work Journal and a prior untracked FPF report; neither was read as evidence or changed.

Stop condition: this is a current-state map, not a proposal, quality verdict, or authorization. It stops after naming the existing structure, lost detail, and legal handoff.

## High-confidence results (>=95%)

### 1. Recovered entities, values, relations, and structure kinds — 99%

The normalization system consists of nine cooperating structures.

| Structure kind | Exact current constituents and obtaining relations | Main enforcement boundary |
| --- | --- | --- |
| Source authority frontier | Current Core Meta-Model and Local Configuration Atom revisions; selected revision → compiled projected Atom | compiler discovery and CA-R-1213, CA-R-1228, CA-M-224, CA-E-379 |
| Atom boundary | Atom → one independently replaceable Claim → one atomic or composite Claim Scope | CA-R-918, CA-R-919, CA-R-643, CA-R-771, CA-R-1270, CA-R-1271; CA-M-111, CA-M-115; CA-E-384 |
| CCE surface | Claim → CCE version and canonical operators; governed terms and scope-unit names remain distinct from operator tokens | CA-R-940, CA-R-941, CA-R-1297; CA-M-113, CA-M-229, CA-M-230, CA-M-234, CA-M-236; CA-D-279, CA-D-280; CA-E-241 |
| Term and Subject graph | Term occurrences plus SUBTYPE_OF, IS_BORNE_BY, and IS_ALLOWED_VALUE_OF → Subject Expression; Atom → GOVERNS or DEPENDS_ON Claim-Subject relation | CA-R-1242 through CA-R-1247, CA-R-1275 through CA-R-1285, CA-R-1318 through CA-R-1353; CA-M-114, CA-M-125, CA-M-127, CA-M-228, CA-M-232; CA-E-246, CA-E-382, CA-E-383 |
| Direct semantic relation graph | owning Atom → direct registered relation → canonical target reference; inverse is derived, not authored | CA-R-117, CA-R-118, CA-R-121, CA-R-1016 through CA-R-1027, CA-R-1040; CA-M-120; CA-D-268 |
| Type-qualified status | complete Entity-Type path → Status domain → one current Status; earlier transitions → Journal | CA-R-1284, CA-R-1285, CA-R-1306 through CA-R-1313; CA-E-386; CA-D-295 |
| Derived navigation | complete Claim and Claim Scope → Summary and Translations; current Claim-Subject relations → Subject Projection | CA-R-1272 through CA-R-1274, CA-R-1281; CA-M-111, CA-M-114, CA-M-116, CA-M-231, CA-M-232; CA-D-281, CA-D-282 |
| Carrier and address | Artifact revision → File or Directory Carrier → canonical address, filename, frontmatter, or status directory | CA-D-254 through CA-D-303, CA-D-308, CA-D-312, CA-D-314, CA-D-316, CA-D-336 |
| Project-local selection | Local Configuration → current Project, selected source layers, optional extension set, and concrete placement | CA-R-1223 through CA-R-1227; CA-D-317 through CA-D-327 |

The table is a selected organization for this receiving use. It does not add a new CAPRMEDIO graph or relation kind.

### 2. Current-state normalization authority map — 99%

| Family | Normalized fact | Source authority | Enforcement recovered |
| --- | --- | --- | --- |
| One Claim and one Scope | one Atom has one independently replaceable Claim and one Claim Scope; a relational Atom is where Claim Scope differs from Current Scope | CA-R-918 to CA-R-923 | authoring methods CA-M-111 and CA-M-115; scope test CA-E-240; composite test CA-E-384 |
| Split versus retain | independently replaceable content splits; components accepted, replaced, and retired together remain one composite Claim | CA-R-771 and CA-R-1270 | CA-M-115 and CA-E-384 |
| Value-set consolidation | Claims with equal Current Scope, Claim Scope, and X consolidate to one `X: (A, B, C)` Claim only when the allowed value of X is the sole difference | CA-R-1358 | normative authoring authority; generic duplicate-removal step in CA-M-115 |
| Controlled language | Claims are human-readable and have one precise interpretation; canonical CCE operators have controlled spelling, function, rewrite rules, and rendering | CA-R-940, CA-R-941; CA-M-229, CA-M-230, CA-M-234, CA-M-236; CA-D-280 | CA-E-241 specifies CCE and derived-projection validation |
| Term naming and expression syntax | a Term is one reusable atomic Subject; capitalized governed terms, lowercase general terms, and reserved `/` and `:` delimiters keep expression syntax distinct from names | CA-R-1318 to CA-R-1324; CA-M-228 | CA-E-382 and CA-E-383 |
| Term-tree cardinality | a Term has at most one direct SUBTYPE_OF parent and at most one direct IS_ALLOWED_VALUE_OF parent; a dependent occurrence has one immediate bearer | CA-R-1244, CA-R-1247, CA-R-1260, CA-R-1346, CA-R-1347, CA-R-1351 | CA-E-382 and CA-E-383 |
| Claim-Subject relations | active or draft Atom has at least one GOVERNS relation; kind and temporal form are single-valued; same-temporal-form independent governance splits | CA-R-1201 to CA-R-1204 and CA-R-1275 to CA-R-1281 | CA-M-125 and CA-E-246; Subject Projection reproduces, never owns, the relations |
| Direct semantic relations | one semantic relation has one authoritative declaration on its owning Atom, represents an immediate registered fact, and does not author inverses | CA-R-117, CA-R-118, CA-R-121, CA-R-1023 to CA-R-1027, CA-R-1040 | CA-M-120 derives the relation registry; CA-D-268 requires unique canonical target references |
| Type and Status | every Entity occurrence has at most one direct Type; every governed Artifact has one current Status from its complete Entity-Type path | CA-R-1284, CA-R-1285, CA-R-1306 to CA-R-1313 | CA-E-386 and CA-D-295 |
| Summary and navigation | Summary is a concise non-authoritative navigation Projection, source-faithful to the complete Claim and Claim Scope; it cannot reconstruct or validate authority | CA-R-1272 to CA-R-1274 | CA-M-111; CA-D-281 and CA-D-282; CA-E-384 |
| Carrier serialization | canonical address encodes an Artifact property once, while frontmatter omits duplicate address facts; names, cases, lifecycle suffixes, and directories are deterministic carrier facts | CA-D-267 through CA-D-302 | carrier validators are specified by the individual Delivery authorities; active discovery is CA-D-336 |
| Compilation | only exact selected current active RMEDO source revisions contribute; compilation preserves Claim and source identity, reports conflicts, and never synthesizes or merges Claims | CA-R-1213, CA-R-1228, CA-R-1316; CA-M-224; CA-E-379 | implemented compiler dry run; source-frontier digest, conflict report, and approval gate |
| Current local configuration | `caprmedio` is the current Project; only Core Meta-Model and Local Configuration are selected, no Installed Extensions, local Tool, MCP, or App mode | CA-R-1223 to CA-R-1227 | Local Configuration source atoms plus compiler topology and selection logic |

### 3. Recovered overlap and boundary register — 98%

1. Claim-boundary authorities form one decision sequence, not conflicting rules: CA-R-771 splits independently replaceable content; CA-R-1270 retains logically composite content that changes together; CA-R-1358 consolidates the narrower case where equal-scope Claims differ only by one allowed value. CA-M-115 then removes duplicate alternate authoritative statements. The shared boundary is independent accept/replace/retire behavior.

2. CA-R-1358 is an authoring normalization, not a compilation operation. CA-R-1316 and CA-M-224 expressly forbid compilation synthesis or Claim merge; the compiler therefore carries a consolidated source Claim forward but must never create one.

3. CCE normalization divides semantic tokens from their Markdown rendering. CA-M-230/CA-M-234/CA-M-236 govern canonical tokens and rewrites; CA-M-229 and CA-D-280 govern lowercase bold serialization. A bold rendering is a carrier fact, not another operator meaning.

4. The Term System and Claim-Subject system are connected but distinct. Subject Expressions reuse Terms and direct Term-System relations; Claim-Subject relations reference independent Subjects and add Kind plus Temporal Form. A derived Subject Projection reproduces the latter without becoming terminology or authority.

5. Status is one current Property, while status directories and Journal entries materialize lifecycle state and history. CA-R-1311 prevents prior transitions from becoming additional current Status values; CA-D-295 turns the resolved current value into carrier placement.

6. Projections are derived and non-authoritative. Summaries, terminology, Subject Projections, and Applicable Methodology each have distinct source relations and must not become source authority. This boundary is especially material to normalization because a projection may expose a duplicate-like pattern but cannot replace or merge its source.

### 4. Directly observed evidence and inference labels — 99%

**Directly observed source facts**

- the compiler selected 633 current source candidates from CORE_META_MODEL and LOCAL_CONFIGURATION, reported zero conflicts and diagnostics, and set `can_apply: true`;
- the compiler code excludes `archive` and `drafts`, rejects non-empty Installed Extensions, derives a source-frontier digest, detects selected-Atom and Definition conflicts, and blocks application while a conflict lacks exact approval;
- CA-R-1358 is the only active source carrier found that defines the `X: (A, B, C)` value-set Claim form;
- CA-R-1245 defines `:` only within a Subject Expression as an IS_ALLOWED_VALUE_OF relation;
- CA-R-1316 and CA-M-224 prohibit compiler Claim synthesis and merging.

**Supported inferences**

- the active source set is established sufficiently for this map because live compiler discovery selected a conflict-free frontier from the stated authoritative source locations;
- CA-R-1358 belongs to authoring normalization rather than projection compilation because compilation is explicitly barred from performing its merge-like result;
- the current normalization system has semantic, carrier, and projection layers with explicit non-authority boundaries.

**Disputes**

None recovered. The compiler reported no unresolved conflict among the selected current source revisions.

### 5. Missing structural information and enforcement boundaries — 97%

1. **Value-set Claim grammar is not fully recovered.** CA-R-1358 establishes the surface form `X: (A, B, C)`, while CA-R-1245 assigns colon semantics only in a Subject Expression. No active source carrier was recovered that defines value-set Claim membership, duplicate-value handling, ordering significance, or the delimiter’s Claim-context semantics. This is a missing-structure record, not a conflict finding: the two authorities have explicitly different stated contexts.

2. **No specific automated cross-Atom consolidation check was recovered.** CA-M-115 contains a general duplicate-removal authoring step and CA-E-384 tests one Atom’s Claim/Scope boundaries, but neither names the CA-R-1358 equivalence pattern. The compiler detects identity, term-definition, replacement, incompatibility, priority, and output-path conflicts; it neither synthesizes nor merges Claims. Therefore the recovered enforcement for value-set consolidation is currently authoring authority, not an observed mechanical check.

3. **Only source-frontier/compilation mechanics were executed in this recovery.** Evaluation Atoms define checks for CCE, composite Claims, Term-System graphs, Subject Expressions, and Status, but this call did not run their project-specific validators. Their presence is source authority; passing runtime verification was not claimed.

### 6. Recovery stop and legal downstream handoff — 99%

The required Current-State Structure Record is complete for its receiving use. It establishes source authority, constituents, obtaining relations, constraints, carrier/projection boundaries, observed gaps, and a stop against candidate design.

The legal downstream handoff is an explicit, separate exploration of normalization candidates using this map. That work may compare candidates only after retaining the documented boundaries: independent replaceability, source authority, no compiler Claim merge, and non-authority of projections.

## Open questions (confidence <95%)

None identified within the declared scope.

## Skills used

- `$fpf structure recover` — recovered the current normalization authority structure from live source carriers without redesigning it.

#### FPF sources consulted (2 read; 2 used)

- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md` — **used**: separated the selected normalization organization from its files, generated views, and selection method.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/21_33_Structural Information Adequacy for Architecture Capture and Missing-Structure Return/00_C.33 - Structural Information Adequacy for Architecture Capture and Missing-Structure Return.md` — **used**: recorded source-carrier limits, missing structure, and safe downstream handoff.

<oai-mem-citation>
<citation_entries>
MEMORY.md:83-86|note=[live checkout and prior Term normalization continuity]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>
