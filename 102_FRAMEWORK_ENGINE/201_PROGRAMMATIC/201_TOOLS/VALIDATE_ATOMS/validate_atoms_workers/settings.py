"""Settings are inputs; there are no competing numeric defaults in this Tool."""

import hashlib
from pathlib import Path
import tomllib
from typing import Any

from .read_io import ReadContext

# Host safety ceilings for bootstrap reads and impossible requests, not defaults.
CEILINGS = dict(
    max_candidates=1_000_000,
    max_file_bytes=64 * 1024 * 1024,
    max_total_read_bytes=1024 * 1024 * 1024,
    timeout_seconds=300,
    max_findings=100_000,
)


def bound_file(reader: ReadContext, binding: dict[str, Any]) -> bytes:
    raw = reader.read(Path(binding["path"]))
    if binding.get("sha256", hashlib.sha256(raw).hexdigest()) != hashlib.sha256(raw).hexdigest():
        raise ValueError("Stale file binding.")
    return raw


def load_limit_layers(request: dict[str, Any], reader: ReadContext) -> dict[str, dict[str, int]]:
    layers: dict[str, dict[str, int]] = {"request": request.get("limits", {})}
    for source, key in [("instance", "framework_settings"), ("default", "default_settings")]:
        if key in request:
            data = tomllib.loads(bound_file(reader, request[key]).decode("utf-8"))
            layers[source] = data.get("atom_validation", {})
    for layer in layers.values():
        if not isinstance(layer, dict) or set(layer) - CEILINGS.keys():
            raise ValueError("Invalid atom_validation settings.")
        if any(type(v) is not int or v < 1 for v in layer.values()):
            raise ValueError("Invalid atom_validation settings value.")
    return layers


def resolve_limits(
    request: dict[str, Any], reader: ReadContext
) -> tuple[dict[str, int], dict[str, str]]:
    layers = load_limit_layers(request, reader)
    effective, provenance = {}, {}
    for key, ceiling in CEILINGS.items():
        for name in ("request", "instance", "default"):
            if key in layers.get(name, {}):
                effective[key], provenance[key] = layers[name][key], name
                break
        if key not in effective or effective[key] > ceiling:
            raise ValueError("Missing default or requested bound exceeds the host ceiling.")
    reader.limits = effective
    if any(size > effective["max_file_bytes"] for size in reader.sizes.values()):
        raise ValueError("A settings file exceeds the resolved file-read budget.")
    reader.check_size(0)
    reader.checkpoint()
    return effective, provenance
