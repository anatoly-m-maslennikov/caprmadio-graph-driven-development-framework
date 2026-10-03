"""Bounded proof for a registered allowed value in a Subject path.

This deliberately recognizes only four fixed, positive value-domain forms:
the CA-R-1662 registration form, a conditional enumerated domain form, and
an explicit named-value legacy bullet under a directly governed Property, plus
the direct internal Carrier Ownership Class enumeration form.
It does not parse general English or create Entity components; callers retain
ordinary meaning/identity review responsibilities.
"""
from __future__ import annotations

import re
from typing import Any

from context_builder import body_section_texts, metadata, prose


_RMEDO_ROLES = frozenset({"Requirement", "Method", "Evaluation", "Delivery", "Operations"})
_PROOF_FIELDS = frozenset({"property", "value", "authority", "excerpt"})
_VALUE_TOKEN = r"[A-Z][A-Za-z0-9]*(?:[ -][A-Z][A-Za-z0-9]*)*"
_REGISTERED_VALUES = re.compile(
    rf"^(?P<first>{_VALUE_TOKEN}) \*\*and\*\* (?P<second>{_VALUE_TOKEN}) "
    r"\*\*must\*\* be registered as internal values of `(?P<property>[^`\n]+)`\.$"
)
_CONDITIONAL_ENUMERATED_DOMAIN = re.compile(
    rf"^an (?P<bearer>{_VALUE_TOKEN}) \*\*must\*\* have \*\*`=1`\*\* "
    rf"(?P<terminal>{_VALUE_TOKEN}) \*\*in\*\* \((?P<first>{_VALUE_TOKEN}), "
    rf"(?P<second>{_VALUE_TOKEN})\) \*\*if\*\* an explicitly defined Status "
    rf"model applies \*\*to\*\* it, \*\*and\*\* \*\*`=0`\*\* "
    rf"(?P=terminal) \*\*otherwise\*\*\.$"
)
_INTERNAL_CARRIER_OWNERSHIP_DOMAIN = re.compile(
    rf"^\*\*every\*\* internal CAPRMEDIO Carrier \*\*must\*\* have \*\*`=1`\*\* "
    rf"Ownership Class \*\*in\*\* \((?P<first>{_VALUE_TOKEN}), "
    rf"(?P<second>{_VALUE_TOKEN}), (?P<third>{_VALUE_TOKEN})\)\.$"
)
_INTERNAL_CARRIER_OWNERSHIP_PROPERTY = "Carrier/Ownership Class"
_NAMED_VALUE_BULLET = re.compile(rf"^- (?P<value>{_VALUE_TOKEN}): (?P<meaning>.+)$")
# Formatting is not an authority boundary: unbolded qualifiers are equally
# disqualifying. This is a conservative supported grammar, not an English parser.
_UNSUPPORTED_CONTEXT = re.compile(
    r"\b(?:if|then|when|unless|until|otherwise|not|without|except|only|"
    r"conditional|conditionally|proposed|proposal|draft|example|illustration|"
    r"provisional|tentative|pending|hypothetical)\b", re.IGNORECASE
)
_STRUCTURED_HEADINGS = frozenset({"summary", "scope", "claim", "details"})
_SECTION_HEADING = re.compile(r"^body:\d+:(#{1,6})\s+(.+?)\s*$")


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _normalized(value: str) -> str:
    return " ".join(value.split())


def _sections_with_headings(sections: dict[str, str]) -> list[tuple[str, int, str]]:
    result = []
    for address in sections:
        match = _SECTION_HEADING.fullmatch(address)
        if match:
            result.append((address, len(match[1]), match[2].casefold()))
    return result


def _legacy_admitted_prose(sections: dict[str, str], headings: list[tuple[str, int, str]]) -> str:
    if len(headings) != 1 or headings[0][1] != 1:
        return ""
    return prose(sections[headings[0][0]])


def _structured_claim_prose(
    sections: dict[str, str], headings: list[tuple[str, int, str]]
) -> str:
    claims = [address for address, depth, name in headings if depth == 2 and name == "claim"]
    titles = [address for address, depth, _ in headings if depth == 1]
    supported = all(
        depth == 1 or (depth == 2 and name in _STRUCTURED_HEADINGS)
        for _, depth, name in headings
    )
    if not supported or len(titles) != 1 or len(claims) != 1:
        return ""
    return prose(sections[claims[0]])


def _admitted_prose(raw: str) -> str:
    """Accept only a one-title legacy carrier or a known structured Claim."""
    sections = body_section_texts(raw)
    headings = _sections_with_headings(sections)
    if any(_UNSUPPORTED_CONTEXT.search(name) for _, _, name in headings):
        return ""
    structured = any(name in _STRUCTURED_HEADINGS for _, _, name in headings)
    if structured:
        return _structured_claim_prose(sections, headings)
    return _legacy_admitted_prose(sections, headings)


def _is_sole_admitted_sentence(raw: str, excerpt: str) -> bool:
    """Accept no prose context beyond the exact positive registration proof.

    The proof is deliberately not found by sentence extraction: adjacent
    conditional, exception, or qualifying prose changes the authoritative
    context and therefore fails closed.
    """
    return _normalized(_admitted_prose(raw)) == _normalized(excerpt)


def _legacy_named_value_bullet(raw: str, proof: dict[str, str]) -> None:
    """Accept one complete named-value bullet under a direct legacy definition.

    The opening paragraph must define the exact governed Property.  The second
    and final paragraph must be a plain list, and the supplied quote must be
    exactly one whole positive ``- Value: ...`` bullet in that list.  This
    prevents a label-like fragment or an arbitrary prose list from becoming a
    value-domain registration.
    """
    sections = body_section_texts(raw)
    headings = _sections_with_headings(sections)
    if any(_UNSUPPORTED_CONTEXT.search(name) for _, _, name in headings):
        raise ValueError("named-value bullet needs an unconditional legacy Claim")
    legacy = _legacy_admitted_prose(sections, headings)
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", legacy) if part.strip()]
    rendered_property = proof["property"].replace("/", " ")
    definition = re.compile(rf"^{re.escape(rendered_property)} \*\*means\*\* .+\.$")
    if (len(paragraphs) != 2 or definition.fullmatch(_normalized(paragraphs[0])) is None
            or _UNSUPPORTED_CONTEXT.search(paragraphs[0])):
        raise ValueError("named-value bullet needs an opening definition of the governed Property")
    bullets = paragraphs[1].splitlines()
    if not bullets or any(not line.startswith("- ") for line in bullets):
        raise ValueError("named-value bullet needs a plain complete value list")
    matching = [line for line in bullets if line == proof["excerpt"]]
    if len(matching) != 1:
        raise ValueError("named-value evidence must quote one complete bound bullet")
    match = _NAMED_VALUE_BULLET.fullmatch(proof["excerpt"])
    if match is None or match["value"] != proof["value"] or _UNSUPPORTED_CONTEXT.search(proof["excerpt"]):
        raise ValueError("named-value bullet is not a positive registration of the proof value")


def _validate_value_domain_sentence(proof: dict[str, str]) -> str:
    """Classify one supported registration or complete conditional-domain proof.

    The latter permits `if` and `otherwise` only as fixed parts of the complete
    cardinality-and-absence guard.  It is not a general exception parser.
    """
    excerpt = _normalized(proof["excerpt"])
    match = _REGISTERED_VALUES.fullmatch(excerpt)
    if match is not None:
        if _UNSUPPORTED_CONTEXT.search(excerpt):
            raise ValueError("allowed-value proof needs one positive registration sentence")
        if proof["property"] != match["property"]:
            raise ValueError("allowed-value proof property differs from its registration sentence")
        if proof["value"] not in (match["first"], match["second"]):
            raise ValueError("allowed-value proof value is not registered by its sentence")
        return "registration"

    if _NAMED_VALUE_BULLET.fullmatch(excerpt) is not None:
        return "named_value_bullet"

    match = _INTERNAL_CARRIER_OWNERSHIP_DOMAIN.fullmatch(excerpt)
    if match is not None:
        if proof["property"] != _INTERNAL_CARRIER_OWNERSHIP_PROPERTY:
            raise ValueError("internal Carrier ownership domain does not match its qualified Property")
        if proof["value"] not in (match["first"], match["second"], match["third"]):
            raise ValueError("value is not admitted by the internal Carrier ownership domain")
        return "internal_carrier_ownership_domain"

    match = _CONDITIONAL_ENUMERATED_DOMAIN.fullmatch(excerpt)
    if match is None:
        raise ValueError("allowed-value proof needs one supported value-domain sentence")
    expected_property = f'{match["bearer"]}/{match["terminal"]}'
    if proof["property"] != expected_property:
        raise ValueError("conditional value domain does not match its qualified Property")
    if proof["value"] not in (match["first"], match["second"]):
        raise ValueError("value is not admitted by the conditional value domain")
    return "conditional_domain"


def _present_proof(mention: Any) -> dict[str, str] | None:
    if not isinstance(mention, dict):
        raise ValueError("allowed-value evidence needs a Subject mention")
    if "allowed_value_evidence" not in mention:
        return None
    proof = mention["allowed_value_evidence"]
    if not isinstance(proof, dict) or set(proof) != _PROOF_FIELDS:
        raise ValueError("invalid allowed-value evidence")
    if any(not _text(proof.get(field)) for field in _PROOF_FIELDS):
        raise ValueError("invalid allowed-value evidence")
    return {field: str(proof[field]).strip() for field in _PROOF_FIELDS}


def _validate_mention_binding(mention: dict[str, Any], proof: dict[str, str]) -> None:
    exact_entity = f'{proof["property"]}: {proof["value"]}'
    if not _text(mention.get("entity")) or mention["entity"] != exact_entity:
        raise ValueError("allowed-value evidence needs the exact qualified Entity path")
    definitions = mention.get("definitions")
    exact_definition = isinstance(definitions, list) and any(
        isinstance(row, dict) and row.get("authority") == proof["authority"]
        and row.get("excerpt") == proof["excerpt"] for row in definitions
    )
    if not exact_definition:
        raise ValueError("allowed-value evidence must repeat one exact bound definition citation")


def _bound_authority_raw(proof: dict[str, str], authorities: Any, targets: Any) -> str:
    if not isinstance(authorities, dict) or not isinstance(targets, dict):
        raise ValueError("allowed-value evidence needs bound authorities and targets")
    raw = authorities.get(proof["authority"])
    if not _text(raw) or targets.get(proof["authority"]) != proof["property"]:
        raise ValueError("allowed-value authority does not directly govern the proof Property")
    return raw


def _validate_authority_metadata(raw: str, property_path: str) -> None:
    props = metadata(raw)
    if not isinstance(props, dict):
        raise ValueError("allowed-value authority metadata is invalid")
    if str(props.get("status", "")).casefold() != "active":
        raise ValueError("allowed-value authority must be Active RMEDO")
    if not isinstance(props.get("content_role"), str) or props["content_role"] not in _RMEDO_ROLES:
        raise ValueError("allowed-value authority must be Active RMEDO")
    subjects = props.get("subjects")
    if not isinstance(subjects, dict) or subjects.get("governs") != property_path:
        raise ValueError("allowed-value authority metadata does not govern the proof Property")


def validate_allowed_value_evidence(mention: Any, authorities: Any, targets: Any, *,
                                    candidate_source: str | None = None) -> bool:
    """Validate a narrowly structured allowed-value proof, or return False if absent.

    A present proof is intentionally fail-closed.  It must be exactly duplicated
    in the mention's normal bound definitions, then be backed by an Active RMEDO
    authority that directly governs the Property and contains the whole positive
    registration sentence in Claim prose (or in legacy title-only body prose).
    """
    proof = _present_proof(mention)
    if proof is None:
        return False
    _validate_mention_binding(mention, proof)
    raw = _bound_authority_raw(proof, authorities, targets)
    if candidate_source is not None and raw == candidate_source:
        raise ValueError("evaluation candidate cannot self-admit allowed-value evidence")
    _validate_authority_metadata(raw, proof["property"])
    form = _validate_value_domain_sentence(proof)
    if form == "named_value_bullet":
        _legacy_named_value_bullet(raw, proof)
    elif not _is_sole_admitted_sentence(raw, proof["excerpt"]):
        raise ValueError("allowed-value proof must be the sole admitted body sentence")
    return True
