"""Reuse Carrier splitting and PyYAML's safe parser without constructing tags."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import sys

import yaml
from yaml.events import AliasEvent, MappingStartEvent, SequenceStartEvent
from yaml.events import MappingEndEvent, SequenceEndEvent
from yaml.nodes import MappingNode

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from artifact_metadata import split_frontmatter  # type: ignore[import-not-found]


class CarrierError(ValueError):
    def __init__(self, code: str, reason: str) -> None:
        super().__init__(reason)
        self.code = code


class UniqueSafeLoader(yaml.SafeLoader):
    def construct_mapping(self, node: MappingNode, deep: bool = False) -> dict[Any, Any]:
        result: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            if key_node.tag == "tag:yaml.org,2002:merge":
                raise CarrierError("YAML_UNSUPPORTED", "YAML merge keys are unsupported.")
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                raise CarrierError("YAML_INVALID", "Frontmatter mapping keys must be strings.")
            if key in result:
                raise CarrierError("YAML_DUPLICATE_KEY", "Duplicate frontmatter mapping key.")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


@dataclass(frozen=True)
class ParsedCarrier:
    text: str
    frontmatter: str
    body: str
    metadata: dict[str, Any]


def check_yaml_resources(frontmatter: str) -> None:
    """Hard parser safety ceilings, not configurable assessment-budget defaults."""
    depth = 0
    for count, event in enumerate(yaml.parse(frontmatter, Loader=yaml.SafeLoader), 1):
        if isinstance(event, AliasEvent):
            raise CarrierError("YAML_UNSUPPORTED", "YAML aliases require an unsupported adapter.")
        if isinstance(event, (MappingStartEvent, SequenceStartEvent)):
            depth += 1
        if isinstance(event, (MappingEndEvent, SequenceEndEvent)):
            depth -= 1
        if depth > 64 or count > 100_000:
            raise CarrierError("YAML_UNSUPPORTED", "YAML exceeds the parser safety ceiling.")


def parse_carrier(raw: bytes, path: Path) -> ParsedCarrier:
    try:
        text = raw.decode("utf-8")
        delimiter, frontmatter, body = split_frontmatter(text.replace("\r\n", "\n"), path)
        if delimiter != "---":
            raise CarrierError("CARRIER_UNSUPPORTED", "Atom validation supports YAML frontmatter.")
        check_yaml_resources(frontmatter)
        metadata = yaml.load(frontmatter, Loader=UniqueSafeLoader)
        if not isinstance(metadata, dict):
            raise CarrierError("YAML_INVALID", "Frontmatter must contain one mapping.")
        return ParsedCarrier(text, frontmatter, body, metadata)
    except CarrierError:
        raise
    except (UnicodeError, yaml.YAMLError, RuntimeError, ValueError) as error:
        # Parser errors can include arbitrary input: do not expose their message.
        raise CarrierError(
            "CARRIER_INVALID", "Unreadable UTF-8 or malformed frontmatter."
        ) from error
