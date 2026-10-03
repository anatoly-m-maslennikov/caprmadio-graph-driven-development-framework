"""Bounded ownership proof for an Atom that defines its own GOVERNS target.

This admits only a primary definition/classification Claim. It is not a
general self-citation escape hatch and it does not resolve parent Terms.
"""
from __future__ import annotations

import hashlib
import re
from typing import Any

from context_builder import body_section_texts, metadata, prose


_RMEDO_ROLES = frozenset({"Requirement", "Method", "Evaluation", "Delivery", "Operations"})
_PROOF_FIELDS = frozenset({"entity", "kind", "excerpt", "reason", "component_definitions"})
_COMPONENT_FIELDS = frozenset({"term", "authority", "excerpt"})
_UNSUPPORTED_CLAUSE = re.compile(
    r"\b(?:if|then|when|unless|until|otherwise|conditional|conditionally|example|examples|"
    r"illustrative|hypothetical|proposal|proposed|provisional|tentative|pending)\b", re.IGNORECASE)
_NEGATED_HEADING = re.compile(r"\b(?:not|without)\b", re.IGNORECASE)
_SECTION_HEADING = re.compile(r"^body:\d+:(#{1,6})\s+(.+?)\s*$")
_STRUCTURED_HEADINGS = frozenset({"summary", "scope", "claim", "details"})
_DEFINITION = re.compile(r"^(?:a|an) (?P<term>.+?) \*\*means\*\* .+\.$", re.IGNORECASE)
_CLASSIFICATION = re.compile(
    r"^the Term (?P<term>.+?) \*\*must\*\* be \*\*(?:NARROWER_THAN|BROADER_THAN)\*\* .+\.$",
    re.IGNORECASE)


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _normalized(value: str) -> str:
    return " ".join(value.split())


def _present_proof(mention: Any) -> dict[str, Any] | None:
    if not isinstance(mention, dict):
        raise ValueError("candidate-definition evidence needs a Subject mention")
    if "candidate_definition_evidence" not in mention:
        return None
    proof = mention["candidate_definition_evidence"]
    if not isinstance(proof, dict) or set(proof) != _PROOF_FIELDS:
        raise ValueError("invalid candidate-definition evidence")
    if any(not _text(proof.get(field)) for field in ("entity", "kind", "excerpt", "reason")):
        raise ValueError("invalid candidate-definition evidence")
    if proof["kind"] not in ("definition", "classification"):
        raise ValueError("candidate-definition evidence needs definition or classification kind")
    if not isinstance(proof["component_definitions"], list):
        raise ValueError("candidate-definition evidence needs component definitions")
    return {"entity": str(proof["entity"]).strip(), "kind": str(proof["kind"]).strip(),
            "excerpt": str(proof["excerpt"]).strip(), "reason": str(proof["reason"]).strip(),
            "component_definitions": proof["component_definitions"]}


def _candidate_metadata(candidate_source: Any, candidate_binding: Any) -> dict[str, Any]:
    if not _text(candidate_source) or not isinstance(candidate_binding, dict):
        raise ValueError("candidate-definition evidence needs bound candidate bytes and binding")
    required = {"atom_id", "version", "path", "sha256"}
    if not required <= candidate_binding.keys() or not _text(candidate_binding.get("path")):
        raise ValueError("candidate-definition evidence needs a complete candidate binding")
    if hashlib.sha256(str(candidate_source).encode()).hexdigest() != candidate_binding["sha256"]:
        raise ValueError("candidate-definition evidence candidate bytes contradict binding")
    props = metadata(str(candidate_source))
    if not isinstance(props, dict):
        raise ValueError("candidate-definition evidence candidate metadata is invalid")
    if props.get("atom_id") != candidate_binding["atom_id"] or props.get("version") != candidate_binding["version"]:
        raise ValueError("candidate-definition evidence candidate metadata contradicts binding")
    if str(props.get("status", "")).casefold() != "active" or props.get("content_role") not in _RMEDO_ROLES:
        raise ValueError("candidate-definition evidence needs an Active RMEDO candidate")
    return props


def _admitted_claim_section(raw: str, excerpt: str) -> str:
    sections = body_section_texts(raw)
    headings = []
    for address in sections:
        match = _SECTION_HEADING.fullmatch(address)
        if match is not None:
            headings.append((address, len(match[1]), match[2].casefold()))
    if any(_UNSUPPORTED_CLAUSE.search(name) or _NEGATED_HEADING.search(name)
           for _, _, name in headings):
        raise ValueError("candidate-definition evidence needs unconditional non-negated headings")
    if any(_UNSUPPORTED_CLAUSE.search(name) for _, _, name in headings):
        raise ValueError("candidate-definition evidence needs an unconditional Claim context")
    candidates = [address for address, section in sections.items() if excerpt in prose(section)]
    if len(candidates) != 1:
        raise ValueError("candidate-definition evidence needs one body Claim occurrence")
    candidate = candidates[0]
    titles = [address for address, depth, _ in headings if depth == 1]
    if len(titles) == 1 and candidate == titles[0]:
        title = next(name for address, _, name in headings if address == titles[0])
        structured = any(depth == 2 and name in ("scope", "claim") for _, depth, name in headings)
        if title not in _STRUCTURED_HEADINGS and not structured and not _UNSUPPORTED_CLAUSE.search(title):
            return sections[candidate]
    claims = [address for address, depth, name in headings if depth == 2 and name == "claim"]
    structured = all(depth == 1 or (depth == 2 and name in _STRUCTURED_HEADINGS)
                     for _, depth, name in headings)
    if structured and len(titles) == 1 and len(claims) == 1 and candidate == claims[0]:
        return sections[candidate]
    raise ValueError("candidate-definition evidence needs an unconditional primary Claim")


def _complete_clause(section: str, excerpt: str) -> bool:
    paragraphs = [paragraph.strip() for paragraph in re.split(r"\n\s*\n", prose(section)) if paragraph.strip()]
    return len(paragraphs) == 1 and _normalized(paragraphs[0]) == _normalized(excerpt)


def _path_components(entity: str) -> list[str]:
    if ":" in entity:
        raise ValueError("candidate-definition evidence does not admit value-qualified Entity paths")
    return [part.strip() for part in entity.split("/") if part.strip()]


def _terminal_occurs(entity: str, excerpt: str) -> bool:
    components = _path_components(entity)
    if not components:
        return False
    return re.search(r"(?<![\w/])" + re.escape(components[-1]) + r"(?![\w/:])", excerpt, re.IGNORECASE) is not None


def _explicit_form(kind: str, term: str, excerpt: str) -> bool:
    match = _DEFINITION.fullmatch(excerpt) if kind == "definition" else _CLASSIFICATION.fullmatch(excerpt)
    return match is not None and _normalized(match["term"]).casefold() == _normalized(term).casefold()


def _validate_components(proof: dict[str, Any], candidate_source: str, authorities: Any, targets: Any) -> None:
    required = _path_components(proof["entity"])[:-1]
    supplied = proof["component_definitions"]
    if len(supplied) != len(required):
        raise ValueError("candidate-definition evidence needs one independent definition for every parent component")
    if not isinstance(authorities, dict) or not isinstance(targets, dict):
        raise ValueError("candidate-definition evidence needs bound component authorities")
    seen = set()
    for row in supplied:
        if not isinstance(row, dict) or set(row) != _COMPONENT_FIELDS or any(not _text(row.get(key)) for key in _COMPONENT_FIELDS):
            raise ValueError("invalid candidate-definition component evidence")
        term, authority, excerpt = str(row["term"]).strip(), str(row["authority"]).strip(), str(row["excerpt"]).strip()
        if term not in required or term in seen:
            raise ValueError("candidate-definition component evidence does not match an unresolved parent component")
        seen.add(term)
        raw = authorities.get(authority)
        if not _text(raw) or raw == candidate_source:
            raise ValueError("candidate-definition parent component needs independent bound authority")
        props, target = metadata(str(raw)), targets.get(authority)
        if (not isinstance(props, dict) or str(props.get("status", "")).casefold() != "active"
                or props.get("content_role") not in _RMEDO_ROLES or not _text(target)
                or _path_components(str(target))[-1] != term):
            raise ValueError("candidate-definition parent component authority does not define its exact Term")
        if (excerpt not in prose(str(raw)) or len(excerpt.split()) < 4
                or _UNSUPPORTED_CLAUSE.search(excerpt)):
            raise ValueError("candidate-definition parent component needs substantive body evidence")
        section = _admitted_claim_section(str(raw), excerpt)
        if not _complete_clause(section, excerpt) or not (
                _explicit_form("definition", term, excerpt)
                or _explicit_form("classification", term, excerpt)):
            raise ValueError("candidate-definition parent component needs a complete primary definition or classification")
    if seen != set(required):
        raise ValueError("candidate-definition evidence leaves a parent component unresolved")


def validate_candidate_definition_evidence(mention: Any, *, candidate_source: str | None,
                                           candidate_binding: Any, authorities: Any, targets: Any) -> bool:
    """Validate the sole candidate-owned Entity-definition route, or return False."""
    proof = _present_proof(mention)
    if proof is None:
        return False
    if mention.get("entity") != proof["entity"] or mention.get("resolution_basis") != "meaning":
        raise ValueError("candidate-definition evidence needs the resolved exact Entity by meaning")
    if not _text(mention.get("rationale")) or mention.get("excerpt") != proof["excerpt"]:
        raise ValueError("candidate-definition evidence needs the matching candidate body mention and rationale")
    props = _candidate_metadata(candidate_source, candidate_binding)
    subjects = props.get("subjects")
    if not isinstance(subjects, dict) or subjects.get("governs") != proof["entity"]:
        raise ValueError("candidate-definition evidence only admits the candidate exact GOVERNS target")
    section = _admitted_claim_section(str(candidate_source), proof["excerpt"])
    if not _complete_clause(section, proof["excerpt"]) or _UNSUPPORTED_CLAUSE.search(proof["excerpt"]):
        raise ValueError("candidate-definition evidence needs one complete unconditional primary Claim")
    components = _path_components(proof["entity"])
    if not components:
        raise ValueError("candidate-definition evidence needs a nonempty Entity path")
    if proof["kind"] == "definition" and not _explicit_form("definition", components[-1], proof["excerpt"]):
        raise ValueError("candidate-definition evidence is not an explicit definition")
    if proof["kind"] == "classification" and not _explicit_form("classification", components[-1], proof["excerpt"]):
        raise ValueError("candidate-definition evidence is not a positive classification")
    _validate_components(proof, str(candidate_source), authorities, targets)
    return True
