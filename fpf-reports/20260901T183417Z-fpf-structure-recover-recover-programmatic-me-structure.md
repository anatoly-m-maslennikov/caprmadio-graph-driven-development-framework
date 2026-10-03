## Task, scope, and boundaries

Recover the current active Method and Evaluation structure under
`.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC`
for a subsequent coherence and gap audit.

Saved report: `fpf-reports/20260901T183417Z-fpf-structure-recover-recover-programmatic-me-structure.md`

The observed edition is the working tree on 2026-09-01. The selected structure
contains active Markdown Method and Evaluation carriers, their direct typed
relations, their governed subjects, and their placement under the declared
PROGRAMMATIC, TOOLS, APPS, and MCP Scope Units. Archives, drafts, other Content
roles, and implementation code are excluded except where they resolve a direct
relation or structural boundary.

The receiving use is the next `$fpf alignment audit`. This record is descriptive:
it does not decide whether the recovered policies are good. The operator remains
the project authority, and active Principles remain overriding project authority.

Evidence used:

- all 413 active M/E carriers in the selected subtree;
- `project_scope_unit_graph.projection.toml`, explicitly treated as a
  non-authoritative projection;
- active relation definitions for `method_for`, `evaluation_for`, and
  `derived_from` in the Applicable Methodology;
- live relation targets in `.caprmedio_caprmedio` and
  `.caprmedio_framework/00_APPLICABLE_METHODOLOGY`;
- the active project Principle carrier set.

Stop condition: the selected organization, carrier-versus-Scope-Unit boundary,
direct relations, coverage structure, preserved information, and missing
information are explicit enough for the audit without proposing repairs.

## High-confidence results (>=95%)

### Subject, boundary, state or edition, receiving use, and resolved FPF source

The selected organization is the active PROGRAMMATIC M/E authority subtree,
not the folder tree by itself and not the generated Scope Unit projection.
**Confidence: 99%.** This follows from direct carrier enumeration and the
projection's own `non_authoritative = true` declaration.

The declared structural chain is:

```text
FRAMEWORK_ENGINE (Layer, level 1)
└── PROGRAMMATIC (Feature, level 2)
    ├── TOOLS (Feature, level 3)
    ├── APPS (Feature, level 3)
    └── MCP (Feature, level 3)
```

The directories beneath TOOLS and APPS, such as `ATOM_READ`,
`COMMIT_CHANGE_SET`, `GRAPH_APP`, and `CODEX_PLUGIN`, are physical carrier
groups. They are not declared Scope Units in the current project Scope Unit
graph. **Confidence: 99%.** The projection declares `child_composition =
"NONE"` for TOOLS, APPS, and MCP and registers no lower Scope Units.

The FPF structure source supplies the rule used here: recover independently
identified constituents, direct obtaining relations, applied constraints, and
one named use; do not mistake the carrier or view for the selected structure.
The structural-information source supplies the missing-information boundary:
this report states what the carriers and projection preserve and what the next
audit must return to live sources to decide.

### Recovered entities, values, relations, and structure kinds

The active set contains **98 Methods and 315 Evaluations: 413 Atoms total**.
Versions range from 1 through 18. Every active carrier has a governed subject.
The carrier-frontier SHA-256 is
`c4fea4f8c261900b2749df4a7f9279d3431a3ebdf6963d68ab48142791cf4233`.

| Declared Scope Unit or physical carrier group | Methods | Evaluations |
|---|---:|---:|
| PROGRAMMATIC | 22 | 62 |
| TOOLS, direct | 34 | 156 |
| TOOLS child carrier groups, combined | 17 | 67 |
| APPS, direct | 2 | 5 |
| APPS child carrier groups, combined | 8 | 8 |
| MCP | 15 | 17 |
| **Total** | **98** | **315** |

TOOLS child carrier groups with M/E carriers are APPEND_CHANGE_RECORDS,
ATOM_ARCHIVE, ATOM_CREATE, ATOM_MOVE, ATOM_PROMOTE, ATOM_READ, ATOM_SEARCH,
ATOM_UPDATE, ATOM_UPGRADE, CLOSE_ATOM, COMMIT_CHANGE_SET, COMMIT_CONTEXT,
COMMIT_TRIGGER, COMPILE_APPLICABLE_METHODOLOGY, INSTALL_TOOLS,
MIGRATE_ATOM_IDENTITY, REBIND_ATOM_RELATIONS, REPLACE_ATOM,
RETRIEVE_APPLICABLE_METHODOLOGY, START_BACKGROUND_SERVICES, and
DETECT_CLAIM_VALUE_SET_CANDIDATES. APPS child
carrier groups are AGENT_HOST_PLUGINS, AGENT_HOST_PLUGINS/CODEX_PLUGIN, and
GRAPH_APP.

The direct relation vocabulary used by the selected carriers is exactly:

- `method_for`: 131 edges owned by all 98 Methods; 130 are directed to
  Requirements and CA-M-238 is incorrectly directed to Evaluation CA-E-403;
- `evaluation_for`: 418 edges owned by all 315 Evaluations and directed to
  Requirements or Methods;
- `derived_from`: 176 edges owned by 176 carriers and directed to Analyses.

The active relation definitions permit Evaluations to target either a
Requirement or a Method. Therefore mixed `evaluation_for` target roles are part
of the recovered structure, not an inferred defect.

The subject representation has two observed layers:

- every carrier declares `subjects.governs`;
- 27 Methods and 66 Evaluations also declare `subjects.depends_on`.

The remaining 320 carriers do not declare `subjects.depends_on`. This is an
observed absence only; its quality significance belongs to the audit.

### Current-state structure map or relation register

Ninety-seven active Methods have at least one incoming active
`evaluation_for` edge. CA-M-238 has none.
There are no duplicate active short identities inside the selected subtree.
All direct relation targets resolve when the project source and compiled
Applicable Methodology are treated as the two declared authority carriers.
**Confidence: 99%.** This was checked against the live filenames and
frontmatter, not inferred from the generated projection.

Coverage is uneven and incomplete at the Method identity level:

| Area | Methods | Covered Methods | Evaluations per Method, observed range |
|---|---:|---:|---:|
| PROGRAMMATIC | 22 | 22 | 1–8 |
| TOOLS direct | 34 | 34 | 1–31 |
| TOOLS child carrier groups | 17 | 16 | 0–8 |
| APPS direct and child groups | 10 | 10 | 1–3 |
| MCP | 15 | 15 | 1–2 |

The shared PROGRAMMATIC identity and version register is:

- Methods: CA-M-110@9, CA-M-157@5, CA-M-158@5, CA-M-159@3,
  CA-M-160@5, CA-M-161@3, CA-M-162@5, CA-M-163@3, CA-M-164@3,
  CA-M-165@3, CA-M-166@3, CA-M-191@4, CA-M-192@4, CA-M-193@4,
  CA-M-221@4, CA-M-228@1, CA-M-229@2, CA-M-230@1, CA-M-231@1,
  CA-M-232@1, CA-M-233@1, CA-M-234@1.
- Evaluations: CA-E-253@4–CA-E-272@4; CA-E-309@3–CA-E-311@3;
  CA-E-356@2–CA-E-367@2; CA-E-368@3; CA-E-369@2–CA-E-378@2;
  CA-E-382@1–CA-E-397@1.

The MCP register is:

- Methods: CA-M-167@2–CA-M-173@2, CA-M-174@3, CA-M-175@2–CA-M-177@2,
  CA-M-178@3–CA-M-180@3, CA-M-181@2.
- Evaluations: CA-E-273@3–CA-E-284@3, CA-E-285@4,
  CA-E-286@3–CA-E-287@3, CA-E-398@1–CA-E-399@1.

The APPS register is:

- direct: CA-M-196@2, CA-M-222@4; CA-E-314@2,
  CA-E-349@3–CA-E-352@3;
- AGENT_HOST_PLUGINS: CA-M-197@2; CA-E-315@2;
- CODEX_PLUGIN: CA-M-150@8–CA-M-152@7, CA-M-198@2–CA-M-199@2;
  CA-E-288@3–CA-E-290@3, CA-E-316@2–CA-E-317@2;
- GRAPH_APP: CA-M-153@10–CA-M-154@9; CA-E-067@9–CA-E-068@9.

The TOOLS Method register is:

- direct: CA-M-087@18, CA-M-101@6, CA-M-102@5, CA-M-142@9,
  CA-M-143@9, CA-M-144@9, CA-M-145@10, CA-M-146@9, CA-M-147@7,
  CA-M-148@7, CA-M-149@9, CA-M-182@3, CA-M-200@2–CA-M-220@2,
  and CA-M-223@4;
- child carrier groups: CA-M-103@10, CA-M-104@5, CA-M-128@5,
  CA-M-129@5, CA-M-155@4, CA-M-156@4, CA-M-183@2–CA-M-190@2,
  CA-M-226@1, CA-M-227@2, and CA-M-238@1.

The TOOLS Evaluation register is the union of:

- direct CA-E-065–CA-E-066, CA-E-069–CA-E-168, CA-E-178, CA-E-180,
  CA-E-182, CA-E-184–CA-E-185, CA-E-188, CA-E-191–CA-E-193,
  CA-E-195, CA-E-198, CA-E-201, CA-E-217, CA-E-291–CA-E-295,
  CA-E-300, CA-E-318–CA-E-346, CA-E-348, CA-E-353–CA-E-355,
  and CA-E-400–CA-E-401;
- APPEND_CHANGE_RECORDS CA-E-181, CA-E-183, CA-E-187, CA-E-197,
  CA-E-200, CA-E-205;
- COMMIT_CHANGE_SET CA-E-179, CA-E-196, CA-E-199, CA-E-202–CA-E-204,
  CA-E-211–CA-E-213, CA-E-216, CA-E-236–CA-E-237, CA-E-347;
- COMMIT_CONTEXT CA-E-170–CA-E-177, CA-E-189–CA-E-190, CA-E-214,
  CA-E-218, CA-E-232–CA-E-233;
- COMMIT_TRIGGER CA-E-169, CA-E-186, CA-E-194, CA-E-215, CA-E-227,
  CA-E-234–CA-E-235;
- INSTALL_TOOLS CA-E-219–CA-E-221, CA-E-225–CA-E-226, CA-E-231;
- START_BACKGROUND_SERVICES CA-E-222–CA-E-224;
- the one-to-one or two-case groups CA-E-247–CA-E-252,
  CA-E-296–CA-E-299, and CA-E-301–CA-E-308;
- COMPILE_APPLICABLE_METHODOLOGY CA-E-380 and
  RETRIEVE_APPLICABLE_METHODOLOGY CA-E-381.

This identity register selects every active M/E constituent while leaving each
carrier as the canonical location for its full subject and edge values. Copying
all 413 frontmatters into this report would create another representation, not
another authority source.

### Evidence, inference labels, disputes, and missing information

Direct observations:

- 413 current carriers satisfy the active-folder selection.
- No active M/E draft carrier remains in the selected subtree.
- CA-M-238 lacks an incoming active Evaluation relation and uses
  `method_for: CA-E-403`, which does not satisfy the active `method_for`
  target-role definition.
- Seven relation targets appear unresolved if only `.caprmedio_caprmedio` is
  searched; all seven resolve when the compiled Applicable Methodology is
  included. The earlier source-only warning is therefore a carrier-boundary
  effect, not a broken relation.
- 76 Methods and 146 Evaluations declare `cce_version`; 27 Methods and 68
  Evaluations additionally declare `atom_id`. The remainder rely on filename
  identity and the earlier accepted frontmatter shape.
- 79 Methods and 97 Evaluations declare `derived_from`; 18 Methods and 218
  Evaluations do not.

Supported structural inference:

- Shared PROGRAMMATIC Methods are reused by some child-feature Evaluations.
  This is supported by five TOOLS-to-PROGRAMMATIC and one APPS-to-PROGRAMMATIC
  `evaluation_for` edge, rather than inferred from folder ancestry.
- The large TOOLS Evaluation population is partly a Requirement-checking
  register, not merely Method coverage. Many Evaluations target both a Tool
  Method and one or more Requirements.

Preserved structure:

- active identity and version;
- declared Scope Unit and physical carrier group;
- governed and dependency subjects;
- direct `method_for`, `evaluation_for`, and `derived_from` edges;
- distinction between project-source and compiled-methodology targets;
- Method-level Evaluation coverage.

Lost or intentionally excluded structure:

- the complete prose claims and procedures inside all 413 carriers;
- code realization and runtime evidence;
- whether each Evaluation is strong enough to falsify its target;
- whether absent `derived_from`, `depends_on`, or `cce_version` fields are
  valid exceptions or migration gaps;
- whether high Evaluation counts are necessary coverage or duplication;
- whether physical child carrier groups should ever become Scope Units.

Those excluded questions are the explicit return conditions for the alignment
audit. No current-state dispute blocks the handoff.

### Recovery stop and legal downstream handoff

Recovery stops here because the selected constituents, declared structural
units, direct relation classes, coverage structure, carrier boundaries, and
missing information are explicit. Continuing to rank, merge, remove, or rewrite
Atoms would cross from recovery into evaluation or redesign.

Legal handoff: `$fpf alignment audit` may use this record as the frozen
structural frontier, but it must return to the live carriers for prose-level
coherence, applicability, falsifiability, duplication, and gap claims. If the
carrier set changes, this structure record must be regenerated before relying
on its counts or identity register.

## Open questions (confidence <95%)

None identified within the declared recovery scope. Questions about the quality
or intended future structure of the recovered system were deliberately returned
to the next audit rather than answered here.

## Skills used

- `$fpf structure recover` — recovered the current active PROGRAMMATIC M/E
  organization and its evidence boundary without evaluating or redesigning it.

#### FPF sources consulted (2 read; 2 used)

- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/00_A.22 - Structure and Structural Views (STRUCT-CAL).md` — **used**: defined the selected-structure recovery order and prevented the folder or projection from being treated as the structure itself.
- `FPF-Knowledge-Graph/C_Kernel Extension Specifications/21_33_Structural Information Adequacy for Architecture Capture and Missing-Structure Return/00_C.33 - Structural Information Adequacy for Architecture Capture and Missing-Structure Return.md` — **used**: defined the captured-versus-missing structural information and the return condition for the subsequent audit.
