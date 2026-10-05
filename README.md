# CAPRMEDIO

**The Graph-Driven Development Framework**

## The Goal

If it can be built, CAPRMEDIO should help anyone build it if they are willing to invest the time and effort.

In practice, it should make AI-assisted development reliable from the first idea to production without losing meaning, traceability, or learning.

## What CAPRMEDIO is

CAPRMEDIO stores project knowledge as small artifacts connected by typed links. Humans and AI use this graph to understand the project, make changes, check consistency, and generate useful views.

## Why CAPRMEDIO works this way

Prompts/Skills, MCP, Apps and execution Tools form the harness (frontend and toolset) →\
the project's meaning must not depend on them →\
an explicit ontology/base model defines the core: concepts, relations and constraints.

### Ontology (methodology)

The project puts decisions into practice—yours and AI Agents' →\
but sessions are ephemeral →\
we need a **stable source of truth** →\
the specification.

Spec grows →\
we need smaller units →\
no single file structure is optimal for every use case →\
a graph with typed nodes and typed relations.

Each unit should be the smallest meaningful part of the spec →\
one scope + one Claim = one Atom →\
splitting further adds no useful distinction.

Nodes represent different things →\
Atoms state Claims; Entities are the things those Claims describe →\
Subjects link Atoms to Entities through `GOVERNS` and `DEPENDS_ON`.

Different tasks need different views →\
derive them from one authoritative source →\
**load only the context needed without duplicating authority.**

Natural-language phrases can be ambiguous →\
shared vocabulary + CAPRMEDIO Controlled English (CCE), a constrained way to write Claims →\
**explicit, checkable Claims.**

We need more than spec →\
Concerns, Analysis and Plans for understanding and planning →\
Requirements, Methods, Evaluations and Delivery (RMED) for specification →\
Implementation for code, tests and configuration →\
Operations for repeatable actions and workflows.

Implementation, tests and views rely on Claims →\
record the exact source Claim identities and revisions →\
**trace results back to the specification.**

Work changes the project →\
Journal records changes and execution →\
observed outcomes create the next Concerns.

### Harness (engine)

Repeated model reasoning costs time and tokens →\
every repeatable task that can be done deterministically should run programmatically →\
**Tools save time and tokens.**

Work that cannot be done deterministically →\
LLM reasoning →\
repeatable actions need reusable Prompts/Skills.

Repeatable sequences of actions using Tools and Prompts/Skills →\
Workflows define their steps and control flow.

We cannot put everything into one prompt →\
the single entry Skill, [ca](102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md), connects agents to MCP →\
Tools retrieve the needed context and assemble Prompts/Skills →\
MCP delivers them and exposes Tool and Workflow execution.

Wide-context reasoning →\
main session.

Narrow, repeatable work →\
bounded execution contexts and structured results.

Long actions should not block sessions →\
Workflow Orchestrator coordinates the steps in the background →\
durable state, reconnectable runs, approvals and recovery.

Files in folders are clear and inspectable →\
they currently hold authority →\
rescanning can become expensive →\
a derived graph database index supports queries and views. Database authority could be a future migration.

## Main framework architecture

### Node types

- **Scope Unit:** one area of project responsibility, declared in the project structure.
- **Atom:** one Claim in one scope, with a content role. Atoms belong to Scope Units; project-wide goals are the exception.
- **Journal:** records of changes, execution and observed outcomes.
- **Projection:** a derived, non-authoritative view of existing sources.

### Content roles

- **C — Concern:** problems, bugs, questions and opportunities.
- **A — Analysis:** analysis reports and rationale.
- **P — Plan:** backlog, tasks, epics and version plans.
- **R — Requirement:** specification of required outcomes.
- **M — Method:** how code should be written.
- **E — Evaluation:** quality assurance policies and test-case specifications.
- **D — Delivery:** target environments, CI/CD and release policies.
- **I — Implementation:** code, tests, configuration and CI/CD pipelines implementing all RMED.
- **O — Operations:** actions and workflows with steps to operate the project.

Each Atom content role has allowed **Types**. Each Type defines its structure, properties, authoring rules and checks, including when each property is required. For example, O includes Action, Step, Workflow and Actor.

Content roles describe purpose. Atom, Journal and Projection describe form. Both classifications follow **MECE**: categories cover their declared scope without overlap. **DRY** means that each meaning has one authority, not independent copies.

**One coherent source of truth:** Atoms record Claims; actual Implementation shows what is built.

[project_structure.toml](.caprmedio_caprmedio/project_structure.toml) defines Scope Units, their parents and their authority/Delivery paths. Folders follow these declarations; they do not define them.

### Fractal structure

**The same pattern repeats at every level.** Scope Units can contain child Scope Units. P Atoms can break work into smaller P Atoms: epics, sub-epics, tasks and subtasks.

Both structures have **no fixed limit on nesting depth**. Declared relationships define the nesting, not folders alone. Neither structure may contain cycles. Each Claim keeps its own scope; nesting does not give it wider authority.

### Local and global tiers

**Local Tier** describes a Claim's level within its Scope Unit:

- **Principle:** a guiding rule at Project level.
- **Core:** basic definitions and boundaries.
- **General:** reusable rules for Standard content.
- **Standard:** concrete project content and decisions.

At Project level, Principle governs Core, and Core governs Standard. In other Scope Units, Core governs General, and General governs Standard.

**Global Tier** combines scope and Local Tier into one authority number across the hierarchy. Smaller numbers govern larger numbers within the applicable scope. Project goals have Global Tier `-1` and no Local Tier.

**Tiers describe authority, not work priority or folder depth.**

### Ownership and claim scope

- **Internal:** the project sets and owns the artifact's meaning.
- **External:** an identified outside source sets or imposes the meaning. The project records that source and how it applies.
- **Relational:** an Atom's Claim targets a Scope Unit other than the Atom's own, or the Atom has no containing Scope Unit.

Internal/external describe **Governance Origin**; relational describes **claim scope**, not a third origin.

### Relations

- **Direct relations** link specific artifacts: `child_of` links Requirements to their parents; `method_for`, `evaluation_for` and `delivery_for` link RMED Atoms to the Requirements they serve; `derived_from` links results to their sources.
- **Subjects** link an Atom to an Entity. `GOVERNS` names what its Claim governs. `DEPENDS_ON` names what the Claim needs but does not govern. A Subject is a relation, not another node.

Scope Units + typed relations + Subjects →\
**fetch the relevant slice of the specification—or the wider CAPRMEDIO set—mechanically or almost mechanically.**

### Main projections

- **Entity Graph:** Entities and their relationships, built from Atom Subjects.
- **Terms Graph:** terms and their allowed typed relations.
- **Project Scope Unit Graph and Sources view:** Scope Units, their parents and authority/Delivery paths.
- **Applicable Methodology:** the methodology that applies to the selected scope, with conflicts resolved.
- **Requirement Lineage Map:** Requirements traced back to their Principles.

**Different views, one authority:** rebuild Projections from their sources instead of maintaining separate copies of project meaning.

Each Project has a `.caprmedio_<project_name>/` folder. Store persistent Journals in `_journal/` and persistent Projections in `_projection/`. Applicable Methodology, graph views and derived Journal views are Projections. Keep these storage roots separate from authority sources and temporary state.

### Extension and configuration

**CAPRMEDIO is extensible and configurable:** projects can add Types, Workflows, Tools and authoring rules within the allowed extension boundaries. Package reusable additions as Extensions. Settings choose available capabilities, their parameters and configuration precedence; they do not change the capabilities' meaning.

## Current boundaries

- More than one person can use CAPRMEDIO on a project, but the framework does not yet provide native support for team workflows.
- CAPRMEDIO is not only local-first; it is currently local-only.

## Status

The current framework version is declared in [version.toml](version.toml). The framework foundation is under active development; this is not yet a complete production toolchain.

## Version History

See [Version History](VERSION_HISTORY.md) for project origins and version milestones.

## Thanks

- **[Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy)**, for his fresh ideas—especially about graphs. His [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) says it vividly: “Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.” His [Software 3.0 talk](https://www.youtube.com/watch?v=XdbpCM4yGyE) develops the graph perspective further.
- **[Daniel Kravtsov](https://improvado.io/blog-authors/daniel-kravtsov)**, CEO and co-founder of [Improvado](https://improvado.io/company/about), for giving me the challenge of building a knowledge graph for my team. It showed me what graphs can achieve in practice. At Improvado, I also tried for the first time to build an internal product both with AI and by AI.
- **[Anatoly Levenchuk](https://t.me/ailev_blog)**, creator of the [First Principles Framework](https://github.com/ailev/FPF). I could never have built this project without FPF. I also maintain an [LLM-friendly FPF knowledge-graph toolkit](https://github.com/anatoly-m-maslennikov/levenchuk-fpf-knowledge-graph-toolkit).
