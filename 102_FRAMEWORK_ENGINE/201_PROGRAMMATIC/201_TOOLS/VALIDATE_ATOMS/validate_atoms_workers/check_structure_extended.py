"""Conservative, byte-bound resolution of carried structural Atom properties.

These adapters never discover authority, read settings implicitly, or repair a
carrier. Incomplete Operator, Project identity, or address-encoding context is
an explicit gap; a path is never used to supply a missing carried value.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

from .authority import Record
from .check_sections import _headings
from .check_support import Check, _integer, _string


def _inputs(check: Check) -> Record:
    return getattr(check, "inputs", {})


@lru_cache(maxsize=1)
def _pins() -> Record:
    base = Path(__file__).parent
    result = {}
    for name in ("registry.json", "structure_authority.json", "schema_authority.json"):
        result.update(json.loads((base / name).read_text())["sources"])
    return result


def _authority(check: Check, *identifiers: str) -> bool:
    """Require exact source bytes, including dependency authority, before use."""
    registry = _pins()
    sources = _inputs(check).get("sources", [])
    good = True
    for identifier in identifiers:
        matches = [s for s in sources if s.get("binding", {}).get("atom_id") == identifier]
        pin = registry.get(identifier)
        verified = len(matches) == 1 and pin is not None
        if verified:
            assert pin is not None
            source, binding = matches[0], matches[0]["binding"]
            verified = (
                type(binding.get("version")) is int
                and binding.get("version") == pin["version"]
                and binding.get("sha256") == pin["sha256"]
                and isinstance(source.get("text"), str)
                and hashlib.sha256(source["text"].encode()).hexdigest() == pin["sha256"]
            )
        if not verified:
            check.gap(
                "authority",
                "Required exact structural authority is missing, changed, or ambiguous: "
                + identifier
                + ".",
            )
            good = False
        elif binding not in check.obligation.authority:
            check.obligation = replace(
                check.obligation, authority=[*check.obligation.authority, binding]
            )
    return good


def _value(metadata: Record, field: str, check: Check) -> str | None:
    check.require(metadata, field, _string)
    return metadata.get(field) if _string(metadata.get(field)) else None


def _validate_structure_row(row: Record) -> None:
    required = {
        "scope_unit_name",
        "parent",
        "scope_unit_type",
        "scope_unit_label",
        "structural_level",
        "navigational_order_number",
        "authority_path",
        "delivery_path",
    }
    optional = {"local_order", "authority_mode"}
    if not isinstance(row, dict) or not required <= row.keys() or row.keys() - required - optional:
        raise ValueError
    if any(
        not _string(row[k]) for k in required - {"structural_level", "navigational_order_number"}
    ):
        raise ValueError
    if row["scope_unit_name"] == "PROJECT" or row["scope_unit_type"] not in (
        "Ordered",
        "Unordered",
    ):
        raise ValueError
    if not _integer(row["structural_level"]) or row["structural_level"] < 1:
        raise ValueError
    if not _integer(row["navigational_order_number"]) or row["navigational_order_number"] < 0:
        raise ValueError
    if row["scope_unit_type"] == "Ordered":
        if not _integer(row.get("local_order")):
            raise ValueError
    elif "local_order" in row:
        raise ValueError
    if "authority_mode" in row and row["authority_mode"] not in ("strict", "casual"):
        raise ValueError
    _validate_paths(row)


def _validate_paths(row: Record) -> None:
    for key in ("authority_path", "delivery_path"):
        value = row[key]
        path = PurePosixPath(value)
        if (
            path.is_absolute()
            or ".." in path.parts
            or "\\" in value
            or "\x00" in value
            or value in (".", "")
        ):
            raise ValueError


def _validate_parentage(units: dict[str, Record]) -> None:
    for name, row in units.items():
        seen, cursor, depth = set(), name, 0
        while cursor != "PROJECT":
            if cursor in seen or cursor not in units:
                raise ValueError
            seen.add(cursor)
            depth += 1
            cursor = units[cursor]["parent"]
        if depth != row["structural_level"]:
            raise ValueError


def _structure(check: Check) -> dict[str, Record] | None:
    if not _authority(check, "CA-D-440", "CA-D-441", "CA-D-442"):
        return None
    document = _inputs(check).get("structure")
    try:
        if not isinstance(document, dict) or set(document) != {"schema_version", "scope_units"}:
            raise ValueError
        if type(document["schema_version"]) is not int or document["schema_version"] != 1:
            raise ValueError
        if not isinstance(document["scope_units"], list):
            raise ValueError
        units: dict[str, Record] = {}
        for row in document["scope_units"]:
            _validate_structure_row(row)
            name = row["scope_unit_name"]
            if name in units:
                raise ValueError
            units[name] = row
        _validate_parentage(units)
        return units
    except KeyError, TypeError, ValueError:
        check.gap(
            "project_structure",
            "A complete, unambiguous Project Structure with valid declared parentage and path encodings is required.",
        )
        return None


def _owner(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _authority(check, "CA-D-276"):
        return
    owner = _value(metadata, "current_scope_unit", check)
    if owner is None:
        return
    units = _structure(check)
    if units is None or owner in units:
        return
    author = metadata.get("author")
    if not _string(author):
        check.gap(
            "current_scope_unit",
            "A non-Scope Unit current_scope_unit needs a complete carried Author before external admission can be assessed.",
        )
        return
    registry = _inputs(check).get("operators_registry", {})
    names = registry.get("names") if isinstance(registry, dict) else None
    if not isinstance(names, frozenset):
        check.gap(
            "current_scope_unit",
            "A non-Scope Unit current_scope_unit needs a complete selected Operator registry before external admission can be assessed.",
        )
        return
    if owner != author:
        check.gap(
            "current_scope_unit",
            "A non-Scope Unit current_scope_unit must equal the carried Author exactly before external admission can be assessed.",
        )
        return
    if owner not in names:
        check.gap(
            "current_scope_unit",
            "A non-Scope Unit current_scope_unit must be an exact registered Operator name before external admission can be assessed.",
        )
        return
    check.gap(
        "current_scope_unit",
        "Exact Author/Operator identity does not prove the Atom is outside all declared Scope Units; caller-bound external-placement admission is required.",
    )


def _target(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _authority(check, "CA-D-482"):
        return
    target = _value(metadata, "claim_target_scope_unit", check)
    owner = _value(metadata, "current_scope_unit", check)
    check.forbid(metadata, "claim_scope")
    units = _structure(check)
    if target is None or owner is None or units is None:
        return
    if target not in units:
        check.gap(
            "claim_target_scope_unit",
            "Target does not resolve to a declared non-Project Scope Unit; the implicit Project requires explicit identity context.",
        )
        return
    if owner not in units:
        check.gap(
            "current_scope_unit",
            "Relational admission requires resolved Project or Operator ownership.",
        )
        return
    if target != owner:
        if not _authority(check, "CA-R-924"):
            return
        qualified = (metadata.get("content_role"), metadata.get("type"))
        if qualified not in (("Requirement", "Goal"), ("Requirement", "Demand"), ("Plan", "Plan")):
            if check.context.unclassified_sources:
                check.gap(
                    "claim_target_scope_unit",
                    "Unclassified authority may extend the complete qualified Relational Atom domain.",
                )
            else:
                check.fail(
                    "TARGET_RELATIONAL_TYPE",
                    "claim_target_scope_unit",
                    "Different owner and target require an admitted complete qualified Relational Atom Type.",
                )


def _tier(metadata: Record, body: str, check: Check) -> None:
    del body
    if not _authority(check, "CA-D-276", "CA-R-155", "CA-R-1413", "CA-R-1566"):
        return
    check.require(metadata, "global_tier", _integer)
    role = metadata.get("content_role")
    ordinary_without_type = role in ("Requirement", "Method", "Delivery") and "type" not in metadata
    if not _string(role) or (not ordinary_without_type and not _string(metadata.get("type"))):
        check.gap(
            "local_tier", "Tier admission requires the complete carried Content Role and Type."
        )
        return
    if metadata.get("content_role") == "Requirement" and metadata.get("type") == "Goal":
        check.gap(
            "local_tier",
            "Project Goal admission and human Operator ownership must be resolved before selecting tier exceptions.",
        )
        return
    local = _value(metadata, "local_tier", check)
    owner = _value(metadata, "current_scope_unit", check)
    if local is not None and local not in ("Principle", "Core", "General", "Standard"):
        check.fail(
            "TIER_VALUE",
            "local_tier",
            "Local Tier is outside the source-bound canonical tier domain.",
        )
    if (
        metadata.get("content_role")
        in ("Concern", "Analysis", "Plan", "Operations", "Implementation")
        and local != "Standard"
    ):
        check.fail(
            "TIER_ROLE",
            "local_tier",
            "Change and Implementation Content Roles require carried Local Tier Standard.",
        )
    _tier_scope(metadata, owner, local, check)


def _tier_scope(metadata: Record, owner: str | None, local: str | None, check: Check) -> None:
    units = _structure(check)
    if units is None or owner is None or local is None:
        return
    if owner not in units:
        check.gap(
            "global_tier",
            "Project or Operator ownership needs explicit identity/admission before resolving Global Tier.",
        )
        return
    if not _authority(check, "CA-R-1389", "CA-R-1390", "CA-R-1391", "CA-R-1442"):
        return
    if local == "Principle":
        check.fail(
            "TIER_SCOPE",
            "local_tier",
            "A non-Project Scope Unit admits Core, General and Standard tiers.",
        )
        return
    if local not in ("Core", "General", "Standard"):
        return
    expected = 3 * units[owner]["structural_level"] + ("Core", "General", "Standard").index(local)
    if _integer(metadata.get("global_tier")) and metadata["global_tier"] != expected:
        check.fail(
            "TIER_GLOBAL",
            "global_tier",
            "Carried Global Tier disagrees with declared parent depth and the source-bound tier mapping.",
        )


def _qualified_status_domain(role: str, kind: str | None, check: Check) -> tuple[str, ...] | None:
    supported = {
        "Requirement": {None, "Requirement", "Goal", "Demand"},
        "Method": {None, "Method"},
        "Evaluation": {"Evaluation", "Evaluation Approach"},
        "Delivery": {None, "Delivery"},
        "Plan": {"Plan"},
        "Concern": {"Question", "Conflict", "Problem"},
    }
    if kind not in supported.get(role, set()):
        check.gap("status", "This complete qualified Type has no reviewed Status model adapter.")
        return None
    code = "domain.status." + role.lower()
    identifiers = {
        "Requirement": "CA-R-1309",
        "Method": "CA-R-1397",
        "Evaluation": "CA-R-1398",
        "Delivery": "CA-R-1399",
        "Plan": "CA-R-1539",
        "Concern": "CA-R-1608",
    }
    if not _authority(check, identifiers[role]):
        return None
    # Evaluation Approach is an admitted, exact Evaluation Type.  It has no
    # independent Status-domain definition, so CA-R-1398 remains its role
    # domain unless a narrower qualified source is supplied below.
    if (role, kind) == ("Evaluation", "Evaluation Approach") and not _authority(
        check, "CAPRMEDIO-R-793"
    ):
        return None
    if role == "Concern" and not _authority(check, "CA-R-1231"):
        return None
    domain = check.context.domains.get(code)
    if not domain:
        check.gap(
            "status",
            "No verified source-bound Status domain is available for the selected qualified Type.",
        )
        return None
    return tuple(domain)


def _unclassified_status(check: Check, role: str, kind: str) -> bool:
    if not check.context.unclassified_sources:
        return False
    for source in _inputs(check).get("sources", []):
        if source.get("binding", {}).get("atom_id") in _pins():
            continue
        subjects = source.get("metadata", {}).get("subjects", {})
        governs = subjects.get("governs") if isinstance(subjects, dict) else None
        if not isinstance(governs, str):
            return True
        # Generic Artifact/Revision/Status authority governs the property, not
        # a role-qualified Status domain.  CA-R-1308 resolves domains from
        # complete qualified paths, so only an unclassified path explicitly
        # naming Content Role and Status can extend the selected domain.
        role_match = re.search(r"(?:^|/)Atom/Content Role: ([^/]+)", governs)
        status_match = re.search(r"(?:^|/)Status(?:$|[:/])", governs)
        type_match = re.search(r"(?:^|/)Type: ([^/]+)", governs)
        if (
            role_match is not None
            and status_match is not None
            and role_match[1] == role
            and (type_match is None or type_match[1] == kind)
        ):
            return True
    return False


def _status_model(metadata: Record, check: Check) -> tuple[str, ...] | None:
    if not _authority(check, "CA-D-483", "CA-R-1308", "CA-R-1313"):
        return None
    role, kind = metadata.get("content_role"), metadata.get("type")
    ordinary_without_type = role in ("Requirement", "Method", "Delivery") and "type" not in metadata
    if not isinstance(role, str) or not role.strip() or (not ordinary_without_type and not _string(kind)):
        check.gap(
            "status", "Status resolution requires the complete carried Content Role and Type path."
        )
        return None
    domain = _qualified_status_domain(role, None if ordinary_without_type else kind, check)
    if domain is None:
        return None
    if _unclassified_status(check, role, "" if ordinary_without_type else kind):
        check.gap(
            "status",
            "Unclassified relevant authority leaves the qualified Status-model override or extension unresolved.",
        )
        return None
    status = _value(metadata, "status", check)
    if status is None:
        return None
    if status not in domain:
        check.fail(
            "STATUS_VALUE",
            "status",
            "Carried Status is outside its exact, case-sensitive qualified Status domain.",
        )
        return None
    return tuple(domain)


def _status(metadata: Record, body: str, check: Check) -> None:
    del body
    _status_model(metadata, check)


def _owner_base(metadata: Record, check: Check) -> Path | None:
    units = _structure(check)
    owner = metadata.get("current_scope_unit")
    if units is None:
        return None
    if not isinstance(owner, str) or owner not in units:
        check.gap(
            "current_scope_unit",
            "Address checking needs one declared non-Project Scope Unit owner.",
        )
        return None
    binding = _inputs(check).get("request", {}).get("project_structure", {})
    supplied = binding.get("path")
    if (
        not isinstance(supplied, str)
        or not Path(supplied).is_absolute()
        or Path(supplied).name != "project_structure.toml"
    ):
        check.gap(
            "project_structure",
            "Address resolution requires the explicit authoritative Project Structure file binding.",
        )
        return None
    root = Path(supplied).parent.parent
    authority_path = units[owner]["authority_path"]
    assert isinstance(authority_path, str)  # The complete row was validated above.
    base = root / authority_path
    # Authority paths cannot bind another Project's control root (CA-D-442).
    if not base.is_relative_to(Path(supplied).parent):
        check.gap(
            "project_structure",
            "Scope authority path does not remain in the explicitly bound Project control root.",
        )
        return None
    reader = _inputs(check).get("reader")
    allowed = getattr(reader, "allowed", None)
    if callable(allowed):
        try:
            allowed(base)
        except OSError:
            check.gap(
                "project_structure",
                "Scope authority path is unavailable or violates the read boundary.",
            )
            return None
    return base


def _placement(metadata: Record, body: str, check: Check) -> None:
    del body
    if "projection" in metadata:
        check.gap(
            "status",
            "Projected representations need their projection-specific placement authority.",
        )
        return
    domain = _status_model(metadata, check)
    if domain is None or not _authority(check, "CA-D-466", "CA-R-1307", "CA-R-1395", "CA-R-1396"):
        return
    path = _inputs(check).get("path")
    if not isinstance(path, Path):
        check.gap("status", "Status placement requires the selected Carrier path.")
        return
    base = _owner_base(metadata, check)
    if base is None:
        return
    if metadata.get("content_role") == "Plan":
        if not _authority(check, "CA-D-461", "CA-D-469"):
            return
        relations = metadata.get("relations", {})
        if not isinstance(relations, dict) or relations.get("is_decomposition_of"):
            check.gap(
                "status",
                "A decomposed Plan requires its resolved immediate target and admitted matching Directory Carrier.",
            )
            return
        directories = {
            "Active": "",
            "Backlog": "001_backlog",
            "Done": "done",
            "Canceled": "canceled",
            "Archived": "archived",
        }
        expected = base / "03_plan" / directories[metadata["status"]]
        container = path.parent.parent if path.parent.name == path.stem else path.parent
        if container != expected:
            check.fail(
                "STATUS_PLACEMENT",
                "status",
                "Plan placement disagrees with its carried Status and local-container mapping.",
            )
        return
    # Applying the fallback as a failure would presume that no more-specific
    # Type mapping exists. That exclusion needs a resolved placement registry.
    check.gap(
        "status",
        "Canonical role-directory placement and absence of a more-specific Type mapping are not resolved by the supplied Project Structure.",
    )


def _summary(body: str) -> str | None:
    headings = _headings(body)
    found = [row for row in headings if row[:2] == (1, "Summary")]
    if len(found) != 1:
        return None
    start = found[0][2]
    end = next(
        (row[2] for row in headings if row[2] > start and row[0] <= 2), len(body.splitlines())
    )
    value = " ".join(line.strip() for line in body.splitlines()[start + 1 : end] if line.strip())
    return value or None


def _address(metadata: Record, body: str, check: Check) -> None:
    if "projection" in metadata:
        check.gap(
            "address", "Projected representations need their projection-specific address authority."
        )
        return
    if not _authority(check, "CA-D-480", "CA-D-282", "CA-D-283", "CA-D-284", "CA-D-302"):
        return
    path = _inputs(check).get("path")
    if not isinstance(path, Path):
        check.gap("address", "Canonical address comparison requires the selected Carrier path.")
        return
    if (
        metadata.get("content_role") == "Plan"
        or metadata.get("type") == "Goal"
        or metadata.get("status") in ("Draft", "draft", "Archived")
    ):
        check.gap(
            "address",
            "Plan, Goal, Draft and historical address grammars require their specific encoding adapters.",
        )
        return
    identifier = _value(metadata, "atom_id", check)
    if identifier is not None and not path.name.startswith(identifier + "-"):
        check.fail(
            "ADDRESS_IDENTITY",
            "atom_id",
            "Filename identity does not agree with the exact carried Atom ID.",
        )
    summary = _summary(body)
    if summary is None or re.search(r"[^A-Za-z0-9 \t-]", summary):
        check.gap(
            "Summary",
            "Summary slug needs a supported complete ASCII Summary serialization; richer syntax is not guessed.",
        )
    else:
        slug = re.sub(r"[\s-]+", "-", summary.lower()).strip("-")
        if not path.name.endswith("--" + slug + ".md"):
            check.fail(
                "ADDRESS_SUMMARY",
                "Summary",
                "Filename Summary Slug differs from the complete carried Summary serialization.",
            )
    base = _owner_base(metadata, check)
    if base is not None and not path.is_relative_to(base):
        check.fail(
            "ADDRESS_OWNER",
            "current_scope_unit",
            "Carrier path is outside its internally declared owner's authority binding.",
        )
    # CA-D-302 explicitly delegates stable Scope-name tokens to Configuration.
    # Neither an uppercase name nor a familiar filename proves that mapping.
    check.gap(
        "address",
        "Exact Scope, Type, target and directory token encodings require registered Project Configuration; unresolved tokens cannot yield full address conformance.",
    )


ADAPTERS = {
    "owner.resolution": _owner,
    "target.resolution": _target,
    "tier.resolution": _tier,
    "status.resolution": _status,
    "status.placement": _placement,
    "address.consistency": _address,
}
