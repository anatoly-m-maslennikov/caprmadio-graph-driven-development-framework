"""Author membership in the Project's authoritative Operator registry."""

from typing import Self
import tomllib

from pydantic import Field, field_validator, model_validator

from .authority import Record
from .check_support import Check, _string
from .read_io import ReadContext
from .settings import bound_file
from .shared_models import RequestObject, String
from .support_authority import require_sources


class Operator(RequestObject):
    name: String
    role: String

    @field_validator("name", "role")
    @classmethod
    def nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Operator name and role must not be blank.")
        return value  # Membership is exact; never normalize a registered name.


class OperatorRegistry(RequestObject):
    operators: list[Operator] = Field(min_length=1)

    @model_validator(mode="after")
    def unique_names(self) -> Self:
        names = [entry.name for entry in self.operators]
        if len(names) != len(set(names)):
            raise ValueError("Operator names must be unique.")
        return self


def load_operators_registry(request: Record, reader: ReadContext) -> Record:
    """Load once per assessment through the existing bounded, fingerprinted reader."""
    if "operators_registry" not in request:
        return dict(names=None, error="Author membership needs a selected Operator registry.")
    try:
        raw = bound_file(reader, request["operators_registry"])
        registry = OperatorRegistry.model_validate(tomllib.loads(raw.decode("utf-8")))
    except OSError, ValueError:
        return dict(
            names=None,
            error="Operator registry is unavailable, stale, malformed, or has ambiguous entries.",
        )
    return dict(names=frozenset(entry.name for entry in registry.operators), error=None)


def author_membership(metadata: Record, body: str, check: Check) -> None:
    del body
    check.require(metadata, "author", _string)
    if check.findings or not require_sources(check, ("CA-D-494",)):
        return
    registry = check.inputs.get("operators_registry", {})
    names = registry.get("names")
    if names is None:
        check.gap(
            "author",
            registry.get("error") or "Author membership needs the selected Operator registry.",
        )
    elif metadata["author"] not in names:
        check.fail(
            "AUTHOR_UNREGISTERED",
            "author",
            "Author is not an exact registered Operator name in the selected Operator registry.",
        )
