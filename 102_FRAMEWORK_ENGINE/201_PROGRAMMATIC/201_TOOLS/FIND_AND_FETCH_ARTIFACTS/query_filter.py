"""Closed, literal query-filter parser shared by read-only query tools.

The parser deliberately has no filesystem or journal dependencies. A caller
owns its selector namespace and can validate every selector before evaluating a
possibly short-circuited expression.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from typing import Any, Callable


class QueryFilterError(ValueError):
    """The request is outside the closed QUERY_FILTER contract."""

    def __init__(self, message: str, *, statistics: dict[str, int] | None = None):
        super().__init__(message)
        self.statistics = statistics


MISSING = object()
_JSON_WHITESPACE = " \t\r\n"


def _constant(value: str) -> None:
    raise QueryFilterError(f"invalid JSON constant: {value}")


def _no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise QueryFilterError("duplicate JSON object member")
        result[key] = value
    return result


_JSON_DECODER = json.JSONDecoder(
    parse_constant=_constant,
    object_pairs_hook=_no_duplicates,
)


def _is_json_number(value: Any) -> bool:
    return type(value) in (int, float)


def typed_equal(left: Any, right: Any) -> bool:
    """Compare JSON values deeply without Python bool/int coercion."""
    pending: list[tuple[Any, Any]] = [(left, right)]
    while pending:
        first, second = pending.pop()
        if _is_json_number(first) and _is_json_number(second):
            nonfinite = (
                isinstance(first, float)
                and not math.isfinite(first)
                or isinstance(second, float)
                and not math.isfinite(second)
            )
            if nonfinite or first != second:
                return False
            continue
        if type(first) is not type(second):
            return False
        if isinstance(first, list):
            if len(first) != len(second):
                return False
            pending.extend(zip(first, second))
        elif isinstance(first, dict):
            if first.keys() != second.keys():
                return False
            pending.extend((first[key], second[key]) for key in first)
        elif first != second:
            return False
    return True


def _check_literal_depth(
    text: str,
    start: int,
    max_depth: int,
    observe_depth: Callable[[int], None] | None = None,
) -> None:
    """Reject deeply nested containers before ``json`` can recurse on them."""
    if start >= len(text) or text[start] not in "[{":
        return
    stack: list[str] = []
    in_string = False
    escaped = False
    for char in text[start:]:
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char in "[{":
            stack.append(char)
            if observe_depth is not None:
                observe_depth(len(stack))
            if len(stack) > max_depth:
                raise QueryFilterError("JSON literal depth exceeded")
        elif char in "]}":
            if not stack:
                return
            opener = stack.pop()
            if (opener, char) not in (("[", "]"), ("{", "}")):
                return
            if not stack:
                return


def _validate_json_value(value: Any) -> None:
    pending = [value]
    while pending:
        item = pending.pop()
        if isinstance(item, float) and not math.isfinite(item):
            raise QueryFilterError("non-finite JSON number")
        if isinstance(item, list):
            pending.extend(item)
        elif isinstance(item, dict):
            pending.extend(item.values())


def _json_value(
    text: str,
    start: int,
    max_depth: int,
    observe_depth: Callable[[int], None] | None = None,
) -> tuple[Any, int]:
    _check_literal_depth(text, start, max_depth, observe_depth)
    try:
        value, end = _JSON_DECODER.raw_decode(text, start)
    except QueryFilterError:
        raise
    except (json.JSONDecodeError, ValueError, RecursionError) as error:
        raise QueryFilterError("expected RFC 8259 JSON literal") from error
    _validate_json_value(value)
    return value, end


def _positive_limit(value: Any, name: str) -> int:
    if type(value) is not int or value <= 0:
        raise QueryFilterError(f"{name} must be a positive integer")
    return value


@dataclass
class _Parser:
    text: str
    max_depth: int
    max_tokens: int
    max_in: int
    tokens: int = 0
    pos: int = 0
    last_json_end: int | None = None
    max_syntactic_depth: int = 0
    max_literal_depth: int = 0
    max_observed_in_members: int = 0

    def ws(self) -> None:
        while self.pos < len(self.text) and self.text[self.pos] in _JSON_WHITESPACE:
            self.pos += 1

    def _count(self) -> None:
        self.tokens += 1
        if self.tokens > self.max_tokens:
            raise QueryFilterError("filter token budget exceeded")

    def punctuation(self, value: str) -> bool:
        self.ws()
        if self.text.startswith(value, self.pos):
            self.pos += len(value)
            self._count()
            return True
        return False

    def word(self, value: str) -> bool:
        self.ws()
        if self.pos == self.last_json_end and self.text.startswith(value, self.pos):
            raise QueryFilterError("expected separator after JSON value")
        if not self.text.startswith(value, self.pos):
            return False
        end = self.pos + len(value)
        if end < len(self.text) and (self.text[end].isalnum() or self.text[end] == "_"):
            return False
        if end < len(self.text) and self.text[end] == '"':
            raise QueryFilterError("expected separator before JSON string")
        self.pos = end
        self._count()
        return True

    def required_punctuation(self, value: str) -> None:
        if not self.punctuation(value):
            raise QueryFilterError(f"expected {value}")

    def _enter_depth(self, depth: int) -> int:
        consumed = depth + 1
        self.max_syntactic_depth = max(self.max_syntactic_depth, consumed)
        if consumed > self.max_depth:
            raise QueryFilterError("filter grammar depth exceeded")
        return consumed

    def _observe_literal_depth(self, depth: int) -> None:
        self.max_literal_depth = max(self.max_literal_depth, depth)

    def json_literal(self) -> tuple[Any, int]:
        self.ws()
        value, end = _json_value(
            self.text,
            self.pos,
            self.max_depth,
            self._observe_literal_depth,
        )
        self.pos = end
        self.last_json_end = end
        self._count()
        return value, end

    def expression(self, depth: int = 0):
        node = self.and_(depth)
        while self.word("OR"):
            node = ("or", node, self.and_(depth))
        return node

    def and_(self, depth: int):
        node = self.unary(depth)
        while self.word("AND"):
            node = ("and", node, self.unary(depth))
        return node

    def unary(self, depth: int):
        if self.word("NOT"):
            return ("not", self.unary(self._enter_depth(depth)))
        if self.punctuation("("):
            node = self.expression(self._enter_depth(depth))
            self.required_punctuation(")")
            return node
        return self.comparison()

    def comparison(self):
        selector, selector_end = self.json_literal()
        if not isinstance(selector, str):
            raise QueryFilterError("selector must be a JSON string")
        self.ws()
        if self.pos == selector_end:
            raise QueryFilterError("expected separator after JSON string selector")
        if self.word("IN"):
            self.required_punctuation("(")
            values = []
            while True:
                value, _ = self.json_literal()
                values.append(value)
                self.max_observed_in_members = max(self.max_observed_in_members, len(values))
                if len(values) > self.max_in:
                    raise QueryFilterError("IN member budget exceeded")
                if not self.punctuation(","):
                    break
            self.required_punctuation(")")
            return ("in", selector, values)
        if self.punctuation("!="):
            kind = "ne"
        elif self.punctuation("="):
            kind = "eq"
        else:
            raise QueryFilterError("expected comparison operator")
        value, _ = self.json_literal()
        return (kind, selector, value)


def _parser_statistics(parser: _Parser) -> dict[str, int]:
    """Return only counters observed by this parser instance."""
    return {
        "tokens": parser.tokens,
        "grammar_depth": max(parser.max_syntactic_depth, parser.max_literal_depth),
        "syntactic_depth": parser.max_syntactic_depth,
        "literal_depth": parser.max_literal_depth,
        "in_members": parser.max_observed_in_members,
    }


def parse_filter_with_stats(
    expression: str,
    *,
    max_depth: int = 32,
    max_tokens: int = 1024,
    max_in_members: int = 256,
) -> tuple[Any, dict[str, int]]:
    """Parse once and return its AST plus actual parser-consumption counters."""
    if not isinstance(expression, str):
        raise QueryFilterError("expression must be a string")
    parser = _Parser(
        expression,
        _positive_limit(max_depth, "max_depth"),
        _positive_limit(max_tokens, "max_tokens"),
        _positive_limit(max_in_members, "max_in_members"),
    )
    try:
        tree = parser.expression()
        parser.ws()
        if parser.pos != len(expression):
            raise QueryFilterError("unexpected filter syntax")
    except QueryFilterError as error:
        error.statistics = _parser_statistics(parser)
        raise
    return tree, _parser_statistics(parser)


def parse_filter(
    expression: str,
    *,
    max_depth: int = 32,
    max_tokens: int = 1024,
    max_in_members: int = 256,
):
    """Parse one bounded closed filter expression without changing its AST API."""
    tree, _ = parse_filter_with_stats(
        expression,
        max_depth=max_depth,
        max_tokens=max_tokens,
        max_in_members=max_in_members,
    )
    return tree


def _node_parts(node: Any) -> tuple[str, tuple[Any, ...]]:
    if not isinstance(node, tuple) or not node or not isinstance(node[0], str):
        raise QueryFilterError("malformed filter tree")
    return node[0], node[1:]


def collect_selectors(tree: Any) -> tuple[str, ...]:
    """Return unique selectors in source order while validating the whole AST."""
    selectors: list[str] = []
    seen: set[str] = set()
    pending = [tree]
    while pending:
        kind, parts = _node_parts(pending.pop())
        if kind == "not":
            if len(parts) != 1:
                raise QueryFilterError("malformed NOT filter")
            pending.append(parts[0])
        elif kind in {"and", "or"}:
            if len(parts) != 2:
                raise QueryFilterError(f"malformed {kind.upper()} filter")
            pending.append(parts[1])
            pending.append(parts[0])
        elif kind in {"eq", "ne", "in"}:
            if len(parts) != 2 or not isinstance(parts[0], str):
                raise QueryFilterError("malformed comparison filter")
            if kind == "in" and not isinstance(parts[1], (list, tuple)):
                raise QueryFilterError("malformed IN filter")
            if parts[0] not in seen:
                seen.add(parts[0])
                selectors.append(parts[0])
        else:
            raise QueryFilterError("unknown filter node")
    return tuple(selectors)


def evaluate_filter(tree: Any, resolve: Callable[[str], Any]) -> bool:
    """Evaluate a parsed tree iteratively while preserving short-circuiting."""
    pending: list[tuple[str, Any]] = [("node", tree)]
    values: list[bool] = []
    while pending:
        action, payload = pending.pop()
        if action == "node":
            kind, parts = _node_parts(payload)
            if kind == "not":
                if len(parts) != 1:
                    raise QueryFilterError("malformed NOT filter")
                pending.extend((("not", None), ("node", parts[0])))
            elif kind in {"and", "or"}:
                if len(parts) != 2:
                    raise QueryFilterError(f"malformed {kind.upper()} filter")
                pending.extend(((kind, parts[1]), ("node", parts[0])))
            elif kind in {"eq", "ne", "in"}:
                if len(parts) != 2 or not isinstance(parts[0], str):
                    raise QueryFilterError("malformed comparison filter")
                value = resolve(parts[0])
                if value is MISSING:
                    values.append(False)
                elif kind == "eq":
                    values.append(typed_equal(value, parts[1]))
                elif kind == "ne":
                    values.append(not typed_equal(value, parts[1]))
                else:
                    if not isinstance(parts[1], (list, tuple)):
                        raise QueryFilterError("malformed IN filter")
                    values.append(any(typed_equal(value, candidate) for candidate in parts[1]))
            else:
                raise QueryFilterError("unknown filter node")
        elif action == "not":
            values.append(not values.pop())
        elif action == "and":
            left = values.pop()
            if not left:
                values.append(False)
            else:
                pending.append(("node", payload))
        elif action == "or":
            left = values.pop()
            if left:
                values.append(True)
            else:
                pending.append(("node", payload))
        else:
            raise QueryFilterError("malformed filter evaluation")
    if len(values) != 1:
        raise QueryFilterError("malformed filter evaluation")
    return values[0]


def decode_json_pointer(pointer: str) -> tuple[str, ...]:
    """Decode RFC 6901 tokens and reject malformed escapes."""
    if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
        raise QueryFilterError("invalid JSON Pointer")
    tokens: list[str] = []
    for raw in (() if pointer == "" else pointer[1:].split("/")):
        decoded: list[str] = []
        index = 0
        while index < len(raw):
            char = raw[index]
            if char != "~":
                decoded.append(char)
                index += 1
            elif index + 1 >= len(raw) or raw[index + 1] not in "01":
                raise QueryFilterError("invalid JSON Pointer escape")
            else:
                decoded.append("~" if raw[index + 1] == "0" else "/")
                index += 2
        tokens.append("".join(decoded))
    return tuple(tokens)


def resolve_json_pointer(value: Any, pointer: str) -> Any:
    """Resolve a valid RFC 6901 pointer; absent members return ``MISSING``."""
    for token in decode_json_pointer(pointer):
        if isinstance(value, dict):
            if token not in value:
                return MISSING
            value = value[token]
        elif isinstance(value, list):
            valid_index = token == "0" or (
                token
                and token[0] != "0"
                and token.isascii()
                and token.isdecimal()
            )
            if not valid_index:
                return MISSING
            maximum = len(value) - 1
            if len(token) > len(str(maximum)):
                return MISSING
            index = int(token)
            if index >= len(value):
                return MISSING
            value = value[index]
        else:
            return MISSING
    return value


__all__ = [
    "MISSING",
    "QueryFilterError",
    "collect_selectors",
    "decode_json_pointer",
    "evaluate_filter",
    "parse_filter",
    "parse_filter_with_stats",
    "resolve_json_pointer",
    "typed_equal",
]
