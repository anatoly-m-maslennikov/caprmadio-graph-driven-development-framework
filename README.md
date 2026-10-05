# CAPRMEDIO

**The Graph-Driven Development Framework**

## The Goal

If it can be built, CAPRMEDIO should help anyone build it if they are willing to invest the time and effort.

In practice, it should make AI-assisted development reliable from the first idea to production without losing meaning, traceability, or learning.

## What CAPRMEDIO is

CAPRMEDIO stores project knowledge as small artifacts connected by typed links. Humans and AI use this graph to understand the project, make changes, check consistency, and generate useful views.

## Why CAPRMEDIO works this way

Prompts, Skills, MCP, Apps and execution Tools form the harness (frontend and toolset) →\
the project's meaning must not depend on them →\
an explicit ontology/base model defines the core: concepts, relations and constraints.

### Ontology (methodology)

Sessions are ephemeral →\
we need a stable source of truth →\
specification.

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
load only the context needed without duplicating authority.

Natural-language phrases can be ambiguous →\
shared vocabulary + CAPRMEDIO Controlled English (CCE), a constrained way to write Claims →\
explicit, checkable Claims.

We need more than spec →\
Concerns, Analysis and Plans for understanding and planning →\
Requirements, Methods, Evaluations and Delivery (RMED) for specification →\
Implementation for code, tests and configuration →\
Operations for repeatable actions and workflows.

Implementation, tests and views rely on Claims →\
record the exact source Claim identities and revisions →\
trace results back to the specification.

Work changes the project →\
Journal records changes and execution →\
observed outcomes create the next Concerns.

### Harness (engine)

Files in folders are clear and inspectable →\
they currently hold authority →\
rescanning can become expensive →\
a derived graph database index supports queries and views. Database authority could be a future migration.

Repeated model reasoning costs time and tokens →\
every repeatable task that can be done deterministically should run programmatically →\
Tools.

We cannot put everything into one prompt →\
Tools retrieve context and assemble Prompts.

Wide-context reasoning →\
main session.

Narrow, repeatable work →\
bounded execution contexts and structured results.

Long actions should not block sessions →\
background orchestration →\
Workflow Orchestrator coordinates the steps →\
durable state, reconnectable runs, approvals and recovery.

Agents need a consistent interface →\
MCP exposes capabilities →\
Skills guide their use.

### Content roles and artifact forms

- **C — Concern:** problems, bugs, questions and opportunities.
- **A — Analysis:** analysis reports and rationale.
- **P — Plan:** backlog, tasks, epics and version plans.
- **R — Requirement:** specification of required outcomes.
- **M — Method:** how code should be written.
- **E — Evaluation:** quality assurance policies and test-case specifications.
- **D — Delivery:** target environments, CI/CD and release policies.
- **I — Implementation:** code, tests, configuration and CI/CD pipelines implementing all RMED.
- **O — Operations:** actions and workflows with steps to operate the project.

Content roles and Atom/Journal/Projection forms are separate classifications. Both follow MECE (complete, non-overlapping categories within their scope) and DRY (no independently maintained duplicate authority).

CAPRMEDIO keeps one coherent source of truth: Atoms express governed Claims; actual Implementation is what is built. Journals preserve change and execution history; Projections are derived, non-authoritative views.

[project_structure.toml](.caprmedio_caprmedio/project_structure.toml) is authoritative for Scope Units, hierarchy and path bindings; folders materialize those bindings, not structural authority.

Each Project has its own `.caprmedio_<project_name>/` folder. All persistent Journals belong in its `_journal/` directory; all persistent Projections belong in its `_projection/` directory, including Applicable Methodology, graph views and derived Journal views. These are the single storage roots for those artifact forms, separate from authoritative sources and ephemeral runtime state.

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
