"""Public operation: resolve context, select, assess, verify currentness, report."""

from typing import Any

from .assessment import apply_checks, candidates, duplicate_sources
from .authority import resolve_context
from .context import load_sources, load_structure
from .contracts import empty_report
from .read_io import ReadContext, LimitReached
from .reporting import diagnostic, finish
from .selection import structural_names
from .settings import CEILINGS, resolve_limits
from .reference_context import references
from .check_operators import load_operators_registry


def execute(request: dict[str, Any]) -> dict[str, Any]:
    report = empty_report()
    report["selection"]["requested"] = request["selection"]
    report["selection"]["source_roots"] = request["source_roots"]
    report["execution"]["run_context"] = request.get("run_context", {})
    reader = ReadContext(request["allowed_read_roots"], dict(CEILINGS))
    try:
        limits, sources = resolve_limits(request, reader)
        report["execution"]["limits"] = limits
        report["execution"]["limit_sources"] = sources
    except OSError, ValueError, LimitReached:
        report["execution"]["diagnostics"].append(
            diagnostic(
                "SETTINGS_INVALID",
                "Settings are unreadable, stale, invalid, or cannot resolve every bounded limit.",
            )
        )
        return finish(report)
    try:
        assess(request, reader, report)
        report["currentness"] = reader.currentness()
    except LimitReached as error:
        report["execution"]["stopped_by"] = error.limit
        report["coverage"]["gaps"].append(
            diagnostic("LIMIT_REACHED", f"Outstanding assessment stopped at {error.limit}.")
        )
    except OSError:
        report["coverage"]["gaps"].append(
            diagnostic(
                "INPUT_UNAVAILABLE",
                "A required input is unavailable or outside the admitted boundary.",
            )
        )
    except ValueError, TypeError, KeyError, RecursionError:
        report["execution"]["diagnostics"].append(
            diagnostic(
                "ASSESSMENT_ERROR", "Assessment failed; no complete validation result is available."
            )
        )
    report["bindings"]["context"] = [
        {"path": p, "sha256": h} for p, h in reader.fingerprints.items()
    ]
    return finish(report)


def assess(request: dict[str, Any], reader: ReadContext, report: dict[str, Any]) -> None:
    sources = load_sources(request, reader, report)
    context = resolve_context(sources)
    report["bindings"]["rules"] = context.bindings
    report["coverage"]["rules"] = dict(
        required=context.required, supported=context.supported, unsupported=context.unsupported
    )
    report["coverage"]["gaps"].extend(context.gaps)
    structure = load_structure(request, reader, report)
    names = resolve_names(request, structure, report)
    records: list[dict[str, Any]] = []
    selected = candidates(request, reader, report, names, context.status_domains, records)
    reference_records, complete = references(request, reader, records, sources)
    if request.get("reference_roots") and not complete:
        report["coverage"]["gaps"].append(
            diagnostic(
                "REFERENCE_CONTEXT_INCOMPLETE",
                "Reference inventory is incomplete; independent carrier checks still run.",
            )
        )
    inputs = dict(
        request=request,
        structure=structure,
        sources=sources,
        references=reference_records,
        reference_complete=complete,
        operators_registry=load_operators_registry(request, reader),
    )
    report["selection"]["selected"] = [str(path) for path, _ in selected]
    for path, parsed in selected:
        reader.checkpoint()
        apply_checks(path, parsed, context, reader, report, inputs)
    duplicate_sources(report, reader)


def resolve_names(
    request: dict[str, Any], structure: dict[str, Any] | None, report: dict[str, Any]
) -> set[str] | None:
    selection = request["selection"]
    if "scope_unit" not in selection:
        return None
    try:
        if structure is None:
            raise ValueError("Missing Project Structure.")
        return structural_names(
            structure, selection["scope_unit"], selection.get("include_descendants", False)
        )
    except ValueError, TypeError, KeyError:
        report["coverage"]["gaps"].append(
            diagnostic(
                "SCOPE_UNRESOLVED",
                "Scope Unit selection requires an unambiguous Project Structure.",
            )
        )
        return None
