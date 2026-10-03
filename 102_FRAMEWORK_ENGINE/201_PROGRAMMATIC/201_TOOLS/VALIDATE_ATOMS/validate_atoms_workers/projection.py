"""Compare projected carrier bytes; never repair or normalize the source."""

from pathlib import Path
import re
from typing import Any

from .parsing import ParsedCarrier
from .read_io import ReadContext
from .reporting import diagnostic


def verify_projection(
    parsed: ParsedCarrier, path: Path, reader: ReadContext, assessment: dict[str, Any]
) -> dict[str, Any] | None:
    if "projection" not in parsed.metadata:
        assessment["representation"] = "source"
        return None
    block = parsed.metadata["projection"]
    if (
        not isinstance(block, dict)
        or set(block) != {"source_carrier_path"}
        or not isinstance(block["source_carrier_path"], str)
        or not block["source_carrier_path"]
    ):
        return diagnostic("PROJECTION_BINDING", "Invalid original-Atom binding.", str(path))
    source = path.parent / block["source_carrier_path"]
    assessment["source_path"] = str(source.absolute())
    source = reader.allowed(source)
    assessment["source_path"] = str(source)
    raw = reader.read(source)
    # Recognize only a top-level block mapping; other YAML is an explicit gap.
    # Restrict removal to raw frontmatter, never a similarly named body block.
    opening = re.match(r"---\r?\n", parsed.text)
    closing = re.search(r"(?m)^---\r?\n", parsed.text[opening.end() :]) if opening else None
    if opening is None or closing is None:
        raise ValueError("Projection lacks supported raw frontmatter boundaries.")
    prefix_end = opening.end()
    frontmatter = parsed.text[prefix_end : prefix_end + closing.start()]
    match = re.search(r"(?m)^projection:[ \t]*\r?\n(?:[ \t]+[^\r\n]*\r?\n)+", frontmatter)
    if match is None:
        raise ValueError("Projection fidelity needs a supported block mapping.")
    without_binding = (
        parsed.text[: prefix_end + match.start()] + parsed.text[prefix_end + match.end() :]
    )
    if without_binding.encode("utf-8") != raw:
        return diagnostic(
            "PROJECTION_FIDELITY",
            "Projected bytes differ from source after removing the binding.",
            str(path),
        )
    assessment["representation"] = "projected"
    return None
