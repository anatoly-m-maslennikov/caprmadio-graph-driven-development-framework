---
atom_id: CA-A-057
subjects:
  - programmatic-policy
  - method-authority
  - evaluation-coverage
  - scope-ownership
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  derived_from:
    - CA-A-053
    - CA-A-055
    - CA-A-056
---
# Reconcile PROGRAMMATIC specialization authority

## Frozen and final validation sets

The frozen CA-P-074 input was the exact active-or-draft Method and Evaluation
set selected by the following address expression at `2026-08-23 17:20:00 +0400`:

```text
.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/**/(05_method|06_evaluation)/**/*.md
```

The expression excluded any carrier below `archive/`, `done/`, or `canceled/`.
It resolved to 250 current carriers: 222 active and 28 drafts; 42 Methods and
208 Evaluations. This is the successor-inclusive continuation of CA-A-052,
CA-A-055, and CA-A-056; it includes the finalized shared PROGRAMMATIC set.

The final CA-P-074 validation set uses the same address expression and
exclusions at `2026-08-23 17:40:00 +0400`. It contains 291 current carriers:
264 active and 27 drafts; 56 Methods and 235 Evaluations. The set adds 42
accepted component-specific carriers and archives one duplicate Tool Method
candidate. No native Implementation carrier is in either set.

## Ownership matrix

| Owner | Current Methods | Current Evaluations | Current requirement and method ownership | Boundary retained |
|---|---:|---:|---|---|
| `PROGRAMMATIC` | 12 (11 active, 1 draft) | 20 (all active) | `CA-M-110`, `CA-M-157`–`CA-M-166`, and `CA-E-253`–`CA-E-272` serve `CA-R-1047`; the one `uv` draft remains an unaccepted configuration candidate. | Shared Python realization, deterministic transformation, state/lifecycle, typed-interface, effect, diagnostics, adoption, performance, and compatibility behavior only. |
| `TOOLS` and descendants | 23 (17 active, 6 drafts) | 191 (176 active, 15 drafts) | The Tool frontier remains `CA-R-802`–`CA-R-857`, `CA-R-1041`, `CA-R-1042`, `CA-R-1048`, `CA-R-1049`, `CA-R-1059`–`CA-R-1072`, and `CA-R-1120`–`CA-R-1156`. | Tool operation, runtime, manager/worker, scheduler, Hook, file-effect, Atom, projection, and delivery boundaries. |
| `APPS` and descendants | 6 (5 active, 1 draft) | 9 (5 active, 4 drafts) | `GRAPH_APP` owns `CA-R-1076` and `CA-R-1077`; `CODEX_PLUGIN` owns `CA-R-1073`–`CA-R-1075`; structural unit Requirements `CA-R-1100`–`CA-R-1104` are not behavioral M/E owners. | App interface, graph rendering/read service, and Codex-host package behavior. |
| `MCP` | 15 (all active) | 15 (all active) | `CA-M-167`–`CA-M-181` and `CA-E-273`–`CA-E-287` each directly serve one of `CA-R-1105`–`CA-R-1119`. | Transport admission, currentness, protocol, request control, least authority, and model-readable result behavior. |

`AGENTIC` and `SKILLS` are absent from this Task's validation set.

## Shared-versus-specialized lineage

Every active Method now has a direct `method_for` relation, every active
Evaluation has a direct `evaluation_for` relation, and no current Method or
Evaluation carries `child_of`. The owning Requirement or Method is therefore
the direct typed relation owner; this report records the applicable shared
Method without inventing an unregistered relation kind between Methods.

| Specialization surface | Applicable shared Method boundary | Child-specific acceptance owner |
|---|---|---|
| Tool deterministic parsers, planning, projections, and Finders | `CA-M-157`, `CA-M-159`, and `CA-M-160` only when the Tool has that transformation, interface, or decision/effect boundary | The owning Tool Method and its direct Tool Evaluation; no App or MCP behavior is asserted. |
| Tool runtime, file, subprocess, diagnostic, adoption, performance, and public CLI behavior | `CA-M-158`, `CA-M-161`–`CA-M-166` only at the named runtime, effect, diagnostic, changed-source, measured-performance, or declared-interface condition | `CA-M-142`, `CA-M-143`, and the owning Tool or descendant Method/Evaluation retain the Tool-specific procedure and evidence. |
| Graph App and Codex plugin behavior | `CA-M-110`, `CA-M-159`, `CA-M-163`, and `CA-M-166` only when a Python component, contract, diagnostic, or declared interface is present | `CA-M-150`–`CA-M-154`, `CA-E-067`, `CA-E-068`, and `CA-E-288`–`CA-E-290` own plugin and graph-App acceptance. |
| MCP registry, transport, protocol, cancellation, authority, and result behavior | `CA-M-110`, `CA-M-159`, `CA-M-163`, and `CA-M-166` only at a Python realization, typed boundary, diagnostic, or declared protocol contract | `CA-M-167`–`CA-M-181` and `CA-E-273`–`CA-E-287` own every MCP-specific procedure and acceptance boundary. |

No shared Method owns a component-specific Tool manager, worker, scheduler,
Hook, file-mutation flow, App interface, App service interaction, MCP protocol,
MCP request boundary, or MCP authority boundary.

## Duplicate removal and revision preservation

`CA-M--IMPL_METHOD-FR_ENGN_TOOLS--separate-deterministic-transformations-from-effects-and-lifecycle@3.md`
is archived because its shared deterministic/effect meaning is now canonically
owned by `CA-M-157` and `CA-M-160`. The remaining Tool effect draft was revised
to one Tool-operation-to-effect-result specialization of `CA-M-161`; the App
draft was revised to one App-interface-to-declared-service specialization of
`CA-M-158` and `CA-M-159`.

The final set preserves 15 exact active predecessor revisions in their local
archives: `CA-M-142`, `CA-M-143`, `CA-M-150`–`CA-M-154`, `CA-E-067`,
`CA-E-068`, `CA-E-076`, `CA-E-127`, and `CA-E-233`–`CA-E-235` plus `CA-E-237`.
Two revised candidate predecessors are also preserved in their local archives.
The revisions add direct lineage, separate two previously same-titled
structural-scope checks by carrier versus project-integrity boundary, and do
not alter native code.

## Child-specific coverage matrix

| Surface | Method coverage | Evaluation coverage | Result |
|---|---|---|---|
| `TOOLS` direct and descendants | 17 active component Methods and six candidates | 176 active component Evaluations and 15 candidates; `CA-E-291`–`CA-E-299` close the nine missing direct Method checks | Every active Tool Method has at least one direct active Evaluation. |
| `GRAPH_APP` | `CA-M-153`, `CA-M-154` | `CA-E-067`, `CA-E-068` | One App-specific evaluation owner per current App Method. |
| `CODEX_PLUGIN` | `CA-M-150`–`CA-M-152` | `CA-E-288`–`CA-E-290` | One plugin-specific evaluation owner per current plugin Method. |
| `MCP` | `CA-M-167`–`CA-M-181` | `CA-E-273`–`CA-E-287` | One protocol- and transport-specific evaluation owner per current MCP Method. |

The shared 20 PROGRAMMATIC Evaluations remain the sole owners of their
mechanism-neutral acceptance meanings. Child Evaluations evaluate a named
component Method or Requirement; they do not re-own a shared acceptance case.

## Final validation result

The frozen/final scanner parses all 291 current carriers as YAML with exactly
one H1. It finds 48 active Methods and 216 active Evaluations, zero active
Methods without `method_for`, zero active Evaluations without `evaluation_for`,
zero active Methods lacking a direct active Evaluation, zero cross-Scope
`child_of` relations, and zero duplicate current H1 summaries.

Boundary scans found no Tool manager, worker, scheduler, Hook, or file-mutation
constraint imposed on APPS or MCP, and no App interface or service-lifecycle
constraint imposed on TOOLS or MCP. `CA-M-128`, `CA-M-129`, `CA-M-155`, and
`CA-M-156` have a demonstrated, direct authorized-MCP-ingress dependency
because their owning current Tool Requirements (`CA-R-1041`, `CA-R-1042`,
`CA-R-1048`, and `CA-R-1049`) explicitly require it. That dependency does not
assign MCP protocol, request, or authority ownership to those Tools; MCP-only
authority remains in `CA-M-167`–`CA-M-181` and `CA-E-273`–`CA-E-287`. The
remaining cross-component mentions are bounded references to a source Tool or
an authorized ingress and do not transfer ownership.
