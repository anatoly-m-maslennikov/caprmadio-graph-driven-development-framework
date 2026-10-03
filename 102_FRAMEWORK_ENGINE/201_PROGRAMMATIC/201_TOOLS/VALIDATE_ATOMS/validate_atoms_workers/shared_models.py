"""Shared strict scalar, object, and binding models from CA-D-492@3."""

from __future__ import annotations

import json
import os.path
from typing import Annotated, Any, Literal, TypeVar

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, field_validator


def _absolute_path(value: str) -> str:
    if not os.path.isabs(value) or "\x00" in value:
        raise ValueError("expected an absolute local path")
    return os.path.normpath(value)


def _ordered_set[T](values: list[T]) -> list[T]:
    encoded = [
        json.dumps(
            v.model_dump(exclude_unset=True) if isinstance(v, BaseModel) else v,
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
        )
        for v in values
    ]
    if len(set(encoded)) != len(encoded):
        raise ValueError("duplicate set member")
    return sorted(values, key=_set_sort_key)


def _set_sort_key(value: Any) -> tuple[Any, ...]:
    if isinstance(value, AtomBinding):
        return (value.atom_id, value.version, value.path, value.sha256)
    if isinstance(value, FileBinding):
        return (value.path, value.sha256 or "")
    if isinstance(value, BaseModel):
        return (json.dumps(value.model_dump(exclude_unset=True), sort_keys=True),)
    return (value,)


T = TypeVar("T")
String = Annotated[str, Field(min_length=1)]
Path = Annotated[String, AfterValidator(_absolute_path)]
Digest = Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
Positive = Annotated[int, Field(strict=True, ge=1)]
Nonnegative = Annotated[int, Field(strict=True, ge=0)]
SchemaVersion = Annotated[int, Field(strict=True, ge=1, le=1)]
SetList = Annotated[list[T], AfterValidator(_ordered_set)]
NonemptySet = Annotated[SetList[T], Field(min_length=1)]
LimitName = Literal[
    "max_candidates", "max_file_bytes", "max_total_read_bytes", "timeout_seconds", "max_findings"
]


class ClosedModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)


class RequestObject(ClosedModel):
    @field_validator("*", mode="before")
    @classmethod
    def reject_supplied_null(cls, value: Any) -> Any:
        if value is None:
            raise ValueError("null is not admitted")
        return value


class FileBinding(RequestObject):
    path: Path
    sha256: Digest | None = None


class AtomBinding(RequestObject):
    atom_id: String
    version: Positive
    sha256: Digest
    path: Path
