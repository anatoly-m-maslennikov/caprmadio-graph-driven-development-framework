#!/usr/bin/env python3
"""Derive report-only canonical signatures for a restricted CCE Boolean subset."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


TOOL_ID = "DERIVE_CCE_CANONICAL_SIGNATURES"
SCHEMA = "caprmedio.derive_cce_canonical_signatures.v1"
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
EXCLUDED_OPERATOR_PATTERN = re.compile(r"\*\*([^*\n]+?)\*\*")
SUBJECT_PATH_PATTERN = r"[A-Z][A-Za-z0-9_]*(?:/[A-Z][A-Za-z0-9_ ]*)*"
VALUE_PATTERN = r"[A-Z][A-Za-z0-9_ -]*"
ATOMIC_PREDICATE_PATTERN = re.compile(rf"{SUBJECT_PATH_PATTERN}: {VALUE_PATTERN}")


class SignatureError(RuntimeError):
    """A stable input or restricted-grammar failure."""

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
    statement: str

    def evidence(self) -> dict[str, object]:
        return {
            "atom_id": self.atom_id,
            "atom_revision": self.version,
            "carrier_path": self.carrier_path,
            "carrier_sha256": self.sha256,
        }


@dataclass(frozen=True)
class Signature:
    """A structural, non-authoritative comparison value.

    Keeping one member in a group preserves the authored root operator after
    duplicate elimination.  The signature therefore does not silently equate
    an atomic predicate with a degenerate conjunction or disjunction.
    """

    operator: str
    atomic_predicates: tuple[str, ...]

    def record(self) -> dict[str, object]:
        return {"operator": self.operator, "atomic_predicates": list(self.atomic_predicates)}

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
        raise SignatureError("frontmatter-unterminated", "Markdown frontmatter is unterminated", path=path)
    try:
        return data[4:boundary].decode("utf-8"), data[boundary + 5 :].decode("utf-8")
    except UnicodeDecodeError as error:
        raise SignatureError("carrier-not-utf8", "Markdown Carrier must be UTF-8", path=path) from error


def top_scalar(frontmatter: str, key: str, path: str) -> str | None:
    matches = re.findall(rf"(?m)^{re.escape(key)}:\s*([^\n]+?)\s*$", frontmatter)
    if len(matches) > 1:
        raise SignatureError("frontmatter-duplicate-key", "Atom Carrier has a duplicate scalar", path=path, key=key)
    return scalar_value(matches[0]) if matches else None


def display_path(path: Path, selected_folder: Path) -> str:
    return path.relative_to(selected_folder).as_posix()


def is_inactive(path: Path, selected_folder: Path) -> bool:
    return any(part.lower() in INACTIVE_DIRECTORY_NAMES for part in path.relative_to(selected_folder).parts[:-1])


def single_statement(body: str) -> str | None:
    """Return one direct statement, refusing Markdown structure and prose blocks."""

    lines = [line.strip() for line in body.splitlines() if line.strip()]
    if not lines or not lines[0].startswith("# "):
        return None
    statement_lines = lines[1:]
    if len(statement_lines) != 1:
        return None
    statement = statement_lines[0]
    if statement.startswith(("#", "-", "*", "1. ", "```")):
        return None
    return statement


def parenthetical_groups(statement: str) -> list[tuple[int, int]]:
    """Return outermost balanced parenthetical groups, without parsing prose."""

    starts: list[int] = []
    groups: list[tuple[int, int]] = []
    for index, character in enumerate(statement):
        if character == "(":
            starts.append(index)
        elif character == ")":
            if not starts:
                raise SignatureError("parenthesis-unbalanced", "Statement has an unmatched closing parenthesis")
            start = starts.pop()
            if not starts:
                groups.append((start, index + 1))
    if starts:
        raise SignatureError("parenthesis-unbalanced", "Statement has an unmatched opening parenthesis")
    return groups


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
    for match in EXCLUDED_OPERATOR_PATTERN.finditer(text):
        token = match.group(1).strip()
        if token not in RESTRICTED_OPERATORS:
            raise SignatureError(
                "operator-excluded",
                "Restricted canonical-signature grammar excludes this CCE Operator",
                operator=token,
            )


def split_top_level_operands(body: str) -> tuple[str, list[str]]:
    """Split one pure Boolean group and reject mixed or malformed operators."""

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
                raise SignatureError("parenthesis-unbalanced", "Boolean group has an unmatched closing parenthesis")
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
        raise SignatureError("parenthesis-unbalanced", "Boolean group has an unmatched opening parenthesis")
    if not separators:
        raise SignatureError("boolean-operator-missing", "Restricted Boolean group has no canonical Boolean Operator")
    operators = {operator for _, _, operator in separators}
    if len(operators) != 1:
        raise SignatureError("mixed-operator", "Restricted Boolean group mixes **and** and **or**")
    operator = next(iter(operators))
    operands: list[str] = []
    start = 0
    for token_start, token_end, _ in separators:
        operand = body[start:token_start].strip()
        if not operand:
            raise SignatureError("operand-empty", "Restricted Boolean group has an empty operand")
        operands.append(operand)
        start = token_end
    final_operand = body[start:].strip()
    if not final_operand:
        raise SignatureError("operand-empty", "Restricted Boolean group has an empty operand")
    operands.append(final_operand)
    return operator, operands


def parse_atomic_predicate(text: str) -> str:
    atom = text.strip()
    if not ATOMIC_PREDICATE_PATTERN.fullmatch(atom):
        raise SignatureError(
            "atomic-predicate-invalid",
            "Restricted Boolean grammar accepts only canonical `Subject Path: Value` Atomic Predicates",
            value=atom,
        )
    return atom


def parse_restricted_boolean_group(expression: str) -> Signature:
    """Parse, flatten, deduplicate, and order one pure **and** or **or** group."""

    text = expression.strip()
    if not has_outer_parentheses(text):
        raise SignatureError("group-parentheses-required", "Restricted Boolean group requires one enclosing parenthesis pair")
    body = text[1:-1]
    operator, operands = split_top_level_operands(body)
    atomic_predicates: list[str] = []
    for operand in operands:
        if has_outer_parentheses(operand):
            nested = parse_restricted_boolean_group(operand)
            if nested.operator != operator:
                raise SignatureError(
                    "mixed-operator",
                    "Restricted Boolean group has a nested group with a different Boolean Operator",
                    outer_operator=operator,
                    nested_operator=nested.operator,
                )
            atomic_predicates.extend(nested.atomic_predicates)
        else:
            atomic_predicates.append(parse_atomic_predicate(operand))
    return Signature(operator=operator, atomic_predicates=tuple(sorted(set(atomic_predicates))))


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
        statement = single_statement(body)
        if statement is None:
            counts["noncanonical_claim_shape_skipped"] += 1
            continue
        atom_id = top_scalar(frontmatter, "atom_id", relative_path) or path.stem.split("--", 1)[0]
        raw_version = top_scalar(frontmatter, "version", relative_path)
        if not atom_id:
            raise SignatureError("atom-id-missing", "Atom Carrier has no identity", path=relative_path)
        if raw_version is None or not re.fullmatch(r"[1-9][0-9]*", raw_version):
            raise SignatureError(
                "atom-version-invalid",
                "Atom Carrier requires a positive integer version",
                path=relative_path,
                value=raw_version,
            )
        carriers.append(
            Carrier(
                atom_id=atom_id,
                version=int(raw_version),
                carrier_path=relative_path,
                sha256=sha256(data),
                statement=statement,
            )
        )
    return carriers, dict(sorted(counts.items())), diagnostics


def source_frontier_digest(selected_folder: Path) -> tuple[str, int]:
    """Digest all active Atom bytes, including statements outside the subset."""

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
    """Return signatures and exclusions without creating or editing an Atom Carrier."""

    source = selected_folder.resolve()
    if not source.is_dir():
        raise SignatureError("source-folder-missing", "Source folder is not a directory", path=source.as_posix())

    carriers, skipped, diagnostics = discover_active_carriers(source)
    counts: defaultdict[str, int] = defaultdict(int, skipped)
    occurrences: list[dict[str, object]] = []
    for carrier in carriers:
        try:
            groups = parenthetical_groups(carrier.statement)
        except SignatureError as error:
            counts["unparseable_statements_skipped"] += 1
            diagnostics.append(
                {
                    **error.record(),
                    "details": {**error.details, **carrier.evidence()},
                }
            )
            continue
        if not groups:
            counts["no_boolean_group_skipped"] += 1
            continue
        for start, end in groups:
            expression = carrier.statement[start:end]
            if "**and**" not in expression and "**or**" not in expression:
                counts["nonboolean_parenthetical_group_skipped"] += 1
                continue
            try:
                signature = parse_restricted_boolean_group(expression)
            except SignatureError as error:
                counts["restricted_boundary_exclusions"] += 1
                diagnostics.append(
                    {
                        **error.record(),
                        "details": {
                            **error.details,
                            **carrier.evidence(),
                            "statement_offset": {"start": start, "end": end},
                            "source_expression": expression,
                        },
                    }
                )
                continue
            occurrences.append(
                {
                    **carrier.evidence(),
                    "statement_offset": {"start": start, "end": end},
                    "source_expression": expression,
                    "canonical_signature": signature.record(),
                    "canonical_signature_sha256": signature.digest(),
                }
            )
            counts["canonical_signatures"] += 1

    by_signature: defaultdict[str, list[str]] = defaultdict(list)
    for occurrence in occurrences:
        by_signature[str(occurrence["canonical_signature_sha256"])].append(str(occurrence["atom_id"]))
    duplicate_signature_groups = [
        {"canonical_signature_sha256": digest, "atom_ids": sorted(atom_ids)}
        for digest, atom_ids in sorted(by_signature.items())
        if len(atom_ids) > 1
    ]
    counts["active_atom_carriers"] = source_frontier_digest(source)[1]
    counts["eligible_single_statement_carriers"] = len(carriers)
    counts["duplicate_signature_groups"] = len(duplicate_signature_groups)
    return {
        "schema": SCHEMA,
        "tool_id": TOOL_ID,
        "mode": "report_only",
        "source_folder": source.as_posix(),
        "source_frontier": {
            "active_atom_carrier_count": counts["active_atom_carriers"],
            "sha256": source_frontier_digest(source)[0],
        },
        "restricted_grammar": {
            "group": "(operand **and** operand [**and** operand ...]) | (operand **or** operand [**or** operand ...])",
            "operand": "atomic predicate | nested group with the same Boolean Operator",
            "atomic_predicate": "Subject Path: Value",
            "signature": {"operator": "and | or", "atomic_predicates": "sorted unique non-empty list"},
            "exclusions": [
                "mixed **and** and **or** groups",
                "all CCE Operators other than **and** and **or**",
                "unrecognized bold tokens",
                "unbalanced parentheses",
                "unparseable prose and noncanonical Atomic Predicates",
            ],
        },
        "signatures": occurrences,
        "duplicate_signature_groups": duplicate_signature_groups,
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
    parser.add_argument("--source-folder", required=True, type=Path, help="Folder containing Atom Carriers to inspect")
    parser.add_argument("--output", type=Path, help="Optional JSON report path outside the selected source folder")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    try:
        args = parse_args(argv)
        source = args.source_folder.resolve()
        if args.output is not None and output_is_inside_source(source, args.output):
            raise SignatureError(
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
    except SignatureError as error:
        sys.stderr.write(canonical_json({"schema": SCHEMA, "error": error.record(severity="error")}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
