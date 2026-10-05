"""Resolve the Docker image identity without permitting mutable overrides."""

import re


IMAGE = "caprmedio-runtime:local"
IMMUTABLE_IMAGE = re.compile(r"sha256:[0-9a-f]{64}")


def image_reference(environment):
    """Return the development fallback or one explicit immutable image ID."""
    value = environment.get("CAPRMEDIO_IMAGE")
    if value is None or value == "":
        return IMAGE
    if not isinstance(value, str) or not IMMUTABLE_IMAGE.fullmatch(value):
        raise ValueError("CAPRMEDIO_IMAGE must be an immutable sha256 image ID")
    return value
