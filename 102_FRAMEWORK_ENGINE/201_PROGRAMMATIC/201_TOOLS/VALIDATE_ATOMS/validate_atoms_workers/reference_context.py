"""Bounded reference context, separate from selected validation targets."""

from pathlib import Path
from typing import Any

from .parsing import CarrierError, parse_carrier
from .read_io import ReadContext, LimitReached


def _load_reference(
    path: Path, reader: ReadContext, cached: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    if str(path) in cached:
        return cached[str(path)]
    parsed = parse_carrier(reader.read(path), path)
    return dict(path=path, metadata=parsed.metadata, parsed=parsed)


def references(
    request: dict[str, Any],
    reader: ReadContext,
    existing: list[dict[str, Any]],
    sources: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], bool]:
    cached = {str(row["path"]): dict(row, metadata=dict(row["metadata"])) for row in existing}
    roots = request.get("reference_roots", [])
    explicit_frontier = bool(roots)
    # Selected carriers arrive as ``existing`` because assessment has already
    # read them.  With explicit roots they are only a cache: a selected
    # candidate does not become its own (or another target's) reference unless
    # the caller actually admitted its path through that frontier.  Without
    # roots retain the legacy partial context, but never call it complete.
    rows = {} if explicit_frontier else dict(cached)
    complete = explicit_frontier
    for source in sources:
        path = Path(source["binding"]["path"])
        row = rows.setdefault(
            str(path), dict(path=path, metadata=dict(source["metadata"]), text=source["text"])
        )
        row["binding"] = source["binding"]
        # Supplied exact authority identity is reference context, never a repair
        # to a selected validation target or evidence of missing activity.
        for field in ("atom_id", "version"):
            row["metadata"].setdefault(field, source["binding"][field])
    paths: set[Path] = set()
    for root in roots:
        try:
            reader.allowed(Path(root)).stat()
            paths.update(reader.discover([root]))
            if len(paths) > reader.limits["max_candidates"]:
                raise LimitReached("max_candidates")
        except OSError as error:
            complete = False
            rows.setdefault(root, dict(path=Path(root), metadata={}, parsed=error))
    for path in sorted(paths):
        if str(path) in rows:
            continue
        try:
            rows[str(path)] = _load_reference(path, reader, cached)
        except (OSError, CarrierError) as error:
            rows[str(path)] = dict(path=path, metadata={}, parsed=error)
            complete = False
    if any(isinstance(row.get("parsed"), Exception) for row in rows.values()):
        complete = False
    return [rows[path] for path in sorted(rows)], complete
