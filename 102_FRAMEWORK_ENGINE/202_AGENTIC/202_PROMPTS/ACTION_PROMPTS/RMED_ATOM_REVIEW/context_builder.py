"""Prepare source-backed retrieval context. Never infer authority from folders.

The Entity index is a candidate index, not an automatically proved ontology.
Resources are explicit caller-selected paths; no recursive filesystem discovery.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import sys
import tomllib
from typing import Any

CHECKER = Path(__file__).resolve().parents[4] / '201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS'
sys.path.insert(0, str(CHECKER))


def metadata(raw: str) -> dict[str, Any]:
    """Reuse the safe, duplicate-key-rejecting, bounded production YAML parser."""
    from validate_atoms_workers.parsing import CarrierError, parse_carrier  # type: ignore[import-not-found]
    try:
        return dict(parse_carrier(raw.encode(), Path('context.md')).metadata)
    except CarrierError:
        return {}


def markdown(raw: str) -> str:
    lines = raw.splitlines(keepends=True)
    if lines and lines[0].strip() == '---':
        end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == '---'), None)
        if end is None:
            raise ValueError('cannot locate Markdown')
        return ''.join(lines[end + 1:])
    return raw


def body_section_texts(raw: str) -> dict[str, str]:
    """Stable line-addresses for actual headings, including legacy titles.

    Fenced examples cannot invent sections. These addresses are evidence
    coverage bookkeeping, not inferred Atom properties or authoring repairs.
    """
    sections: dict[str, list[str]] = {'body:preamble': []}
    current = 'body:preamble'
    fence = None
    for number, line in enumerate(markdown(raw).splitlines(), 1):
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            token = match[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
        elif fence is None and re.match(r'^#{1,6}\s', line):
            current = f'body:{number}:{line.strip()}'
            sections[current] = []
        sections[current].append(line)
    return {address: '\n'.join(lines) for address, lines in sections.items()}


def body_sections(raw: str) -> list[str]:
    return list(body_section_texts(raw))


def _unquoted_prose_lines(raw: str) -> list[str]:
    lines = []
    fence = None
    for line in markdown(raw).splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            token = match[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
        elif fence is None and not re.match(r'^(?: {4}|\t|\s*>)', line):
            lines.append(line)
    return lines


def prose(raw: str) -> str:
    """Definition evidence excludes headings and the navigation-only Summary."""
    lines = []
    summary = False
    for line in _unquoted_prose_lines(raw):
        heading = re.match(r'^\s*#{1,6}\s+(.+?)\s*$', line)
        if heading:
            summary = heading[1].casefold() == 'summary'
        elif not summary:
            lines.append(line)
    return '\n'.join(lines)


def authority_reference(binding: dict[str, Any]) -> str:
    """Name bound evidence, not an inferred identity for a legacy Carrier."""
    if (isinstance(binding.get('atom_id'), str) and binding['atom_id'].strip()
            and type(binding.get('version')) is int):
        return f'{binding["atom_id"]}@{binding["version"]}'
    return f'source:{binding["path"]}#sha256={binding["sha256"]}'


def validated_candidate_bindings(packet: dict[str, Any]) -> list[dict[str, Any]] | None:
    """A selected evaluation target is distinct from retrieved authority."""
    candidates = packet.get('candidate_bindings')
    if candidates is None:
        return None
    bindings = [record['binding'] for record in packet.get('sources', [])]
    if (not isinstance(candidates, list) or not candidates
            or any(binding not in bindings for binding in candidates)):
        raise ValueError('candidate_bindings must select exact bound sources')
    paths = [binding['path'] for binding in candidates]
    if len(set(paths)) != len(paths):
        raise ValueError('candidate_bindings contains duplicate targets')
    return deepcopy(candidates)


def rebuild_baseline(packet: dict[str, Any], manifest: dict[str, Any]) -> None:
    """Derive manifest-selected inline rules from already verified source text.

    This cannot admit a new source or refresh its bytes. The caller must bind
    every manifest entry before requesting this convenience projection.
    """
    sources = {}
    for record in packet['sources']:
        binding, raw = record['binding'], record['text']
        key = json.dumps(binding, sort_keys=True)
        if key in sources or hashlib.sha256(raw.encode()).hexdigest() != binding['sha256']:
            raise ValueError('ambiguous or stale baseline source')
        sources[key] = raw
    baseline = []
    seen = set()
    for binding in manifest['sources']:
        key = json.dumps(binding, sort_keys=True)
        if key in seen or key not in sources:
            raise ValueError(f'baseline declaration is not a unique bound source: {binding}')
        seen.add(key)
        baseline.append({'source': deepcopy(binding), 'raw': sources[key]})
    packet['source_bindings_manifest'] = deepcopy(manifest)
    packet['baseline'] = baseline


def validate_baseline_sources(packet: dict[str, Any]) -> None:
    """Reject stale auxiliary baseline text in favor of the canonical sources.

    ``baseline`` is a review convenience copy, never a second authority
    channel.  Its source binding and raw Markdown must therefore be the exact
    record already carried in ``sources``.  Packets without this optional
    convenience view remain valid for existing callers.
    """
    baseline = packet.get('baseline')
    if baseline is None:
        return
    if not isinstance(baseline, list):
        raise ValueError('baseline must be a list of canonical source copies')
    sources = packet.get('sources')
    if not isinstance(sources, list):
        raise ValueError('baseline requires canonical sources')
    for item in baseline:
        if (not isinstance(item, dict) or not isinstance(item.get('source'), dict)
                or not isinstance(item.get('raw'), str) or not item['raw'].strip()):
            raise ValueError('baseline source copy is invalid')
        matches = [record for record in sources if isinstance(record, dict)
                   and record.get('binding') == item['source']]
        if len(matches) != 1 or matches[0].get('text') != item['raw']:
            raise ValueError('baseline source/raw contradicts canonical sources')


def validated_principle_admissions(packet: dict[str, Any]) -> list[dict[str, Any]]:
    """Validate caller declarations without deciding admission or activation."""
    admissions = packet.get('principle_admissions', [])
    if not isinstance(admissions, list):
        raise ValueError('Principle admissions must be a list')
    sources = packet.get('sources', [])
    bindings = [record['binding'] for record in sources]
    paths = {binding['path'] for binding in bindings}
    candidates = validated_candidate_bindings(packet)
    candidate_paths = {binding['path'] for binding in candidates} if candidates is not None else paths
    allowlist = packet.get('authority_bindings')
    seen = set()
    for admission in admissions:
        if not isinstance(admission, dict) or admission.get('binding') not in bindings:
            raise ValueError('Principle admission needs an exact bound source')
        binding = admission['binding']
        unidentified = authority_reference(binding).startswith('source:')
        if (allowlist is not None and binding not in allowlist
                or unidentified and not isinstance(allowlist, list)):
            raise ValueError('Principle admission needs inclusion in the authority allowlist')
        if unidentified and candidates is None:
            raise ValueError('Legacy Principle admission needs explicit candidate_bindings')
        if any(not isinstance(admission.get(k), str) or not admission[k].strip()
               for k in ('reason', 'provenance')):
            raise ValueError('Principle admission needs reason and provenance')
        applicable = admission.get('applicable_to')
        if (not isinstance(applicable, list) or not applicable
                or any(not isinstance(path, str) or path not in candidate_paths for path in applicable)
                or len(set(applicable)) != len(applicable)):
            raise ValueError('Principle applicability needs distinct bound candidate paths')
        path = admission['binding']['path']
        if path in seen:
            raise ValueError('duplicate Principle admission')
        seen.add(path)
    return deepcopy(admissions)


def _resource(root: Path, path: str, role: str) -> tuple[dict[str, Any] | None, dict[str, str]]:
    relative = Path(path)
    if relative.is_absolute() or '..' in relative.parts or any(p.startswith('.env') for p in relative.parts):
        raise ValueError('unsafe context resource path')
    resolved = (root / relative).resolve()
    if not resolved.is_relative_to(root.resolve()) or any(p.startswith('.env') for p in resolved.parts):
        raise ValueError('context resource escapes admitted root or is secret')
    if not resolved.is_file():
        return None, {'state': 'missing', 'reason': f'No admitted file at {path}.'}
    if resolved.stat().st_size > 8 * 1024 * 1024:
        return None, {'state': 'invalid', 'reason': 'Context resource exceeds 8 MiB safety ceiling.'}
    raw = resolved.read_bytes()
    try:
        text = raw.decode('utf-8')
        data = tomllib.loads(text)
        if role == 'project_structure' and ('projection' in data or not isinstance(data.get('scope_units'), list)):
            raise ValueError('not authoritative Project Structure')
    except (UnicodeError, ValueError):
        return None, {'state': 'invalid', 'reason': f'{path} is not a valid admitted {role} TOML Carrier.'}
    return {'path': path, 'sha256': hashlib.sha256(raw).hexdigest(), 'text': text,
            'data': json.loads(json.dumps(data, default=str))}, {'state': 'available', 'reason': f'Bound full content from {path}.'}


def prepare_context(packet: dict[str, Any], *, root: Path | None = None,
                    resources: dict[str, str] | None = None) -> dict[str, Any]:
    """Return a fresh packet. Authority admission remains explicit caller input.

    `principle_admissions` entries need an exact source binding, applicable_to
    candidate paths, and a reason/provenance for that selection. This function
    never sets Active Status or derives identity/tier from a filename.
    """
    output = deepcopy(packet)
    output['entity_index'] = []
    output['relation_index'] = []
    output['applicable_principles'] = []
    output['preflight'] = {}
    output['resources'] = {}
    admissions = validated_principle_admissions(output)
    authority_bindings = output.get('authority_bindings')
    for record in output.get('sources', []):
        raw, binding = record['text'], record['binding']
        if hashlib.sha256(raw.encode()).hexdigest() != binding['sha256']:
            raise ValueError('source content differs from its binding')
        props = metadata(raw)
        target = props.get('subjects', {}).get('governs') if isinstance(props.get('subjects'), dict) else None
        active = str(props.get('status', '')).lower() == 'active'
        admitted = authority_bindings is None or binding in authority_bindings
        if active and admitted and isinstance(target, str):
            output['entity_index'].append({'entity': target, 'binding': binding, 'body': markdown(raw),
                'admission': 'retrieval_candidate_not_definition_proof'})
            if 'relation' in target.lower() or re.fullmatch(r'[A-Z]+(?:_[A-Z]+)+', target):
                output['relation_index'].append({'entity': target, 'binding': binding, 'body': markdown(raw)})
        for admission in admissions:
            if (admission.get('binding') == binding and admission.get('reason')
                    and admission.get('applicable_to') and admission.get('provenance')):
                output['applicable_principles'].append({'binding': binding, 'text': raw,
                    'applicable_to': admission['applicable_to'], 'reason': admission['reason'],
                    'provenance': admission['provenance'], 'reference': authority_reference(binding)})
    validate_baseline_sources(output)
    output['preflight']['principles'] = {
        'state': 'available' if output['applicable_principles'] else 'missing',
        'reason': 'Explicit bound Principle applicability supplied.' if output['applicable_principles']
                  else 'No explicit bound Principle admission and candidate applicability supplied; legacy filenames do not establish these facts.'}
    for role, path in (resources or {}).items():
        if root is None:
            raise ValueError('explicit root required for resources')
        value, state = _resource(root, path, role)
        output['preflight'][role] = state
        if value is not None:
            output['resources'][role] = value
    output['context_builder_version'] = 1
    return output


def lookup(packet: dict[str, Any], query: str) -> list[dict[str, Any]]:
    """Rank candidates without choosing a canonical Entity for the reviewer."""
    normalized = query.strip().casefold()
    if not normalized:
        raise ValueError('empty lookup query')
    found = [row for row in packet['entity_index']
             if normalized in row['entity'].casefold() or normalized in row['body'].casefold()]
    return sorted(found, key=lambda row: (row['entity'].casefold() != normalized,
        normalized not in row['entity'].casefold(), row['entity'], row['binding']['path']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Query the frozen Entity retrieval index, not the live repository.')
    parser.add_argument('--context', type=Path, required=True)
    parser.add_argument('--query', required=True)
    args = parser.parse_args()
    print(json.dumps(lookup(json.loads(args.context.read_text()), args.query), ensure_ascii=False, indent=2))
