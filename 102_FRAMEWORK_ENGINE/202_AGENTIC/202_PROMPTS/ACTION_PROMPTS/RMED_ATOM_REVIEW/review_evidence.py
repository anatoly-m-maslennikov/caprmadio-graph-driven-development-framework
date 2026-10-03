"""Evidence admission, not semantic inference or a replacement for the reviewer."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import math
import re
from pathlib import PurePosixPath
from typing import Any, TypeGuard

from allowed_value_evidence import validate_allowed_value_evidence
from candidate_definition_evidence import validate_candidate_definition_evidence
from declared_subject_evidence import validate_declared_subject_evidence
from relation_ordering import validate_ordering_policy
from context_builder import (authority_reference, body_sections, body_section_texts,
                             metadata, prose, validated_candidate_bindings,
                             validated_principle_admissions, validate_baseline_sources)


def text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def probability(value: Any) -> TypeGuard[float | int]:
    return (type(value) in (float, int) and math.isfinite(value) and 0 <= value <= 1)


def strings(value: Any, *, empty: bool = False) -> bool:
    return isinstance(value, list) and (empty or bool(value)) and all(text(v) for v in value)


class ReviewContext:
    """Caller-owned frozen packet. The response cannot choose its own threshold.

    Normalize already supplied context into confidence_threshold and sources
    (binding + text records); retain other Run context in the same packet. Source
    identity/admission and filesystem freshness remain caller responsibilities.
    """

    def __init__(self, packet: dict[str, Any]):
        snapshot = deepcopy(packet)
        if not probability(snapshot.get("confidence_threshold")):
            raise ValueError("invalid caller confidence threshold")
        self.confidence_threshold = snapshot["confidence_threshold"]
        constraints = snapshot.get('review_constraints', {})
        if not isinstance(constraints, dict):
            raise ValueError('caller review_constraints must be a mapping')
        self.report_contract = constraints.get('report_contract', 4)
        self.operator_precheck = constraints.get('operator_precheck')
        if self.operator_precheck is not None:
            if (self.report_contract != 6 or not isinstance(self.operator_precheck, list)
                    or not self.operator_precheck
                    or any(not isinstance(v, str) or not v for v in self.operator_precheck)):
                raise ValueError('operator precheck needs an explicit contract-6 operator inventory')
        if type(self.report_contract) is not int or self.report_contract not in (4, 5, 6):
            raise ValueError('caller report_contract must be 4, 5 or 6')
        if self.report_contract == 6:
            if constraints.get('review_profile') != 'atom_local':
                raise ValueError('contract 6 needs an explicit atom_local profile')
            if (not isinstance(snapshot.get('candidate_bindings'), list)
                    or len(snapshot['candidate_bindings']) != 1):
                raise ValueError('atom_local context needs exactly one candidate')
            if not isinstance(snapshot.get('authority_bindings'), list):
                raise ValueError('atom_local context needs an explicit rule allowlist')
            if snapshot['candidate_bindings'][0] in snapshot['authority_bindings']:
                raise ValueError('a local candidate cannot admit itself as a checking rule')
        self.relation_ordering = validate_ordering_policy(snapshot.get('relation_ordering'))
        self.preflight = snapshot.get('preflight', {})
        self.authority_bindings = snapshot.get('authority_bindings')
        if self.authority_bindings is not None and not isinstance(self.authority_bindings, list):
            raise ValueError('authority_bindings must be an explicit binding list')
        raw = json.dumps(snapshot, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=False, allow_nan=False).encode()
        self.sha256 = hashlib.sha256(raw).hexdigest()
        self._sources: dict[str, dict[str, Any]] = {}
        sources = snapshot.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValueError("context requires bound source texts")
        for record in sources:
            if not isinstance(record, dict) or not isinstance(record.get("binding"), dict):
                raise ValueError("invalid context source")
            binding = record["binding"]
            if not {"atom_id", "version", "path", "sha256"} <= binding.keys():
                raise ValueError("incomplete context source binding")
            if not text(binding["path"]) or not text(record.get("text")):
                raise ValueError("missing source path or text")
            if hashlib.sha256(record["text"].encode()).hexdigest() != binding["sha256"]:
                raise ValueError("source text contradicts binding")
            if binding["path"] in self._sources:
                raise ValueError("duplicate context source path")
            self._sources[binding["path"]] = record
        validate_baseline_sources(snapshot)
        self._principles = {row['binding']['path']: row
                            for row in validated_principle_admissions(snapshot)}
        self._candidates = validated_candidate_bindings(snapshot)
        if self.operator_precheck is not None:
            from operator_precheck import word_inventory
            registry_ref = constraints.get('operator_registry')
            registries = [r for r in self._sources.values()
                          if authority_reference(r['binding']) == registry_ref
                          and r['binding'] in (self.authority_bindings or [])]
            if len(registries) != 1:
                raise ValueError('operator precheck requires one bound registry authority')
            expected = word_inventory(registries[0]['text'])
            if sorted(self.operator_precheck) != sorted(expected):
                raise ValueError('operator precheck inventory differs from bound authority')

    def source_text(self, binding: Any) -> str:
        if not isinstance(binding, dict) or not text(binding.get("path")):
            raise ValueError("invalid source binding")
        record = self._sources.get(binding["path"])
        if record is None or binding != record["binding"]:
            raise ValueError("unbound or changed source")
        return str(record["text"])

    def candidate_text(self, binding: Any) -> str:
        raw = self.source_text(binding)
        if self._candidates is not None and binding not in self._candidates:
            raise ValueError('source is not a selected evaluation candidate')
        return raw

    def authorities(self, bindings: list[Any], *, candidate: Any = None) -> dict[str, str]:
        result = {}
        for binding in bindings:
            if self.authority_bindings is not None and binding not in self.authority_bindings:
                raise ValueError('source is bound as input, not admitted as authority')
            body = self.source_text(binding)
            principle = self._principles.get(binding['path'])
            carried_identity = text(binding.get('atom_id')) and type(binding.get('version')) is int
            if principle is not None:
                if candidate is None:
                    raise ValueError('Principle citation needs a bound candidate')
                self.candidate_text(candidate)
                if candidate['path'] not in principle['applicable_to']:
                    raise ValueError('Principle applicability excludes this candidate')
                if not carried_identity and self.authority_bindings is None:
                    raise ValueError('Legacy Principle citation needs an explicit authority allowlist')
            if principle is None and not carried_identity:
                raise ValueError("authority needs a carried identity")
            ref = authority_reference(binding)
            if ref in result:
                raise ValueError("ambiguous or duplicate authority reference")
            result[ref] = body
        return result

    def authority_paths(self, bindings: list[Any], *, candidate: Any = None) -> dict[str, str]:
        """Return citation addresses only after caller-owned binding admission."""
        self.authorities(bindings, candidate=candidate)
        return {authority_reference(binding): binding['path'] for binding in bindings}

    def authority_targets(self, authorities: dict[str, str]) -> dict[str, str]:
        targets = {}
        for ref, raw in authorities.items():
            props = metadata(raw)
            subjects = props.get('subjects')
            if isinstance(subjects, dict) and text(subjects.get('governs')):
                targets[ref] = subjects['governs']
        return targets

    def admitted_principle_references(self, bindings: list[Any], *, candidate: Any) -> frozenset[str]:
        """Return only context-admitted Principles applicable to this candidate."""
        self.candidate_text(candidate)
        result = set()
        for binding in bindings:
            if not isinstance(binding, dict) or not text(binding.get('path')):
                raise ValueError('invalid authority binding')
            principle = self._principles.get(binding['path'])
            if principle is None:
                continue
            if self.authority_bindings is not None and binding not in self.authority_bindings:
                raise ValueError('source is bound as input, not admitted as authority')
            if candidate['path'] not in principle['applicable_to']:
                raise ValueError('Principle applicability excludes this candidate')
            result.add(authority_reference(binding))
        return frozenset(result)


def validate_quotes(quotes: Any, authorities: dict[str, str], *, empty: bool = False) -> None:
    if not isinstance(quotes, list) or (not quotes and not empty):
        raise ValueError("missing bound evidence quotes")
    for quote in quotes:
        if not isinstance(quote, dict) or not text(quote.get("authority")) or not text(quote.get("excerpt")):
            raise ValueError("invalid authority quote")
        if quote["authority"] not in authorities or quote["excerpt"] not in authorities[quote["authority"]]:
            raise ValueError("authority quote is not in the bound source")


def _obligation_states(row: dict[str, Any], authorities: dict[str, str]) -> dict[str, str]:
    records = row.get("obligation_resolutions")
    if not isinstance(records, list):
        raise ValueError("missing obligation resolutions")
    states = {}
    for record in records:
        if not isinstance(record, dict) or not text(record.get("id")) or not text(record.get("reason")):
            raise ValueError("invalid obligation resolution")
        identifier, state = record["id"], record.get("state")
        if identifier in states or state not in ("local", "inherited", "missing", "unresolved", "conflicting"):
            raise ValueError("duplicate or invalid obligation resolution")
        states[identifier] = state
        unresolved = state in ("unresolved", "conflicting")
        local_required = record.get("local_required")
        if type(local_required) is not bool and not (unresolved and local_required is None):
            raise ValueError("obligation must resolve whether local restatement is required")
        validate_quotes(record.get("support"), authorities, empty=unresolved)
        if state == "inherited" and local_required is not False:
            raise ValueError("inherited rule cannot satisfy mandatory local content")
        if unresolved and row["status"] != "blocked":
            raise ValueError("unresolved obligation needs a check-specific gap")
    return states


def validate_obligations(row: dict[str, Any], authorities: dict[str, str]) -> None:
    """Require an explicit inheritance resolution before alleging an omission."""
    states = _obligation_states(row, authorities)
    omissions = set()
    for finding in row["findings"]:
        if finding["kind"] == "omission":
            identifier = finding.get("obligation_id")
            if not text(identifier) or states.get(identifier) != "missing":
                raise ValueError("omission is not supported by resolved missing authority")
            omissions.add(identifier)
    if any(state == "missing" and identifier not in omissions for identifier, state in states.items()):
        raise ValueError("confirmed missing obligation must retain its finding")


def _markdown(source: str) -> str:
    # Exclude frontmatter from body-mention evidence. This is not a YAML parser.
    lines = source.splitlines(keepends=True)
    if lines and lines[0].strip() == "---":
        end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None)
        if end is None:
            raise ValueError("cannot locate Markdown for Subject evidence")
        source = "".join(lines[end + 1:])
    return source


def _validate_mention(mention: Any, source: str, authorities: dict[str, str],
                      targets: dict[str, str], *, candidate_source: str | None = None,
                      candidate_binding: dict[str, Any] | None = None,
                      admitted_legacy_principles: frozenset[str] = frozenset(),
                      authority_paths: dict[str, str] | None = None) -> bool:
    if not isinstance(mention, dict) or any(not text(mention.get(k)) for k in ("location", "excerpt", "rationale")):
        raise ValueError("invalid Subject mention evidence")
    if mention["excerpt"] not in source:
        raise ValueError("Subject excerpt is not in Markdown")
    _validate_mention_location(mention, source)
    resolution = mention.get("resolution")
    if resolution not in ("resolved", "general", "unresolved"):
        raise ValueError("unknown Subject resolution")
    if mention.get('citation_evidence') is not None and (resolution != 'general' or mention.get('entity') is not None):
        raise ValueError('citation evidence is only allowed on a general non-Entity mention')
    if resolution == "resolved":
        _validate_resolved_mention(mention, authorities, targets, candidate_source=candidate_source,
                                   candidate_binding=candidate_binding,
                                   admitted_legacy_principles=admitted_legacy_principles)
    else:
        if mention.get("entity") is not None:
            raise ValueError("unresolved/general mention cannot assert an Entity path")
        validate_quotes(mention.get("definitions"), authorities, empty=True)
        if mention.get('citation_evidence') is not None:
            _validate_citation_evidence(mention, source, authorities, authority_paths)
    return bool(resolution == "unresolved")


def _validate_resolved_mention(mention: dict[str, Any], authorities: dict[str, str],
                               targets: dict[str, str], *, candidate_source: str | None = None,
                               candidate_binding: dict[str, Any] | None = None,
                               admitted_legacy_principles: frozenset[str] = frozenset()) -> None:
    if not text(mention.get('entity')):
        raise ValueError('resolved Subject needs a full Entity path')
    basis = mention.get('resolution_basis')
    if basis not in ('identity', 'meaning'):
        raise ValueError('resolved Subject needs identity or meaning resolution basis')
    candidate_defined = validate_candidate_definition_evidence(
        mention, candidate_source=candidate_source, candidate_binding=candidate_binding,
        authorities=authorities, targets=targets)
    validate_quotes(mention.get('definitions'), authorities, empty=candidate_defined)
    if basis == 'identity':
        _validate_literal_identity(mention, authorities)
    anchored = False
    for definition in mention['definitions']:
        ref, excerpt = definition['authority'], definition['excerpt']
        if candidate_source is not None and authorities[ref] == candidate_source:
            raise ValueError('evaluation candidate cannot self-admit an exact Entity anchor')
        if excerpt not in prose(authorities[ref]) or len(excerpt.split()) < 4:
            raise ValueError('Entity definition needs substantive body evidence, not a title or metadata')
        # Every citation must be substantive and bound, but supplementary
        # sources may explain an anchored Entity without creating its identity.
        anchored = anchored or mention['entity'] == targets.get(ref)
    # A directly registered value qualifies its exact Property without needing
    # a duplicate Definition Atom governing the whole composed path. A supplied
    # proof is always checked, even when another exact anchor exists.
    value_admitted = validate_allowed_value_evidence(
        mention, authorities, targets, candidate_source=candidate_source)
    declared_admitted = validate_declared_subject_evidence(
        mention, authorities, candidate_source=candidate_source,
        admitted_legacy_principles=admitted_legacy_principles)
    if not anchored and not value_admitted and not declared_admitted and not candidate_defined:
        raise ValueError('resolved Subject needs an exact full Entity authority anchor')


def literal_occurs(entity: str, source: str) -> bool:
    return bool(_literal_occurrence_spans(entity, source))


def _literal_occurrence_spans(entity: str, source: str) -> list[tuple[int, int]]:
    literal = r'(?<![\w/])' + re.escape(entity) + r'(?![\w/:])'
    return [match.span() for match in re.finditer(literal, source)]


def _section_spans(source: str) -> dict[str, tuple[int, int]]:
    """Return exact Markdown offsets for the section addresses used by reviews."""
    sections: list[tuple[str, int]] = [('body:preamble', 0)]
    fence: str | None = None
    offset = 0
    for number, line in enumerate(source.splitlines(keepends=True), 1):
        stripped = line.rstrip('\r\n')
        match = re.match(r'^\s*(`{3,}|~{3,})', stripped)
        if match:
            token = match[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
        elif fence is None and re.match(r'^#{1,6}\s', stripped):
            sections.append((f'body:{number}:{stripped.strip()}', offset))
        offset += len(line)
    return {address: (start, sections[index + 1][1] if index + 1 < len(sections) else len(source))
            for index, (address, start) in enumerate(sections)}


def _validate_citation_evidence(mention: dict[str, Any], source: str,
                                authorities: dict[str, str],
                                authority_paths: dict[str, str] | None) -> list[tuple[int, int]]:
    """Admit exact filename-without-.md citation spans from bound addresses.

    This deliberately validates provenance and location, not whether a
    reviewer correctly classified a citation as non-substantive.  Such spans
    can exempt only their own characters from the declared-target literal
    guard below. The caller's admitted path supplies the filename; response
    fields, Atom IDs, Summaries and surrounding folders cannot reconstruct it.
    """
    evidence = mention.get('citation_evidence')
    if not isinstance(evidence, dict):
        raise ValueError('invalid citation evidence')
    authority = evidence.get('authority')
    atom_id = evidence.get('atom_id')
    filename = evidence.get('filename')
    spans = evidence.get('spans')
    if (not text(authority) or not text(atom_id) or not text(filename)
            or not isinstance(spans, list) or not spans):
        raise ValueError('citation evidence needs authority, Atom ID, filename, and spans')
    bound = authorities.get(authority)
    if bound is None:
        raise ValueError('citation evidence authority is not bound')
    props = metadata(bound)
    version = props.get('version')
    if props.get('atom_id') != atom_id or type(version) is not int or authority != f'{atom_id}@{version}':
        raise ValueError('citation evidence does not identify its exact bound Atom source')
    path = (authority_paths or {}).get(authority)
    if not text(path) or not path.endswith('.md'):
        raise ValueError('citation evidence needs a bound Markdown Carrier path')
    label = PurePosixPath(path).name[:-3]
    if filename != label:
        raise ValueError('citation filename differs from the complete bound filename without .md')
    matching_paths = {value for ref, value in (authority_paths or {}).items()
                      if ref in authorities and text(value) and value.endswith('.md')
                      and PurePosixPath(value).name[:-3] == label}
    if len(matching_paths) != 1:
        raise ValueError('citation filename is ambiguous across bound sources')
    sections = _section_spans(source)
    claimed_sections = [address for address in sections
                        if address == mention['location']
                        or address.split(':', 2)[-1].lstrip('# ') == mention['location']]
    if len(claimed_sections) != 1:
        raise ValueError('citation evidence has no unambiguous claimed Markdown section')
    validated: list[tuple[int, int]] = []
    for span in spans:
        if (not isinstance(span, dict) or not text(span.get('section'))
                or type(span.get('start')) is not int or type(span.get('end')) is not int
                or not text(span.get('text'))):
            raise ValueError('invalid citation span')
        section = span['section']
        start, end = span['start'], span['end']
        if section not in sections or section != claimed_sections[0] or start < 0 or end <= start or end > len(source):
            raise ValueError('citation span has an invalid Markdown section or range')
        section_start, section_end = sections[section]
        if start < section_start or end > section_end:
            raise ValueError('citation span falls outside its claimed Markdown section')
        if source[start:end] != span['text'] or span['text'] != label:
            raise ValueError('citation span is not the exact bound filename without .md')
        if span['text'] not in mention['excerpt']:
            raise ValueError('citation span is unrelated to its general mention excerpt')
        validated.append((start, end))
    if len(validated) != len(set(validated)):
        raise ValueError('duplicate citation span')
    return validated


def _validate_qualified_literal_evidence(mention: dict[str, Any], source: str,
                                         authorities: dict[str, str],
                                         candidate_binding: dict[str, Any] | None) -> tuple[str, list[tuple[int, int]]] | None:
    """Bind reviewer-classified qualified literals to one resolved mention.

    Offsets are Python string (Unicode-codepoint) offsets into ``source`` after
    frontmatter removal.  This validates exact coverage/provenance only; the
    already-validated resolved meaning mention remains responsible for the
    semantic mapping.
    """
    if 'qualified_literal_evidence' not in mention:
        return None
    evidence = mention['qualified_literal_evidence']
    if not isinstance(evidence, dict) or set(evidence) != {'declared_entity', 'mention_span', 'literal_spans'}:
        raise ValueError('invalid qualified literal evidence')
    if mention.get('resolution') != 'resolved' or mention.get('resolution_basis') != 'meaning':
        raise ValueError('qualified literal evidence needs a resolved meaning mention')
    if mention.get('candidate_definition_evidence') is not None:
        raise ValueError('qualified literal evidence cannot use candidate-definition admission')
    proof = mention.get('declared_subject_evidence')
    if not isinstance(proof, dict) or not text(proof.get('authority')):
        raise ValueError('qualified literal evidence needs declared Subject meaning evidence')
    if not isinstance(candidate_binding, dict) or not text(candidate_binding.get('atom_id')):
        raise ValueError('qualified literal evidence needs the bound candidate identity')
    proof_raw = authorities.get(proof['authority'])
    if not text(proof_raw):
        raise ValueError('qualified literal evidence needs a bound declared Subject authority')
    if metadata(proof_raw).get('atom_id') == candidate_binding['atom_id']:
        raise ValueError('qualified literal evidence cannot use a same-Atom candidate alias')
    declared = evidence.get('declared_entity')
    entity = mention.get('entity')
    if not text(declared) or not text(entity) or '/' not in entity or entity.rsplit('/', 1)[1] != declared:
        raise ValueError('qualified literal evidence needs the resolved Entity terminal as declared entity')
    sections = _section_spans(source)
    claimed_sections = [address for address in sections
                        if address == mention['location']
                        or address.split(':', 2)[-1].lstrip('# ') == mention['location']]
    if len(claimed_sections) != 1:
        raise ValueError('qualified literal evidence has no unambiguous mention section')
    span = evidence.get('mention_span')
    if (not isinstance(span, dict) or set(span) != {'section', 'start', 'end', 'text'}
            or not text(span.get('section')) or type(span.get('start')) is not int
            or type(span.get('end')) is not int or not text(span.get('text'))):
        raise ValueError('invalid qualified literal mention span')
    section = span['section']
    start, end = span['start'], span['end']
    if section != claimed_sections[0] or section not in sections or start < 0 or end <= start or end > len(source):
        raise ValueError('qualified literal mention span has an invalid section or range')
    section_start, section_end = sections[section]
    if start < section_start or end > section_end or source[start:end] != span['text'] or span['text'] != mention['excerpt']:
        raise ValueError('qualified literal mention span is not the exact resolved mention excerpt')
    literals = evidence.get('literal_spans')
    if not isinstance(literals, list) or not literals:
        raise ValueError('qualified literal evidence needs literal spans')
    expected = [(left, right) for left, right in _literal_occurrence_spans(declared, source)
                if start <= left and right <= end]
    validated: list[tuple[int, int]] = []
    for literal in literals:
        if (not isinstance(literal, dict) or set(literal) != {'section', 'start', 'end', 'text'}
                or literal.get('section') != section or type(literal.get('start')) is not int
                or type(literal.get('end')) is not int or not text(literal.get('text'))):
            raise ValueError('invalid qualified literal span')
        left, right = literal['start'], literal['end']
        if (left < start or right <= left or right > end or source[left:right] != literal['text']
                or literal['text'] != declared or (left, right) not in expected):
            raise ValueError('qualified literal span is not an exact declared-entity occurrence')
        validated.append((left, right))
    if len(validated) != len(set(validated)) or set(validated) != set(expected):
        raise ValueError('qualified literal evidence must account for every literal in its exact mention span')
    return declared, validated


def _validate_literal_identity(mention: dict[str, Any], authorities: dict[str, str]) -> None:
    if not literal_occurs(mention['entity'], mention['excerpt']):
        raise ValueError('identity recognition requires an exact canonical literal, not a paraphrase')
    for citation in mention.get('definitions', []):
        props = metadata(authorities.get(citation.get('authority'), ''))
        if str(props.get('status', '')).casefold() != 'active':
            raise ValueError('literal identity admission needs explicit Active authority')
        if props.get('content_role') not in ('Requirement', 'Method', 'Evaluation', 'Delivery', 'Operations'):
            raise ValueError('a Concern or Plan is not Entity identity admission authority')


def _validate_mention_location(mention: dict[str, Any], source: str) -> None:
    sections = body_section_texts(source)
    address = mention['location']
    # Accept an unambiguous registered heading alias as well as its exact
    # line-address. Never let an excerpt elsewhere validate a wrong location.
    candidates = [value for key, value in sections.items()
                  if key == address or key.split(':', 2)[-1].lstrip('# ') == address]
    if len(candidates) != 1 or mention['excerpt'] not in candidates[0]:
        raise ValueError('Subject excerpt is absent from its claimed Markdown section')


def _validate_sections(inventory: dict[str, Any], source: str) -> None:
    expected_sections = body_sections(source)
    reviewed = inventory.get('sections_reviewed')
    if not isinstance(reviewed, list) or not strings(reviewed, empty=True):
        raise ValueError('invalid reviewed section inventory')
    if len(reviewed) != len(set(reviewed)) or not set(reviewed) <= set(expected_sections):
        raise ValueError('invalid reviewed section inventory')
    if inventory['complete'] and set(reviewed) != set(expected_sections):
        raise ValueError('complete inventory omitted Markdown sections')


def _declared_subjects(source: str) -> list[Any]:
    properties = metadata(source).get('subjects', {})
    declared: list[Any] = []
    if isinstance(properties, dict):
        if text(properties.get('governs')):
            declared.append(properties['governs'])
        if isinstance(properties.get('depends_on'), list):
            declared.extend(properties['depends_on'])
    return declared


def _validate_subject_findings(row: dict[str, Any], resolved: set[str], declared: list[Any]) -> None:
    for finding in row['findings']:
        if finding.get('subject_issue') == 'extra':
            if (finding['kind'] != 'violation' or finding.get('entity') not in declared
                    or finding['entity'] in resolved or not row['subject_inventory']['complete']):
                raise ValueError('extra Subject needs a complete inventory excluding a declared target')
            continue
        if finding.get('entity') not in resolved:
            raise ValueError('Subject finding lacks a resolved Entity mapping')
        if (finding['kind'] == 'violation' and finding.get('entity') not in declared
                and finding.get('subject_issue') != 'governs'):
            raise ValueError('missing Subject requires an omission resolution or explicit governs mismatch')
        if finding['kind'] == 'omission' and finding['entity'] in declared:
            raise ValueError('Subject omission names an already declared Entity')


def _validate_subject_accounting(row: dict[str, Any], resolved: set[str],
                                 declared: list[Any], governs: Any) -> None:
    """Check the reviewer's own set comparison, not the truth of its mappings.

    An incomplete inventory can preserve a target while a contextual reference
    is unresolved. A complete inventory cannot silently drop that uncertainty
    and claim success, or omit a defect implied by its own resolved inventory.
    """
    governing = {f['entity'] for f in row['findings']
                 if f.get('subject_issue') == 'governs'}
    if isinstance(governs, str) and governs in governing:
        raise ValueError('governing mismatch names the Entity already GOVERNS')
    if not row['subject_inventory']['complete']:
        return
    if any(not text(value) for value in declared):
        raise ValueError('complete Subject comparison requires valid declared targets')
    declarations = set(declared)
    omissions = {f['entity'] for f in row['findings'] if f['kind'] == 'omission'}
    extras = {f['entity'] for f in row['findings'] if f.get('subject_issue') == 'extra'}
    if resolved - declarations - omissions - governing:
        raise ValueError('complete Subject inventory has unaccounted resolved targets')
    # A coordinated replacement of GOVERNS accounts for the old target without
    # demanding a second, redundant deletion finding for that same correction.
    replaced = {governs} if governing and isinstance(governs, str) else set()
    if declarations - resolved - extras - replaced:
        raise ValueError('complete Subject inventory has unaccounted declared targets')
    duplicates = {value for value in declarations if declared.count(value) > 1}
    violations = {f['entity'] for f in row['findings'] if f['kind'] == 'violation'}
    if duplicates - violations:
        raise ValueError('complete Subject inventory ignores duplicate declared targets')


def _citation_spans(mentions: list[Any], source: str,
                    authorities: dict[str, str],
                    authority_paths: dict[str, str] | None) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for mention in mentions:
        if (isinstance(mention, dict) and mention.get('resolution') == 'general'
                and mention.get('citation_evidence') is not None):
            spans.extend(_validate_citation_evidence(mention, source, authorities, authority_paths))
    return spans


def _uncovered_literal_occurrence(entity: str, source: str,
                                  exempt_spans: list[tuple[int, int]]) -> bool:
    """Keep an extra-target finding guarded by every substantive occurrence."""
    for start, end in _literal_occurrence_spans(entity, source):
        if not any(exempt_start <= start and end <= exempt_end
                   for exempt_start, exempt_end in exempt_spans):
            return True
    return False


def validate_subject_inventory(row: dict[str, Any], source: str, authorities: dict[str, str],
                               targets: dict[str, str], *,
                               candidate_binding: dict[str, Any] | None = None,
                               admitted_legacy_principles: frozenset[str] = frozenset(),
                               authority_paths: dict[str, str] | None = None) -> None:
    declared = _declared_subjects(source)
    subjects = metadata(source).get('subjects', {})
    governs = subjects.get('governs') if isinstance(subjects, dict) else None
    inventory = row.get("subject_inventory")
    if not isinstance(inventory, dict) or type(inventory.get("complete")) is not bool:
        raise ValueError("missing structured Subject inventory")
    mentions = inventory.get("mentions")
    if not isinstance(mentions, list):
        raise ValueError("invalid Subject mentions")
    _validate_sections(inventory, source)
    candidate_source = source
    source = _markdown(source)
    unresolved = not inventory["complete"]
    resolved = set()
    qualified_spans: dict[str, list[tuple[int, int]]] = {}
    for mention in mentions:
        ambiguous = _validate_mention(mention, source, authorities, targets,
                                      candidate_source=candidate_source,
                                      candidate_binding=candidate_binding,
                                      admitted_legacy_principles=admitted_legacy_principles,
                                      authority_paths=authority_paths)
        if inventory['complete'] and ambiguous:
            raise ValueError('complete inventory contains unresolved mentions')
        unresolved |= ambiguous
        if mention['resolution'] == 'resolved':
            resolved.add(mention['entity'])
        qualified = _validate_qualified_literal_evidence(
            mention, source, authorities, candidate_binding)
        if qualified is not None:
            declared_entity, spans = qualified
            qualified_spans.setdefault(declared_entity, []).extend(spans)
    _validate_subject_findings(row, resolved, declared)
    _validate_subject_accounting(row, resolved, declared, governs)
    citation_spans = _citation_spans(mentions, source, authorities, authority_paths)
    for finding in row['findings']:
        if (finding.get('subject_issue') == 'extra'
                and _uncovered_literal_occurrence(
                    finding['entity'], source,
                    citation_spans + qualified_spans.get(finding['entity'], []))):
            raise ValueError('extra Subject has a literal Markdown occurrence requiring resolution')
    if not mentions and row["status"] == "passed":
        raise ValueError("complete Subject review needs positive mention evidence")
    if unresolved and row["status"] != "blocked":
        raise ValueError("unresolved Subject inventory needs a subjects gap")
