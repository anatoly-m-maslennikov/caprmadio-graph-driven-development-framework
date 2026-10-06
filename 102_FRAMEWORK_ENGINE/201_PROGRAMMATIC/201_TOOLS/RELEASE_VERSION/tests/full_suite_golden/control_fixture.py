"""Retained, source-pinned controls for the disposable Unit driver Project.

The canonical live selector may lag an accepted Release graph.  This fixture
copies actual current or archived carriers by digest and constructs its private
selector from those copied sources; it never repairs the live selector.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil

from release_suite_reference_context import _project_structure_ref, _prompt_binding_rows
from release_source_admission import (
    AUTHORITY_PIN,
    derive_release_graph_admission,
    derive_release_private_carriers,
    derive_release_source_admission,
)
from selected_routes import PROJECT_SETTINGS_REF, canonical_digest, canonical_json, selected_manifest_ref


_UNIT_DEADLINE_SETTINGS = (
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/"
    "caprmedio_framework_default_settings.toml",
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/"
    "caprmedio_framework_settings.toml",
)


def _pins(value: object) -> dict[str, str]:
    result: dict[str, str] = {}
    if isinstance(value, dict):
        path, digest = value.get("source_path"), value.get("digest")
        if isinstance(path, str) and isinstance(digest, str):
            result[path] = digest
        children = value.values()
    elif isinstance(value, list):
        children = value
    else:
        return result
    for child in children:
        for path, digest in _pins(child).items():
            prior = result.setdefault(path, digest)
            if prior != digest:
                raise RuntimeError(f"golden control pin disagrees for {path}")
    return result


def _retained_source(repository: Path, relative: str, digest: str | None) -> Path:
    source = repository / relative
    if source.is_file() and not source.is_symlink():
        if digest is None or hashlib.sha256(source.read_bytes()).hexdigest() == digest:
            return source
    archive = source.parent / "archive"
    if archive.is_dir() and not archive.is_symlink():
        for carrier in sorted(archive.rglob("*.md")):
            if carrier.is_file() and not carrier.is_symlink():
                if hashlib.sha256(carrier.read_bytes()).hexdigest() == digest:
                    return carrier
    raise RuntimeError(f"golden control has no retained byte carrier: {relative}")


def copy_control_closure(repository: Path, root: Path) -> None:
    """Build a synthetic selector while retaining real source-admission guards."""

    manifest_ref = selected_manifest_ref(repository)
    manifest = json.loads((repository / manifest_ref).read_bytes())
    # Replace only the private fixture's Release route.  An obsolete live
    # Release graph must not select retired bytes for the new admission.
    manifest["routes"] = [route for route in manifest["routes"] if route["route"] != "release_version"]
    manifest.pop("release_source_admissions", None)
    admission = derive_release_source_admission(repository)
    pins = _pins(manifest)
    for path, digest in _pins(admission).items():
        prior = pins.setdefault(path, digest)
        if prior != digest:
            raise RuntimeError(f"golden control pin disagrees for {path}")
    pins[AUTHORITY_PIN["source_path"]] = AUTHORITY_PIN["digest"]
    freshness = manifest["source_freshness"]
    pins[freshness["selected_source_registry_ref"]] = freshness["selected_source_registry_digest"]
    settings_relative = PROJECT_SETTINGS_REF.as_posix()
    settings_source = _retained_source(repository, settings_relative, pins.get(settings_relative))
    project_structure_relative = _project_structure_ref(settings_source.read_bytes())
    required = set(pins) | {
        ".caprmedio_caprmedio/operators_registry.toml",
        settings_relative,
        project_structure_relative,
        *_UNIT_DEADLINE_SETTINGS,
    }
    for relative in sorted(required):
        source = _retained_source(repository, relative, pins.get(relative))
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        target.chmod(source.stat().st_mode & 0o777)

    # D580 declares a closed Prompt binding frontier.  Copy only its two
    # binding carriers and their exact pinned active Atom files; no directory
    # discovery or legacy Plan material is admitted into the retained fixture.
    d580_relative = next(path for path in pins if "/CA-D-580-" in path)
    for binding_relative, binding_digest in _prompt_binding_rows((root / d580_relative).read_bytes()):
        binding_source = _retained_source(repository, binding_relative, binding_digest)
        binding_target = root / binding_relative
        binding_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(binding_source, binding_target)
        binding_target.chmod(binding_source.stat().st_mode & 0o777)
        binding = json.loads(binding_target.read_bytes())
        for pin in binding["sources"]:
            atom_source = _retained_source(repository, pin["path"], pin["sha256"])
            atom_target = root / pin["path"]
            atom_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(atom_source, atom_target)
            atom_target.chmod(atom_source.stat().st_mode & 0o777)

    # Implementation carriers have D572 byte declarations, not Atom pins.
    # Preserve their actual modes and independently check the copied bytes.
    for row in derive_release_private_carriers(repository):
        source = repository / row["source_path"]
        target = root / row["source_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        target.chmod(source.stat().st_mode & 0o777)
        if hashlib.sha256(target.read_bytes()).hexdigest() != row["sha256"]:
            raise RuntimeError(f"golden private carrier changed: {row['source_path']}")

    route, copied_admission = derive_release_graph_admission(root)
    manifest["routes"].append(route)
    manifest["release_source_admissions"] = [copied_admission]
    freshness["selected_binding_digest"] = canonical_digest(manifest["routes"])
    manifest["canonical_manifest_sha256"] = canonical_digest({
        key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"
    })
    target = root / manifest_ref
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(canonical_json(manifest), encoding="utf-8", newline="\n")
    target.chmod((repository / manifest_ref).stat().st_mode & 0o777)
