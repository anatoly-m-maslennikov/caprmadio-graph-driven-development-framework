#!/usr/bin/env python3
"""Derive report-only signatures for a restricted static Scope Expression subset."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


TOOL_ID = "DERIVE_SCOPE_CANONICAL_SIGNATURES"
SCHEMA = "caprmedio.derive_scope_canonical_signatures.v1"
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
RESTRICTED_OPERATORS = {"and", "or"}
BOLD_TOKEN_PATTERN = re.compile(r"\*\*([^*\n]+?)\*\*")


class ScopeSignatureError(RuntimeError):
    """A stable input, parsing, or output-boundary failure."""

    def __init__(self, code: str, message: str, **details: object) -> None:
        self.code = code
        self.message = message
        self.details = details
        super().__init__(message)

    def record(self, *, severity: str = "info") -> dict[str, object]:
        record: dict[str, object] = {"severity": severity, "code": self.code, "message": self.message}
        if self.details:
            record["details"] = self.details
        return record


@dataclass(frozen=True)
class Carrier:
    atom_id: str
    version: int
    carrier_path: str
    sha256: str
    scope_expression: str | None

    def evidence(self) -> dict[str, object]:
        return {
            "atom_id": self.atom_id,
            "atom_revision": self.version,
            "carrier_path": self.carrier_path,
            "carrier_sha256": self.sha256,
        }


@dataclass(frozen=True)
class ScopeSignature:
    """A structural non-authoritative signature for one static Scope Expression."""

    operator: str
    atomic_identities: tuple[str, ...]

    def record(self) -> dict[str, object]:
        return {"operator": self.operator, "atomic_identities": list(self.atomic_identities)}

    def digest(self) -> str:
        return sha256(canonical_json(self.record()).encode("utf-8"))


def canonical_json(value: object, *, pretty: bool = False) -> str:
    if pretty:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def scalar_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def split_frontmatter(data: bytes, path: str) -> tuple[str, str] | None:
    if not data.startswith(b"---\n"):
        return None
    boundary = data.find(b"\n---\n", 4)
    if boundary < 0:
        raise ScopeSignatureError("frontmatter-unterminated", "Markdown frontmatter is unterminated", path=path)
    try:
        return data[4:boundary].decode("utf-8"), data[boundary + 5 :].decode("utf-8")
    except UnicodeDecodeError as error:
        raise ScopeSignatureError("carrier-not-utf8", "Markdown Carrier must be UTF-8", path=path) from error


def top_scalar(frontmatter: str, key: str, path: str) -> str | None:
    matches = re.findall(rf"(?m)^{re.escape(key)}:\s*([^\n]+?)\s*$", frontmatter)
    if len(matches) > 1:
        raise ScopeSignatureError("frontmatter-duplicate-key", "Atom Carrier has a duplicate scalar", path=path, key=key)
    return scalar_value(matches[0]) if matches else None


def display_path(path: Path, selected_folder: Path) -> str:
    return path.relative_to(selected_folder).as_posix()


def is_inactive(path: Path, selected_folder: Path) -> bool:
    return any(part.lower() in INACTIVE_DIRECTORY_NAMES for part in path.relative_to(selected_folder).parts[:-1])


def scope_section(body: str) -> str | None:
    """Return the one line from an exact `## Scope` section, if present.

    Existing Task Carrier syntax delivers a Scope Expression in this section.
    Other Carrier shapes are deliberately skipped instead of being inferred.
    """

    lines = body.splitlines()
    headers = [index for index, line in enumerate(lines) if line.strip() == "## Scope"]
    if not headers:
        return None
    if len(headers) != 1:
        raise ScopeSignatureError("scope-section-ambiguous", "Atom Carrier has multiple `## Scope` sections")
    start = headers[0] + 1
    end = len(lines)
    for index in range(start, len(lines)):
        if re.fullmatch(r"#{1,2}\s+.+", lines[index].strip()):
            end = index
            break
    values = [line.strip() for line in lines[start:end] if line.strip()]
    if len(values) != 1:
        raise ScopeSignatureError(
            "scope-expression-shape-invalid",
            "The `## Scope` section must contain exactly one unwrapped Scope Expression line",
        )
    return values[0]


def has_outer_parentheses(text: str) -> bool:
    if not text.startswith("(") or not text.endswith(")"):
        return False
    depth = 0
    for index, character in enumerate(text):
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
            if depth == 0:
                return index == len(text) - 1
            if depth < 0:
                return False
    return False


def reject_excluded_operators(text: str) -> None:
    for match in BOLD_TOKEN_PATTERN.finditer(text):
        operator = match.group(1).strip()
        if operator not in RESTRICTED_OPERATORS:
            raise ScopeSignatureError(
                "operator-excluded",
                "Restricted Scope canonical-signature grammar excludes this CCE Operator",
                operator=operator,
            )


def split_top_level_operands(body: str) -> tuple[str, list[str]]:
    """Split one union or intersection and reject all mixed or unknown operators."""

    reject_excluded_operators(body)
    separators: list[tuple[int, int, str]] = []
    depth = 0
    index = 0
    while index < len(body):
        character = body[index]
        if character == "(":
            depth += 1
            index += 1
            continue
        if character == ")":
            depth -= 1
            if depth < 0:
                raise ScopeSignatureError("parenthesis-unbalanced", "Scope Expression has an unmatched closing parenthesis")
            index += 1
            continue
        matched = False
        for operator in sorted(RESTRICTED_OPERATORS):
            token = f"**{operator}**"
            if body.startswith(token, index):
                if depth == 0:
                    separators.append((index, index + len(token), operator))
                index += len(token)
                matched = True
                break
        if not matched:
            index += 1
    if depth != 0:
        raise ScopeSignatureError("parenthesis-unbalanced", "Scope Expression has an unmatched opening parenthesis")
    if not separators:
        raise ScopeSignatureError(
            "set-operator-missing",
            "Restricted Scope canonical-signature grammar requires **and** or **or**",
        )
    operators = {operator for _, _, operator in separators}
    if len(operators) != 1:
        raise ScopeSignatureError("mixed-operator", "Scope Expression mixes **and** and **or**")
    operator = next(iter(operators))
    operands: list[str] = []
    start = 0
    for token_start, token_end, _ in separators:
        operand = body[start:token_start].strip()
        if not operand:
            raise ScopeSignatureError("operand-empty", "Scope Expression has an empty operand")
        operands.append(operand)
        start = token_end
    final_operand = body[start:].strip()
    if not final_operand:
        raise ScopeSignatureError("operand-empty", "Scope Expression has an empty operand")
    operands.append(final_operand)
    return operator, operands


def parse_atomic_identity(text: str, known_atom_ids: set[str]) -> str:
    identity = text.strip()
    if identity not in known_atom_ids:
        raise ScopeSignatureError(
            "atomic-identity-unresolved",
            "Restricted Scope grammar accepts only an exact active Atom ID in the selected source folder",
            identity=identity,
        )
    return identity


def parse_restricted_scope_group(expression: str, known_atom_ids: set[str]) -> ScopeSignature:
    """Parse a static Atom-ID union/intersection without distributing operators."""

    text = expression.strip()
    if not has_outer_parentheses(text):
        raise ScopeSignatureError(
            "group-parentheses-required",
            "Restricted Scope canonical-signature grammar requires one enclosing parenthesis pair",
        )
    operator, operands = split_top_level_operands(text[1:-1])
    atomic_identities: list[str] = []
    for operand in operands:
        if has_outer_parentheses(operand):
            nested = parse_restricted_scope_group(operand, known_atom_ids)
            if nested.operator != operator:
                raise ScopeSignatureError(
                    "mixed-operator",
                    "Nested Scope Expression group has a different set operator",
                    outer_operator=operator,
                    nested_operator=nested.operator,
                )
            atomic_identities.extend(nested.atomic_identities)
        else:
            atomic_identities.append(parse_atomic_identity(operand, known_atom_ids))
    return ScopeSignature(operator=operator, atomic_identities=tuple(sorted(set(atomic_identities))))


def discover_active_carriers(selected_folder: Path) -> tuple[list[Carrier], dict[str, int], list[dict[str, object]]]:
    carriers: list[Carrier] = []
    counts: defaultdict[str, int] = defaultdict(int)
    diagnostics: list[dict[str, object]] = []
    for path in sorted(selected_folder.rglob("*.md")):
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
            raise ScopeSignatureError("atom-id-missing", "Atom Carrier has no identity", path=relative_path)
        if raw_version is None or not re.fullmatch(r"[1-9][0-9]*", raw_version):
            raise ScopeSignatureError(
                "atom-version-invalid",
                "Atom Carrier requires a positive integer version",
                path=relative_path,
                value=raw_version,
            )
        try:
            expression = scope_section(body)
        except ScopeSignatureError as error:
            counts["invalid_scope_sections_skipped"] += 1
            diagnostics.append({**error.record(), "details": {**error.details, "carrier_path": relative_path, "atom_id": atom_id}})
            expression = None
        if expression is None:
            counts["scope_section_absent_or_invalid_skipped"] += 1
        carriers.append(
            Carrier(
                atom_id=atom_id,
                version=int(raw_version),
                carrier_path=relative_path,
                sha256=sha256(data),
                scope_expression=expression,
            )
        )
    return carriers, dict(sorted(counts.items())), diagnostics


def source_frontier_digest(selected_folder: Path) -> tuple[str, int]:
    """Digest every active Atom byte sequence in the selected source frontier."""

    records: list[dict[str, str]] = []
    for path in sorted(selected_folder.rglob("*.md")):
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


def build_report(selected_folder: Path) -> dict[str, object]:
    """Derive only static Scope signatures; source Carriers remain byte-identical."""

    source = selected_folder.resolve()
    if not source.is_dir():
        raise ScopeSignatureError("source-folder-missing", "Source folder is not a directory", path=source.as_posix())
    carriers, skipped, diagnostics = discover_active_carriers(source)
    known_atom_ids: dict[str, Carrier] = {}
    for carrier in carriers:
        previous = known_atom_ids.get(carrier.atom_id)
        if previous is not None:
            raise ScopeSignatureError(
                "atom-identity-ambiguous",
                "Selected source folder has multiple active Carriers for one Atom ID",
                atom_id=carrier.atom_id,
                first_carrier=previous.carrier_path,
                second_carrier=carrier.carrier_path,
            )
        known_atom_ids[carrier.atom_id] = carrier
    counts: defaultdict[str, int] = defaultdict(int, skipped)
    occurrences: list[dict[str, object]] = []
    for carrier in carriers:
        if carrier.scope_expression is None:
            continue
        try:
            signature = parse_restricted_scope_group(carrier.scope_expression, set(known_atom_ids))
        except ScopeSignatureError as error:
            counts["restricted_boundary_exclusions"] += 1
            diagnostics.append(
                {
                    **error.record(),
                    "details": {
                        **error.details,
                        **carrier.evidence(),
                        "source_section": "Scope",
                        "source_expression": carrier.scope_expression,
                    },
                }
            )
            continue
        occurrences.append(
            {
                **carrier.evidence(),
                "source_section": "Scope",
                "source_expression": carrier.scope_expression,
                "canonical_scope_signature": signature.record(),
                "canonical_scope_signature_sha256": signature.digest(),
            }
        )
        counts["canonical_signatures"] += 1
    by_signature: defaultdict[str, list[str]] = defaultdict(list)
    for occurrence in occurrences:
        by_signature[str(occurrence["canonical_scope_signature_sha256"])].append(str(occurrence["atom_id"]))
    duplicate_signature_groups = [
        {"canonical_scope_signature_sha256": digest, "atom_ids": sorted(atom_ids)}
        for digest, atom_ids in sorted(by_signature.items())
        if len(atom_ids) > 1
    ]
    frontier_digest, active_carrier_count = source_frontier_digest(source)
    counts["active_atom_carriers"] = active_carrier_count
    counts["scope_expression_occurrences"] = sum(carrier.scope_expression is not None for carrier in carriers)
    counts["duplicate_signature_groups"] = len(duplicate_signature_groups)
    return {
        "schema": SCHEMA,
        "tool_id": TOOL_ID,
        "mode": "report_only",
        "source_folder": source.as_posix(),
        "source_frontier": {"active_atom_carrier_count": active_carrier_count, "sha256": frontier_digest},
        "restricted_grammar": {
            "scope_group": "(atom_id **or** atom_id [**or** atom_id ...]) | (atom_id **and** atom_id [**and** atom_id ...])",
            "atom_id": "one exact active Atom ID in the selected source folder",
            "signature": {"operator": "and | or", "atomic_identities": "sorted unique non-empty list"},
            "exclusions": [
                "mixed **and** and **or** groups",
                "**without**, **where**, **all**, and every other CCE Operator",
                "functions, Entity-kind selectors, descendant or dynamic selectors",
                "unresolved Atomic Identities and changing source frontiers",
                "unbalanced parentheses and unparseable prose",
            ],
        },
        "signatures": occurrences,
        "duplicate_canonical_scope_signature_groups": duplicate_signature_groups,
        "diagnostics": diagnostics,
        "counts": dict(sorted(counts.items())),
    }


def output_is_inside_source(source: Path, output: Path) -> bool:
    try:
        output.resolve().relative_to(source.resolve())
    except ValueError:
        return False
    return True


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-folder", required=True, type=Path, help="Folder containing active Atom Carriers to inspect")
    parser.add_argument("--output", type=Path, help="Optional JSON report path outside the selected source folder")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    try:
        args = parse_args(argv)
        source = args.source_folder.resolve()
        if args.output is not None and output_is_inside_source(source, args.output):
            raise ScopeSignatureError(
                "output-inside-source-frontier",
                "Report output must be outside the selected source folder",
                output=args.output.resolve().as_posix(),
            )
        report = build_report(source)
        rendered = canonical_json(report, pretty=True)
        if args.output is None:
            sys.stdout.write(rendered)
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8", newline="\n")
            sys.stdout.write(canonical_json({"schema": SCHEMA, "output": args.output.resolve().as_posix()}))
        return 0
    except ScopeSignatureError as error:
        sys.stderr.write(canonical_json({"schema": SCHEMA, "error": error.record(severity="error")}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
