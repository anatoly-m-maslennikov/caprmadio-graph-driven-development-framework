---
subjects:
  governs:
    occurrent:
      - Programmatic Policy Decision Reconciliation
  depends_on:
    continuant:
      - Programmatic Policy
      - Method Authority
      - Evaluation Coverage
version: 2
updated_at: 2026-08-30 17:21:33 +0400
---
# Reconcile shared PROGRAMMATIC policy decisions

## Resolution boundary

This Analysis reconciles the eight candidate subjects frozen by CA-A-052 with accepted Project RMED authority, explicit Operator decisions in the originating sessions, the FPF evidence reviewed by the Project, and all active BSEED authority except the governed Journal and Work Journal subject.

The excluded Journal-subject constraints are `CAPRMEDIO-META-REQU-105`, `CAPRMEDIO-META-REQU-158`, `CAPRMEDIO-META-REQU-169`, `CAPRMEDIO-GOV-REQU-338`, `CAPRMEDIO-GOV-REQU-339`, `CAPRMEDIO-GOV-REQU-340`, `CAPRMEDIO-GOV-REQU-342`, `CAPRMEDIO-GOV-REQU-367`, and `CA-R-807`. An Atom that merely mentions a Journal while governing another subject remains applicable. In particular, the non-Journal logging requirements of `CAPRMEDIO-GOV-REQU-315` remain applicable.

This Analysis records dispositions and evidence. It does not itself establish RMED authority.

## Decision register

| Subject | Disposition | Reconciled meaning | Receiving use |
|---|---|---|---|
| Supported Python | Already governed | Preserve the accepted CA-R-1047, CA-M-110, CA-E-250, and CA-D-250 contract. CPython `3.12.*` and the standard-library-first runtime boundary remain selected in `pyproject.toml`; local Python versions do not expand support. | CA-P-072 and CA-P-073 must specialize rather than reopen this contract. |
| Platform envelope | Explicitly deferred | Make no general macOS, Ubuntu, Windows, or WSL support claim. Admit a platform or CI boundary only through an accepted Requirement with pinned external origin and current evidence. Present local use and stale workflows do not establish portability. | A later bounded Requirement, Delivery, and Evaluation chain. |
| Third-party prerequisites | Partly accepted and otherwise deferred | Keep the default runtime standard-library-first. The Operator accepted Pydantic only for admitted untrusted structured-data boundaries where its validation and schema capability justifies the dependency; it is not a universal internal object model. Ruff, mypy, pytest, Hypothesis, coverage, pyperf, mutation, fuzz, and golden-output implementations may be admitted only for a bounded evaluation or delivery capability. Their names do not belong in mechanism-neutral Evaluation claims. | CA-P-072 owns reusable selection policy; CA-P-073 owns mechanism-neutral claims; bounded Delivery, Implementation, configuration, and Evaluation carriers own actual admissions. |
| Python paradigm allocation | Accepted | Use responsibility-based multi-paradigm Python. Functions own deterministic transformations. Objects own state, lifecycle, resources, or replaceable adapters. Explicit typed interfaces separate replaceable technical boundaries. No universal OOP rule applies. | Separate irreducible Methods in CA-P-072. |
| Source-size guidance | Accepted as a ratcheted source boundary, not a correctness proof | New or materially changed hand-authored Python files target at most 200 physical lines. Executable units target 25 logical lines, may use 26–40 for one coherent job, and exceed 40 only through a documented exception. Existing oversized carriers are migration debt rather than an immediate whole-repository failure. Review cohesion, responsibility, dependency direction, complexity, and testability independently. Externalize large static mappings; generated Runtime and Delivery outputs are outside the source rule. | CA-P-072 owns Method claims; CA-P-073 owns mechanism-neutral acceptance and exception criteria; operative measurement remains Implementation. |
| Operational logging | Already governed outside the Journal subject | Programmatic components use structured operational diagnostics aligned with the non-Journal part of `CAPRMEDIO-GOV-REQU-315`: ERROR, WARNING, INFO, and DEBUG meanings; actionable failures; bounded DEBUG; contextual and sanitized records; declared retention, loss, back-pressure, and sink behavior; and observable logging failure without silently breaking primary work. Do not add a fifth severity through shared policy. | Separate logging Method, Evaluation, and Delivery carriers. Journal governance is not a receiving use of this Task. |
| Typing and automation | Accepted as a ratchet | Start with a bounded passing target, prevent regression, require the admitted profile for changed or new targets, and expand deliberately. Formatting, linting, typing, and behavioral checks remain distinct evidence. Exact tools, versions, and selected strictness live in their owning Delivery, Implementation, or canonical technical configuration rather than in Evaluation meaning. | CA-P-072 and CA-P-073, followed by bounded toolchain Delivery and Implementation. |
| Performance | Method accepted; budgets explicitly deferred | Profile before optimizing. Evaluate Hook, interactive, batch, MCP, App, and background surfaces with separate representative workloads. Preserve inputs, environment, baseline, distributions, and comparison thresholds. Do not invent numeric budgets before current baselines and Operator priorities exist. | CA-P-072 and CA-P-073 own reusable guidance and acceptance structure; later configuration or bounded authority owns numeric budgets. |

## Placement rules applied

1. One independently replaceable claim receives one Atom and one claim scope.
2. Language, algorithms, functions, classes, module structure, and reusable construction rules belong to Method.
3. Evaluation Atoms state claims, applicable conditions, acceptance, and failure dispositions without prescribing pytest, mypy, Pydantic, or another mechanism.
4. Package, installation, release, and operative tool choices belong to Delivery or Implementation as applicable.
5. Current selected values have one canonical configuration owner; other Atoms may define their allowed surface, meaning, defaults, and constraints without duplicating the selection.
6. External FPF findings are reviewed evidence, not Project authority. Accepted meanings must be materialized in the owning RMED roles.
7. Provenance is not evidence of correctness or currentness.

## Conflicts resolved

- The previous register treated Python and the default dependency boundary as open. The accepted Project R/M/E/D chain already governs them.
- A universal OOP rule conflicts with the admitted multi-paradigm evidence and is rejected.
- Immediate whole-repository enforcement of 25-line functions or 200-line files conflicts with the current implementation and overstates the heuristic. The accepted ratchet applies to new or materially changed source while legacy migration remains explicit work.
- Tool-named Evaluation claims conflict with mechanism-neutral Evaluation authority. Tool names move to bounded Delivery, Implementation, or configuration carriers.
- A shared logging policy with `CRITICAL` conflicts with the active four-level BSEED logging policy. Shared authoring uses only ERROR, WARNING, INFO, and DEBUG unless later authority changes the level set.
- Logging remains in scope, but Journal and Work Journal meaning, schema, append, replay, partition, and recovery are outside this Task.

## Explicit deferrals

CA-P-071 does not invent:

- a cross-platform support claim;
- exact versions or universal admission of development and evaluation tools;
- performance budgets without representative baselines; or
- Journal or Work Journal policy.

These deferrals do not block shared Method and Evaluation authoring because each has a named later owner and a bounded reliance limit.

## Evidence

- `CA-A-052-PROGRAMMATIC-ANALYSIS_RPRT--freeze-programmatic-method-and-evaluation-target.md`
- `fpf-reports/20260821T161903Z-fpf-sota-harvest-python-engineering-policies.md`
- `CA-R-1047`, `CA-M-110`, `CA-E-250`, and `CA-D-250`
- `CAPRMEDIO-META-REQU-092`, `CAPRMEDIO-META-REQU-094`, `CAPRMEDIO-META-REQU-100`, `CAPRMEDIO-META-REQU-104`, `CAPRMEDIO-META-REQU-106`, `CAPRMEDIO-META-REQU-163`, and `CAPRMEDIO-META-REQU-675`
- `CAPRMEDIO-GOV-REQU-301`, `CAPRMEDIO-GOV-REQU-314`, `CAPRMEDIO-GOV-REQU-315`, `CAPRMEDIO-GOV-REQU-625`, and `CAPRMEDIO-GOV-REQU-676`
- `CA-R-154`, `CA-R-918`, `CA-R-1006`, `CA-R-1009`, and `CA-R-1010`
