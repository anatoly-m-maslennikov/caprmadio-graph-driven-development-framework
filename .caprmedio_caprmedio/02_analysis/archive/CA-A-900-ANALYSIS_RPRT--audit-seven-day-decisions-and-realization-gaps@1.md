---
subjects:
  declared:
    continuant:
      - development-flow
      - project-configuration
      - tool-authority
    occurrent:
      - realization
version: 1
updated_at: 2026-08-25 02:00:28 +0400
llm_session_ids:
  - codex:01a01cb4-e15e-78d1-9084-766bf6b0cd63
---
# Audit seven-day decisions and realization gaps

## Audit boundary and precedence

This Analysis reconciles every operator turn in Codex task
`01a01cb4-e15e-78d1-9084-766bf6b0cd63` from 2026-08-20 through
2026-08-25 with the current repository frontier. Later operator input in that
task takes precedence over earlier input. Current Principles, BSEED authority,
and then the applicable global and local Tiers constrain the resulting
disposition.

This Analysis distinguishes four states:

- `captured_and_realized`: current Atoms state the decision and current native
  carriers or generated outputs realize it;
- `captured_not_realized`: current authority states the decision but native
  delivery or operative proof is absent or contradicts it;
- `owned_by_existing_plan`: an accepted Plan already owns the remaining work;
- `superseded`: later higher or current authority replaced an earlier physical
  design detail without rejecting its purpose.

## Decision dispositions

| Decision group | Current disposition | Evidence and boundary |
| --- | --- | --- |
| `candidate = draft`; a draft has no assigned Atom ID; acceptance assigns `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>`; the remaining filename is mutable | `captured_and_realized` | `CAPRMEDIO-META-REQU-130`, `CA-R-728`, `CA-R-956`, `CAPRMEDIO-GOV-REQU-736`, and current empty-number-slot draft carriers own and apply the model. |
| Atoms and Journals are the governed source-of-truth forms; a Projection is a generated non-authoritative view regardless of generation mechanism | `captured_and_realized` | `CAPRMEDIO-META-REQU-125`, `CAPRMEDIO-META-REQU-657`, and current generated Projection carriers preserve the authority boundary. Native code remains current encoded realization rather than an independent owner of governed meaning. |
| Project Configuration is the human-editable settings authority; Project Scope Unit Graph state is a generated Projection | `captured_and_realized` | `CA-R-1052`, `CA-M-137`, `CAPRMEDIO-A-037`, `caprmedio_framework_settings.toml`, and the two current Scope Unit Graph Projection carriers implement the distinction. |
| One Scope Unit has one authority place and one Delivery place; rows expose name, prefix, parent, level, sibling order when ordered, coordinate, upstream unit, and relative authority and Delivery paths | `captured_and_realized` | `CA-R-843`, `CA-R-862`, `CA-R-626`, active Delivery Atoms, and the current Scope Unit Graph Projection own the model. `SEMNTC` and `OPER_DOC` remain the registered filename tokens. |
| Content-role folders are materialized only when their first carrier is created; `.DS_Store` is ignored rather than treated as governed cleanup | `captured_and_realized` | The live tree follows demand materialization and `.gitignore` excludes `.DS_Store`. Neither fact needs another CAP Atom. |
| Canonical Tool source is separate from runtime state | `superseded` | The earlier copy-and-execute-from-`.caprmedio_runtime` detail was replaced by current `CA-R-1065`: canonical source is installed as a content-addressed executable release in `.caprmedio_install`, while `.caprmedio_runtime` contains only mutable reconstructible state. This preserves the original source/runtime separation with a stricter installation boundary. |
| The Project Scope Unit Graph Projection should contain only the minimal then-requested sections | `superseded` | Current BSEED authority now requires registered projection, configuration, project, source-binding, authority-mode, and contribution metadata. The rejected blanket `source_frontier` and `graph_contributions` forms remain absent; newer registered sections are not the rejected forms. |
| FPF reports are Analysis material rather than RMED authority | `captured_and_realized` | Project-owned interpretations are Analysis Atoms. Raw FPF reports now remain external evidence addressed by review-envelope authority and do not become project authority merely because they exist under `fpf-reports`. |
| `ATOM_SEARCH`, `ATOM_READ`, `ATOM_CREATE`, `ATOM_UPDATE`, `ATOM_MOVE`, `ATOM_ARCHIVE`, `ATOM_PROMOTE`, and `ATOM_UPGRADE` are singular-or-bulk CAPRMEDIO Markdown Atom Tools; promotion assigns an operator-supplied ID and upgrade requires an explicit higher Tier | `captured_not_realized` for current Task carriers | `CA-R-863` through `CA-R-870`, their Methods, Evaluations, Deliveries, canonical source carriers, installed launchers, and tests realize ordinary Markdown Atom operations. The installed resolver nevertheless returns `atom-not-found` for active Task IDs such as `CA-P-062`, `CA-P-080`, and `CA-P-082` because their filenames begin with Work Sequence Numbers. `CA-P-901` owns this bounded repair. Folder-carried Epic Atoms remain outside the expressly Markdown-only Tool contract. |
| Every Atom mutation enters through authorized project-local MCP with a sealed human-origin Initiative, expected Revision or digest, canonical Tool delegation, and durable `COMMIT_TRIGGER` acknowledgement; direct Doer apply is rejected | `captured_not_realized` | `CA-R-1093` and `CA-R-1105` own the rule, but the native MCP directory has no operative service and `atom_operations.py` still accepts direct `apply=True` without an MCP delegation proof. `CA-P-902` owns closure. |
| Git and Journal are independent redundant provenance systems; concurrent producers and Journal preparation feed one fenced Git mutation gate; real-change and Journal-only commits remain separate; the Initiative summary supplies the first real-change message field | `owned_by_existing_plan_pending_identity_reconciliation` | Current PROGRAMMATIC Requirements, Methods, Evaluations, and Deliveries state the model. `CA-P-062` owns the higher BSEED conflict. Concurrent work created `04-CA-P-083-PROGRAMMATIC-TASK--realize-durable-asynchronous-commit-automation.md` with the required native realization boundary, but another concurrent BSEED Task also uses `CA-P-083`; those owners must establish unique identities before either carrier can be admitted. This Analysis creates no third semantic duplicate. |
| Brownfield `full`, `continue`, and `partial` adoption operate on an explicit frontier, create only CRMED drafts, first emit a reusable as-is Implementation Inventory, and then optionally derive structural drafts with the folder/file heuristic | `captured_not_realized` | `CA-R-1071`, `CA-R-1072`, `CA-M-101`, `CA-M-102`, `CA-E-291`, and `CA-E-292` state the two-step model. No canonical or installed `IMPLEMENTATION_INVENTORY` or `ADOPT_RECONCILE` implementation exists. `CA-P-903` owns closure. |
| Changed or candidate code passes a small pre-runtime `Implementation -> Evaluation -> repair` loop using applicable syntax, format, lint, type, and focused behavioral checks before later runtime reliance | `captured_not_realized` | `CA-A-048` records the accepted direction and current FRAMEWORK_ENGINE draft Methods and Evaluations refine it, but no accepted complete vertical slice or operative gate realizes it. `CA-P-904` owns closure. |
| The installed Scope Unit Graph generator and generated state must be current after the active migration | `owned_by_existing_plan` | `CA-P-046`, `CA-P-047`, and `CA-P-048` already own Tool update, derived-state rebuild, and stale-state closure. The current differing canonical and executed generator digests reopen those Tasks rather than justify duplicate Plans. |

## New Plan boundary

`CA-P-900` contains exactly the four newly bounded realization Tasks identified
above. It does not duplicate `CA-P-062`, the `CA-P-040` migration Epic, the
completed PROGRAMMATIC authority-repair Epics, or the already realized base
Atom Tool operations.

The execution order is intentional:

1. repair Atom Tool identity resolution for every Markdown role, including
   Work-Sequence-prefixed Task carriers;
2. deliver the MCP mutation gateway and enforce delegated apply;
3. deliver the two-step brownfield inventory and adoption Tools;
4. deliver the pre-runtime Evaluation and repair gate.

Durable asynchronous commit automation is excluded from `CA-P-900` because the
concurrent PROGRAMMATIC Task carrier already owns that exact outcome. Its
current `CA-P-083` collision is an identity-reconciliation condition, not a
reason to introduce another semantic Plan.

## Reopening conditions

Reopen this Analysis if later operator input changes one disposition, current
higher authority changes one boundary, an existing Plan is canceled or
replaced, the concurrent `CA-P-083` collision is not reconciled, an allegedly
absent native realization appears, or any Task closes without fresh installed
end-to-end evidence.
