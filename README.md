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

CAPRMEDIO therefore has two parts: ontology (methodology) and harness (engine). The engine must be replaceable without changing the core.

### Ontology (methodology)

Sessions are ephemeral →\
we need a stable source of truth →\
specification.

Spec grows →\
we need smaller units →\
one scope + one Claim = one Atom →\
splitting further adds no useful distinction.

Different use cases need different structures →\
keep one authoritative source →\
derive different views →\
graph.

The graph grows →\
identify Entities: the things the project describes →\
declare each Atom’s Subjects: what its Claim governs and what it depends on →\
organize them with typed nodes and relations →\
load only the context needed.

Small files can still be ambiguous →\
shared vocabulary + CCE →\
explicit, checkable Claims.

We need more than spec →\
C for problems, A for analysis, P for objectives/tasks/backlog →\
RMED for specification →\
I for implementation →\
O for repeatable actions and workflows.

Work changes the project →\
Journal records changes and execution →\
observed outcomes create the next Concerns.

### Harness (engine)

Files in folders are clear and inspectable →\
they currently hold authority →\
rescanning can become expensive →\
a derived graph database index supports queries and views →\
database state lives in `.caprmedio_runtime/`. Database authority could be a future migration.

Deterministic work →\
programmatic Tools →\
less repeated model reasoning and token use.

We cannot put everything into one prompt →\
Tools retrieve context and assemble Prompts →\
Workflow Orchestrator coordinates the steps.

Wide-context reasoning →\
main session.

Narrow, repeatable work →\
bounded execution contexts and structured results.

Long actions should not block sessions →\
background orchestration →\
durable state, reconnectable runs, approvals and recovery.

Agents need a consistent interface →\
MCP exposes capabilities →\
Skills guide their use.

AI performs delegated work →\
the Operator retains authority →\
Evaluations check Claims and results.

### Content roles and artifact forms

C — concerns; A — analysis; P — plans/tasks; R — requirements; M — methods; E — evaluations; D — delivery; I — actual Implementation; O — operations/workflows.

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
