#!/usr/bin/env python3
"""Report exact Claim Value-Set consolidation candidates without changing sources."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


TOOL_ID = "DETECT_CLAIM_VALUE_SET_CANDIDATES"
SCHEMA = "caprmedio.detect_claim_value_set_candidates.v3"
INACTIVE_DIRECTORY_NAMES = {
    "archive",
    "archived",
    "draft",
    "drafts",
    "done",
    "canceled",
    "cancelled",
    "solved",
    "handled",
}
QUALIFIER_OPERATORS = ("if", "unless", "when", "while", "before", "after", "until")
CONTENT_ROLE_DIRECTORY = re.compile(
    r"^[0-9]+_(?:concern|analysis|plan|requirement|method|evaluation|delivery|implementation|operations)$",
    re.IGNORECASE,
)


class DetectorError(RuntimeError):
    """A stable detector input or output failure."""

    def __init__(self, code: str, message: str, **details: object) -> None:
        self.code = code
        self.message = message
        self.details = details
        super().__init__(message)

    def record(self) -> dict[str, object]:
        record: dict[str, object] = {"code": self.code, "message": self.message}
        if self.details:
            record["details"] = self.details
        return record


@dataclass(frozen=True)
class Carrier:
    atom_id: str
    version: int
    carrier_path: str
    sha256: str
    statement: str
    governed_subject_set: tuple[tuple[str, str], ...]

    def record(self, value: str) -> dict[str, object]:
        return {
            "atom_id": self.atom_id,
            "atom_revision": self.version,
            "carrier_path": self.carrier_path,
            "carrier_sha256": self.sha256,
            "value": value,
        }


@dataclass(frozen=True)
class ParsedSingleValueClaim:
    property_name: str
    value: str
    qualifier: str


def top_block(frontmatter: str, key: str, path: str) -> list[str]:
    lines = frontmatter.splitlines()
    starts = [index for index, line in enumerate(lines) if re.fullmatch(rf"{re.escape(key)}:\s*", line)]
    if len(starts) > 1:
        raise DetectorError("frontmatter-duplicate-key", "Atom Carrier has a duplicate block", path=path, key=key)
    if not starts:
        return []
    block: list[str] = []
    for line in lines[starts[0] + 1 :]:
        if line and not line[0].isspace():
            break
        block.append(line)
    return block


def governed_subject_set(frontmatter: str, path: str) -> tuple[tuple[str, str], ...]:
    """Derive the canonical GOVERNS Subject set without treating it as Atom Scope."""

    block = top_block(frontmatter, "subjects", path)
    current_kind: str | None = None
    current_form: str | None = None
    members: list[tuple[str, str]] = []
    for line in block:
        kind_match = re.fullmatch(r"  ([a-z_]+):\s*", line)
        if kind_match:
            current_kind = kind_match.group(1)
            current_form = None
            continue
        form_match = re.fullmatch(r"    (continuant|occurrent):\s*(?:\[\])?\s*", line)
        if form_match:
            current_form = form_match.group(1).upper()
            continue
        item_match = re.fullmatch(r"      -\s*(.+?)\s*", line)
        if item_match and current_kind in {"governs", "declared"}:
            if current_form is None:
                raise DetectorError(
                    "governed-subject-temporal-form-missing",
                    "A GOVERNS Subject requires one Temporal Form",
                    path=path,
                )
            subject_path = scalar_value(item_match.group(1))
            if not subject_path:
                raise DetectorError("governed-subject-empty", "A GOVERNS Subject must not be empty", path=path)
            members.append((current_form, subject_path))
    if not 1 <= len(members) <= 2:
        raise DetectorError(
            "governed-subject-cardinality",
            "An Atom requires one or two GOVERNS Subjects",
            path=path,
            actual=len(members),
        )
    forms = [form for form, _ in members]
    if len(forms) != len(set(forms)):
        raise DetectorError(
            "governed-subject-temporal-form-cardinality",
            "An Atom permits at most one GOVERNS Subject per Temporal Form",
            path=path,
        )
    return tuple(sorted(set(members)))


def load_allowed_value_edges(path: Path) -> tuple[set[tuple[str, str]], str]:
    """Load exact Property/value pairs from one Entity Graph Projection."""

    if not path.is_file():
        raise DetectorError("term-system-projection-missing", "Term-System Projection is not a file", path=path.as_posix())
    data = path.read_bytes()
    try:
        payload = json.loads(data)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise DetectorError(
            "term-system-projection-invalid",
            "Term-System Projection must be UTF-8 JSON",
            path=path.as_posix(),
        ) from error
    projection = payload
    if isinstance(projection, dict) and "result" in projection:
        projection = projection.get("result")
    if isinstance(projection, dict) and "projection" in projection:
        projection = projection.get("projection")
    if not isinstance(projection, dict):
        raise DetectorError("term-system-projection-invalid", "Term-System Projection has no Projection object")
    term_system = projection.get("term_system")
    edges = term_system.get("edges") if isinstance(term_system, dict) else None
    if not isinstance(edges, list):
        raise DetectorError("term-system-projection-invalid", "Term-System Projection has no Term-System edges")
    allowed: set[tuple[str, str]] = set()
    for edge in edges:
        if not isinstance(edge, dict) or edge.get("relation") != "IS_ALLOWED_VALUE_OF":
            continue
        target = edge.get("target_subject")
        value = edge.get("source_term")
        if isinstance(target, str) and isinstance(value, str):
            allowed.add((target, value))
    return allowed, sha256(data)


def canonical_json(value: object, *, pretty: bool = False) -> str:
    if pretty:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def scalar_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value


def split_frontmatter(data: bytes, path: str) -> tuple[str, str] | None:
    if not data.startswith(b"---\n"):
        return None
    boundary = data.find(b"\n---\n", 4)
    if boundary < 0:
        raise DetectorError("frontmatter-unterminated", "Markdown frontmatter is unterminated", path=path)
    try:
        return data[4:boundary].decode("utf-8"), data[boundary + 5 :].decode("utf-8")
    except UnicodeDecodeError as error:
        raise DetectorError("carrier-not-utf8", "Markdown Carrier must be UTF-8", path=path) from error


def top_scalar(frontmatter: str, key: str, path: str) -> str | None:
    matches = re.findall(rf"(?m)^{re.escape(key)}:\s*([^\n]+?)\s*$", frontmatter)
    if len(matches) > 1:
        raise DetectorError("frontmatter-duplicate-key", "Atom Carrier has a duplicate scalar", path=path, key=key)
    return scalar_value(matches[0]) if matches else None


def display_path(path: Path, selected_folder: Path) -> str:
    return path.relative_to(selected_folder).as_posix()


def repository_path(path: Path, repository: Path) -> str:
    try:
        return path.resolve().relative_to(repository.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def is_inactive(path: Path, selected_folder: Path) -> bool:
    return any(part.lower() in INACTIVE_DIRECTORY_NAMES for part in path.relative_to(selected_folder).parts[:-1])


def local_atom_paths(selected_folder: Path) -> list[Path]:
    """Return only Atoms owned by the selected Scope Unit, excluding child Scope Units."""

    paths = list(selected_folder.glob("*.md"))
    for child in selected_folder.iterdir():
        if child.is_dir() and CONTENT_ROLE_DIRECTORY.fullmatch(child.name):
            paths.extend(child.rglob("*.md"))
    return sorted(set(paths))


def single_statement(body: str) -> str | None:
    """Return one direct CCE statement, refusing prose, headings, and lists."""

    lines = [line.strip() for line in body.splitlines() if line.strip()]
    if not lines or not lines[0].startswith("# "):
        return None
    claim_lines = lines[1:]
    if len(claim_lines) != 1:
        return None
    statement = claim_lines[0]
    if statement.startswith(("#", "-", "*", "1. ", "```")):
        return None
    return statement


def parse_single_value_claim(statement: str) -> ParsedSingleValueClaim | None:
    """Parse only `<Property>: <Value>[ **if** <Qualifier>].`.

    This intentionally excludes natural-language similarity, multiple clauses,
    values already expressed as sets, and every other CCE form.  The detector
    may report only exact, mechanically parseable statements.
    """

    if not statement.endswith("."):
        return None
    head = statement[:-1]
    qualifier = ""
    parts = re.split(
        rf"\s+(\*\*(?:{'|'.join(QUALIFIER_OPERATORS)})\*\*)\s+",
        head,
        maxsplit=1,
    )
    if len(parts) == 3:
        principal, operator, condition = parts
        if not condition or "**" in condition:
            return None
        qualifier = f"{operator} {condition.strip()}"
    elif len(parts) == 1:
        principal = parts[0]
    else:
        return None
    if ": " not in principal:
        return None
    property_name, value = principal.rsplit(": ", 1)
    property_name = property_name.strip()
    if not property_name or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_ /:-]*", property_name):
        return None
    value = value.strip()
    if not value or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_ /-]*", value):
        return None
    return ParsedSingleValueClaim(property_name=property_name, value=value, qualifier=qualifier)


def discover_active_carriers(selected_folder: Path) -> tuple[list[Carrier], dict[str, int]]:
    carriers: list[Carrier] = []
    counts = defaultdict(int)
    for path in local_atom_paths(selected_folder):
        if is_inactive(path, selected_folder):
            counts["inactive_directory_carriers_skipped"] += 1
            continue
        relative_path = display_path(path, selected_folder)
        data = path.read_bytes()
        split = split_frontmatter(data, relative_path)
        if split is None:
            counts["non_atom_markdown_skipped"] += 1
            continue
        frontmatter, body = split
        status = top_scalar(frontmatter, "status", relative_path)
        if status is not None and status.lower() != "active":
            counts["nonactive_status_carriers_skipped"] += 1
            continue
        atom_id = top_scalar(frontmatter, "atom_id", relative_path) or path.stem.split("--", 1)[0]
        raw_version = top_scalar(frontmatter, "version", relative_path)
        if not atom_id:
            raise DetectorError("atom-id-missing", "Atom Carrier has no identity", path=relative_path)
        if raw_version is None or not re.fullmatch(r"[1-9][0-9]*", raw_version):
            raise DetectorError(
                "atom-version-invalid",
                "Atom Carrier requires a positive integer version",
                path=relative_path,
                value=raw_version,
            )
        statement = single_statement(body)
        if statement is None:
            counts["noncanonical_claim_shape_skipped"] += 1
            continue
        if parse_single_value_claim(statement) is None:
            counts["unparseable_single_value_claim_skipped"] += 1
            continue
        carriers.append(
            Carrier(
                atom_id=atom_id,
                version=int(raw_version),
                carrier_path=relative_path,
                sha256=sha256(data),
                statement=statement,
                governed_subject_set=governed_subject_set(frontmatter, relative_path),
            )
        )
    return carriers, dict(sorted(counts.items()))


def source_frontier_digest(selected_folder: Path) -> tuple[str, int]:
    """Digest active Atom carrier bytes, including ones outside the narrow parser."""

    records: list[dict[str, str]] = []
    for path in local_atom_paths(selected_folder):
        if is_inactive(path, selected_folder):
            continue
        relative_path = display_path(path, selected_folder)
        data = path.read_bytes()
        split = split_frontmatter(data, relative_path)
        if split is None:
            continue
        frontmatter, _ = split
        status = top_scalar(frontmatter, "status", relative_path)
        if status is not None and status.lower() != "active":
            continue
        records.append({"carrier_path": relative_path, "carrier_sha256": sha256(data)})
    return sha256(canonical_json(records).encode("utf-8")), len(records)


def build_report(
    selected_folder: Path,
    *,
    term_system_projection: Path,
    repository: Path | None = None,
) -> dict[str, object]:
    if not selected_folder.is_dir():
        raise DetectorError("source-folder-missing", "Source folder is not a directory", path=selected_folder.as_posix())
    carriers, skipped = discover_active_carriers(selected_folder)
    digest, active_carrier_count = source_frontier_digest(selected_folder)
    allowed_values, term_system_digest = load_allowed_value_edges(term_system_projection)
    scope_unit_coordinate = repository_path(selected_folder, repository or Path.cwd())
    grouped: dict[tuple[tuple[tuple[str, str], ...], str, str], list[tuple[Carrier, ParsedSingleValueClaim]]] = defaultdict(list)
    disallowed_value_claims = 0
    for carrier in carriers:
        parsed = parse_single_value_claim(carrier.statement)
        assert parsed is not None
        if (parsed.property_name, parsed.value) not in allowed_values:
            disallowed_value_claims += 1
            continue
        grouped[(carrier.governed_subject_set, parsed.property_name, parsed.qualifier)].append((carrier, parsed))

    candidate_groups: list[dict[str, object]] = []
    ambiguous_groups = 0
    for (governed_subjects, property_name, qualifier), members in sorted(grouped.items()):
        if len(members) < 2:
            continue
        values = [parsed.value for _, parsed in members]
        if len(set(values)) != len(values):
            ambiguous_groups += 1
            continue
        ordered_members = sorted(members, key=lambda item: (item[1].value, item[0].atom_id, item[0].carrier_path))
        ordered_values = [parsed.value for _, parsed in ordered_members]
        values_text = ", ".join(ordered_values)
        proposed_claim = f"{property_name}: ({values_text})"
        if qualifier:
            proposed_claim = f"{proposed_claim} {qualifier}"
        proposed_claim += "."
        candidate_groups.append(
            {
                "fingerprint": {
                    "atom_scope": {
                        "scope_unit_carrier": scope_unit_coordinate,
                    },
                    "governed_subject_set": [
                        {"temporal_form": temporal_form, "subject_path": subject_path}
                        for temporal_form, subject_path in governed_subjects
                    ],
                    "claim_scope": property_name,
                    "property": property_name,
                    "qualifier": qualifier,
                },
                "atom_ids": [carrier.atom_id for carrier, _ in ordered_members],
                "contributors": [carrier.record(parsed.value) for carrier, parsed in ordered_members],
                "proposed_claim": proposed_claim,
            }
        )

    diagnostics: list[dict[str, object]] = []
    if ambiguous_groups:
        diagnostics.append(
            {
                "severity": "info",
                "code": "duplicate-value-group-not-reported",
                "message": "Groups with duplicate values are not consolidation candidates.",
                "details": {"group_count": ambiguous_groups},
            }
        )
    if disallowed_value_claims:
        diagnostics.append(
            {
                "severity": "info",
                "code": "unproven-allowed-value-claim-not-reported",
                "message": "Claims whose value is not proven as an allowed value of the parsed Property were not reported.",
                "details": {"claim_count": disallowed_value_claims},
            }
        )
    diagnostics.append(
        {
            "severity": "info",
            "code": "narrow-parser-boundary",
            "message": "Unparseable or semantically similar prose is out of scope and produces no inferred candidate.",
        }
    )
    return {
        "schema": SCHEMA,
        "tool": TOOL_ID,
        "mode": "report_only",
        "source_frontier": {
            "folder": scope_unit_coordinate,
            "atom_scope_unit_carrier": scope_unit_coordinate,
            "active_carrier_count": active_carrier_count,
            "digest_sha256": digest,
        },
        "term_system_projection": {
            "path": repository_path(term_system_projection, repository or Path.cwd()),
            "digest_sha256": term_system_digest,
        },
        "exact_statement_grammar": "<Property>: <Value>[ **if** <Qualifier>].",
        "candidate_groups": candidate_groups,
        "diagnostics": diagnostics,
        "counts": {
            "parseable_single_value_claims": len(carriers),
            "candidate_groups": len(candidate_groups),
            **skipped,
        },
    }


def output_path_is_safe(output: Path, selected_folder: Path) -> None:
    try:
        output.resolve().relative_to(selected_folder.resolve())
    except ValueError:
        return
    raise DetectorError(
        "output-inside-source-frontier",
        "Report output must not be written inside the selected Source frontier",
        output=output.as_posix(),
        source_folder=selected_folder.as_posix(),
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scope-unit-folder",
        required=True,
        type=Path,
        help="Scope Unit folder whose local active Atom frontier is inspected",
    )
    parser.add_argument("--repository", type=Path, default=Path.cwd(), help="Repository root for stable Carrier paths")
    parser.add_argument(
        "--term-system-projection",
        required=True,
        type=Path,
        help="Entity Graph Projection that proves IS_ALLOWED_VALUE_OF relations",
    )
    parser.add_argument("--output", type=Path, help="Optional report path outside the selected Source frontier")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        selected_folder = args.scope_unit_folder.resolve()
        report = build_report(
            selected_folder,
            term_system_projection=args.term_system_projection.resolve(),
            repository=args.repository.resolve(),
        )
        payload = canonical_json(report, pretty=args.pretty)
        if args.output is None:
            sys.stdout.write(payload)
            return 0
        output = args.output.resolve()
        output_path_is_safe(output, selected_folder)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8", newline="\n")
        return 0
    except DetectorError as error:
        sys.stderr.write(canonical_json({"schema": SCHEMA, "error": error.record()}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
