# CAPRMEDIO

**The Graph-Driven Development Framework**

## The Goal

If it can be built, CAPRMEDIO should help anyone build it if they are willing to invest the time and effort.

In practice, it should make AI-assisted development reliable from the first idea to production without losing meaning, traceability, or learning.

## What CAPRMEDIO is

CAPRMEDIO stores project knowledge as small artifacts connected by typed links. Humans and AI use this graph to understand the project, make changes, check consistency, and generate useful views.

The name describes four connected parts:

- **CAP** — problems, analysis, and planning: Concern, Analysis, and Plan.
- **RMED** — the specification: Requirement, Method, Evaluation, and Delivery.
- **I** — the actual code.
- **O** — Operations: repeatable actions and workflows.

## Why CAPRMEDIO works this way

Interfaces and Tools change → the project's meaning must not depend on them → an explicit ontology/base model defines the core: concepts, relations and constraints.

Prompts, Skills, MCP, Apps and execution Tools expose and operate that core → they form the harness: a frontend and toolset → they must be replaceable without changing the core.

### Ontology

Sessions are ephemeral → we need a stable source of truth → specification.

Spec grows → we need smaller units → one scope + one Claim = one Atom → splitting further adds no useful distinction.

Different use cases need different structures → keep one authoritative source → derive different views → graph.

The graph grows → identify Entities: the things the project describes → declare each Atom’s Subjects: what its Claim governs and what it depends on → organize them with typed nodes and relations → load only the context needed.

Small files can still be ambiguous → shared vocabulary + CCE → explicit, checkable Claims.

We need more than spec → C for problems, A for analysis, P for objectives/tasks/backlog → RMED for specification → I for implementation → O for repeatable actions and workflows.

Work changes the project → Journal records changes and execution → observed outcomes create the next Concerns.

### Harness

Files in folders are clear and inspectable → they currently hold authority → rescanning can become expensive → a derived graph database index supports queries and views → database state lives in `.caprmedio_runtime/`. Database authority could be a future migration.

Deterministic work → programmatic Tools → less repeated model reasoning and token use.

We cannot put everything into one prompt → Tools retrieve context and assemble Prompts → Workflow Orchestrator coordinates the steps.

Wide-context reasoning → main session. Narrow, repeatable work → bounded execution contexts and structured results.

Long actions should not block sessions → background orchestration → durable state, reconnectable runs, approvals and recovery.

Agents need a consistent interface → MCP exposes capabilities → Skills guide their use.

AI performs delegated work → the Operator retains authority → Evaluations check Claims and results.

## Current boundaries

- More than one person can use CAPRMEDIO on a project, but the framework does not yet provide native support for team workflows.
- CAPRMEDIO is not only local-first; it is currently local-only.

## Status

The current framework version is declared in [version.toml](version.toml). The framework foundation is under active development; this is not yet a complete production toolchain.

## History

Local development began on **13 July 2026 at 03:38 (UTC+4)** with the first project-content commit: `8c1c0ff` added the README. The first methodology documents followed at 03:39 (`1bbcef2`).

DSET Loops started with Domain → Spec + Eval/Test Plan → Implementation → Evaluation → Review → Reconciliation.

Selected version milestones from committed declarations:

- **0.2.0 — 15 July 2026:** the executable DSET toolchain gained skill-policy specifications.
- **0.3.0–0.3.1 — 15 July 2026:** layered work areas and bootstrap release preparation.
- **0.3.11 — August 2026:** CARMADIO/CAPRMADIO evolved into CAPRMEDIO. The base CAP, RMED, I and O content roles took shape; Atom, Journal and Projection became distinct artifact forms. BSEED Atoms formalized the bootstrap model.
- **0.4 — 3 October 2026:** BSEED gave way to the self-applicable Core Meta-Model and compiled Applicable Methodology. Stable Atom identities, Entities, Subjects, typed relations, CCE, explicit Scope Units, planning and reusable Workflows clarified the file-backed graph. Deterministic Tools and the first local RMED Atoms Base Revise MCP provided a working harness, with gather → check → fix, structured results and Journal records. The ontology/base model is explicitly separate from replaceable interfaces and Tools; graph services and orchestration remain under development.

## Thanks

- **[Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy)**, for his fresh ideas—especially about graphs. His [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) says it vividly: “Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.” His [Software 3.0 talk](https://www.youtube.com/watch?v=XdbpCM4yGyE) develops the graph perspective further.
- **[Daniel Kravtsov](https://improvado.io/blog-authors/daniel-kravtsov)**, CEO and co-founder of [Improvado](https://improvado.io/company/about), for giving me the challenge of building a knowledge graph for my team. It showed me what graphs can achieve in practice. At Improvado, I also tried for the first time to build an internal product both with AI and by AI.
- **[Anatoly Levenchuk](https://t.me/ailev_blog)**, creator of the [First Principles Framework](https://github.com/ailev/FPF). I could never have built this project without FPF. I also maintain an [LLM-friendly FPF knowledge-graph toolkit](https://github.com/anatoly-m-maslennikov/levenchuk-fpf-knowledge-graph-toolkit).
