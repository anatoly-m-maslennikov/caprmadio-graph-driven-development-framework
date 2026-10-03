"""Admit a repair candidate for independent evaluation, never for source mutation.

This is a pure safety gate. It does not prove preservation of meaning, allocate
identities, write files, archive history, or authorize a commit.
"""
from __future__ import annotations

import hashlib
from datetime import datetime
from pathlib import PurePosixPath
import re
from typing import Any

from context_builder import body_section_texts, markdown, metadata
from evaluation_contract import summarize_evaluations
from review_evidence import ReviewContext, probability, text


# Fixer operations are not the canonical semantic change classes returned by
# CA-O-067 under CA-R-1432. In particular, a split is a replacement class.
CHANGE_CLASSES = {
    'formatting': ('carrier_only',),
    # A recoding is the deliberately narrow carrier-only path change: it may
    # remove an invalid R/M/D role echo and rename the carrier accordingly.
    # It is not a general metadata-edit escape hatch.
    'recoding': ('carrier_only',),
    'revision': ('refinement', 'semantic_revision'),
    'replacement': ('replacement',),
    'split': ('replacement',),
}


def _path(value: Any) -> str:
    if not isinstance(value, str) or not value or '\\' in value or '\0' in value:
        raise ValueError('invalid proposal path')
    path = PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts or str(path) != value or path.suffix != '.md':
        raise ValueError('proposal path must be canonical and relative')
    if any(p.startswith('.env') for p in path.parts):
        raise ValueError('secret path is outside repair admission')
    return value


def _summary(raw: str) -> str:
    matches = [body for address, body in body_section_texts(raw).items()
               if address.endswith(':# Summary')]
    if len(matches) != 1:
        raise ValueError('Summary needs an unambiguous body section')
    result = '\n'.join(matches[0].splitlines()[1:]).strip()
    if not result:
        raise ValueError('Summary cannot be empty')
    return result


def _same_summary_value(before: str, after: str) -> bool:
    """Admit only lossless strong-markup changes, never changed Summary words.

    CA-R-1432 distinguishes the value from its serialization. This deliberately
    narrow comparison is not a general Markdown renderer: links, code, HTML,
    escapes and unmatched/nested emphasis still require separate handling.
    An independent semantic change assessment remains mandatory.
    """
    if before == after:
        return True
    def value(raw: str) -> str | None:
        if any(char in raw for char in ('\\', '`', '[', ']', '<', '>')):
            return None
        result = re.sub(r'\*\*(\S(?:[^*\r\n]*?\S)?)\*\*', r'\1', raw)
        return None if '*' in result else result
    old, new = value(before), value(after)
    return old is not None and new is not None and old == new


def _permission(proposal: dict[str, Any], permission: dict[str, Any]) -> set[str]:
    dispositions = ('formatting', 'recoding', 'revision', 'replacement', 'split')
    disposition = proposal.get('disposition')
    admitted = permission.get('dispositions')
    if not isinstance(admitted, list) or any(item not in dispositions for item in admitted):
        raise ValueError('permission dispositions must be an exact list')
    if disposition not in dispositions or disposition not in admitted:
        raise ValueError('repair disposition lacks explicit permission')
    if not text(permission.get('provenance')) or not isinstance(permission.get('paths'), list):
        raise ValueError('missing caller permission and provenance')
    allowed = {_path(p) for p in permission['paths']}
    if _path(proposal['source']['path']) not in allowed:
        raise ValueError('source path is outside caller permission')
    return allowed


def _resolutions(evaluation: dict[str, Any], proposal: dict[str, Any]) -> None:
    expected = {(row['id'], i) for row in evaluation['checks'] for i, _ in enumerate(row['findings'])}
    resolutions = proposal.get('resolutions')
    if not isinstance(resolutions, list):
        raise ValueError('missing finding resolutions')
    resolved = []
    for resolution in resolutions:
        if not isinstance(resolution, dict) or not text(resolution.get('reason')):
            raise ValueError('unsupported finding resolution')
        if not isinstance(resolution.get('check_id'), str) or type(resolution.get('finding_index')) is not int:
            raise ValueError('invalid finding reference')
        resolved.append((resolution['check_id'], resolution['finding_index']))
    if len(resolved) != len(set(resolved)) or set(resolved) != expected or not expected:
        raise ValueError('every finding needs exactly one supported resolution')
    preservation = proposal.get('preservation')
    if not isinstance(preservation, list) or not preservation or not all(text(p) for p in preservation):
        raise ValueError('missing information-preservation explanation')


def _outputs(proposal: dict[str, Any], allowed: set[str]) -> list[dict[str, Any]]:
    outputs = proposal.get('outputs')
    if not isinstance(outputs, list) or not outputs or any(not isinstance(o, dict) for o in outputs):
        raise ValueError('missing full proposed outputs')
    if (proposal['disposition'] == 'split' and len(outputs) < 2) or (proposal['disposition'] != 'split' and len(outputs) != 1):
        raise ValueError('output count contradicts disposition')
    paths = [_path(o.get('path')) for o in outputs]
    if len(paths) != len(set(paths)) or any(p not in allowed for p in paths):
        raise ValueError('output paths duplicate or lack exact permission')
    return outputs


def _updated_at(raw: str) -> str:
    value = metadata(raw).get('updated_at')
    if not isinstance(value, str):
        raise ValueError('updated_at must be a timezone-bearing timestamp')
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as error:
        raise ValueError('updated_at must be a timezone-bearing timestamp') from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError('updated_at must be a timezone-bearing timestamp')
    return value


def _timestamp_normalized_header(header: str) -> str:
    normalized, count = re.subn(r'(?m)^updated_at:[^\r\n]*', 'updated_at: <REFRESHED>', header)
    if count != 1:
        raise ValueError('updated_at must occur exactly once in frontmatter')
    return normalized


def _refreshes_updated_at(original: str, candidate: str) -> None:
    original_value = _updated_at(original)
    candidate_value = _updated_at(candidate)
    if candidate_value == original_value:
        raise ValueError('updated_at must refresh on every edit')
    if datetime.fromisoformat(candidate_value.replace('Z', '+00:00')) <= datetime.fromisoformat(original_value.replace('Z', '+00:00')):
        raise ValueError('updated_at must advance on every edit')


def _recoding_identity(output: dict[str, Any], before: dict[str, Any], original: str) -> None:
    old_props = metadata(original)
    new_props = metadata(output['text'])
    role = old_props.get('content_role')
    if role not in ('Requirement', 'Method', 'Delivery') or old_props.get('type') != role:
        raise ValueError('recoding requires an ordinary R/M/D role-echo Type')
    _refreshes_updated_at(original, output['text'])
    expected_props = dict(old_props)
    del expected_props['type']
    expected_props.pop('updated_at', None)
    actual_props = dict(new_props)
    actual_props.pop('updated_at', None)
    if actual_props != expected_props:
        raise ValueError('recoding may only remove the role-echo Type metadata')
    old_header = original.removesuffix(markdown(original))
    new_header = output['text'].removesuffix(markdown(output['text']))
    # Semantic YAML equality alone permits unrelated comment, quoting, ordering
    # or whitespace edits. Only a standalone scalar Type field is supported.
    pattern = rf'''(?m)^type:[ \t]*(?:{role}|"{role}"|'{role}')[ \t]*\r?\n'''
    expected_header, count = re.subn(pattern, '', old_header)
    if count != 1 or _timestamp_normalized_header(new_header) != _timestamp_normalized_header(expected_header):
        raise ValueError('recoding must preserve remaining frontmatter bytes')
    if markdown(output['text']) != markdown(original):
        raise ValueError('recoding must preserve the complete Markdown body')
    if output['version'] != before['version']:
        raise ValueError('recoding must preserve version')


def _formatting_identity(output: dict[str, Any], before: dict[str, Any], original: str) -> None:
    old_header = original.removesuffix(markdown(original))
    new_header = output['text'].removesuffix(markdown(output['text']))
    _refreshes_updated_at(original, output['text'])
    if (output['version'] != before['version']
            or _timestamp_normalized_header(old_header) != _timestamp_normalized_header(new_header)):
        raise ValueError('formatting must preserve version and all non-timestamp frontmatter')


def _removes_role_echo(old_props: dict[str, Any], new_props: dict[str, Any]) -> bool:
    role = old_props.get('content_role')
    return (role in ('Requirement', 'Method', 'Delivery')
            and old_props.get('type') == role
            and new_props.get('content_role') == role and 'type' not in new_props)


def _role_echo_path(output_path: str, source_path: str, role: str) -> bool:
    """Elide only the basename's final Type token before its first delimiter."""
    source_path = PurePosixPath(source_path)
    prefix, delimiter, slug = source_path.name.partition('--')
    token = '-' + role.upper()
    return bool(delimiter and prefix.endswith(token)
                and output_path == str(source_path.with_name(prefix[:-len(token)] + '--' + slug)))


def _identity(output: dict[str, Any], before: dict[str, Any], original: str,
              disposition: str, classification: str) -> None:
    _updated_at(output['text'])
    if disposition in ('replacement', 'split'):
        _refreshes_updated_at(original, output['text'])
        if output['atom_id'] == before['atom_id']:
            raise ValueError('replacement/split requires new identities')
        if output['path'] == before['path']:
            raise ValueError('successor Carrier must not reuse its predecessor path')
        return
    if output['atom_id'] != before['atom_id']:
        raise ValueError('identity-preserving correction changed identity')
    old_props, new_props = metadata(original), metadata(output['text'])
    removes_echo = _removes_role_echo(old_props, new_props)
    if output['path'] != before['path']:
        if (disposition not in ('recoding', 'revision') or not removes_echo
                or not _role_echo_path(output['path'], before['path'], old_props['content_role'])):
            raise ValueError('identity-preserving path change requires exact role-echo Type elision')
    if not _same_summary_value(_summary(original), _summary(output['text'])):
        raise ValueError('Summary change requires replacement')
    if (disposition == 'revision' and not removes_echo
            and ('type' in old_props, old_props.get('type')) != ('type' in new_props, new_props.get('type'))):
        raise ValueError('Type change requires replacement except ordinary role-echo elision')
    if disposition == 'formatting':
        _formatting_identity(output, before, original)
    elif disposition == 'recoding':
        _recoding_identity(output, before, original)
    elif classification == 'refinement':
        _refreshes_updated_at(original, output['text'])
        if output['version'] != before['version']:
            raise ValueError('refinement must preserve version')
    elif classification == 'semantic_revision':
        _refreshes_updated_at(original, output['text'])
        if output['version'] != before['version'] + 1:
            raise ValueError('semantic revision must increment version once')
    else:
        raise ValueError('revision requires an admitted semantic change class')


def _output_binding(output: dict[str, Any]) -> dict[str, Any]:
    raw = output.get('text')
    if not isinstance(raw, str) or not raw.strip() or not text(output.get('atom_id')) or type(output.get('version')) is not int or output['version'] < 1:
        raise ValueError('invalid proposed Carrier or identity')
    props = metadata(raw)
    if (props.get('atom_id') != output['atom_id'] or type(props.get('version')) is not int
            or props.get('version') != output['version']):
        raise ValueError('proposed binding is missing or contradicts frontmatter')
    return {k: output[k] for k in ('path', 'atom_id', 'version')} | {
        'sha256': hashlib.sha256(raw.encode()).hexdigest()}


def _candidate_bindings(proposal: dict[str, Any], outputs: list[dict[str, Any]],
                        context: ReviewContext) -> list[dict[str, Any]]:
    before = proposal['source']
    original = context.source_text(before)
    old_summary = _summary(original)
    if proposal.get('before_summary') != old_summary:
        raise ValueError('declared before Summary differs from body')
    ids = []
    bindings = []
    for output in outputs:
        binding = _output_binding(output)
        new_summary = _summary(output['text'])
        if len(outputs) == 1 and proposal.get('after_summary') != new_summary:
            raise ValueError('declared after Summary differs from body')
        if output['text'] == original:
            raise ValueError('repair proposal makes no progress')
        ids.append(output['atom_id'])
        bindings.append(binding)
    if len(ids) != len(set(ids)):
        raise ValueError('successors must have distinct identities')
    return bindings


def _preflight(proposal: dict[str, Any], bindings: list[dict[str, Any]], *,
               context: ReviewContext, preflight: Any) -> str:
    """Check caller-supplied evidence bindings without claiming it is true."""
    if not isinstance(preflight, dict):
        raise ValueError('missing caller admission preflight')
    if 'identity_assessment' in proposal:
        raise ValueError('proposal cannot self-attest a CA-O-067 identity assessment')
    if (preflight.get('source') != proposal['source']
            or preflight.get('context_sha256') != context.sha256
            or not text(preflight.get('provenance'))):
        raise ValueError('caller preflight is not bound to this source and context')
    attempt, budget = preflight.get('attempt'), preflight.get('retry_budget')
    if (type(attempt) is not int or type(budget) is not int or attempt < 0
            or budget < 0 or attempt > budget):
        raise ValueError('invalid repair attempt or retry budget')

    assessment = preflight.get('identity_assessment')
    if not isinstance(assessment, dict):
        raise ValueError('missing caller CA-O-067 identity assessment')
    if (assessment.get('source') != proposal['source']
            or assessment.get('context_sha256') != context.sha256
            or assessment.get('classification') not in CHANGE_CLASSES[proposal['disposition']]
            or assessment.get('outputs') != bindings
            or not text(assessment.get('provenance'))):
        raise ValueError('identity assessment is not bound to this proposal')

    if proposal['disposition'] not in ('replacement', 'split'):
        return assessment['classification']
    successors = preflight.get('successor_reservations')
    if not isinstance(successors, dict):
        raise ValueError('missing caller successor reservations')
    if (successors.get('bindings') != bindings
            or not text(successors.get('provenance'))
            or not text(successors.get('history_reference_plan'))):
        raise ValueError('successor reservations or history plan are not bound')
    return assessment['classification']


def admit_proposal(evaluation: dict[str, Any], proposal: dict[str, Any], *,
                   context: ReviewContext, permission: dict[str, Any],
                   preflight: dict[str, Any] | None = None) -> dict[str, Any]:
    """Admit a preview, not a write, from caller-supplied bound evidence.

    The caller attests freshness, CA-O-067 classification, reservations and
    retry state. This gate verifies only their agreement with this proposal;
    independent evaluation and the source writer still establish correctness.
    """
    if context.report_contract not in (5, 6):
        raise ValueError('repair admission requires report contract 5 or 6')
    summarize_evaluations([evaluation], context=context)
    if proposal.get('source') != evaluation['source'] or proposal.get('context_sha256') != context.sha256:
        raise ValueError('proposal is not bound to this source and context')
    if evaluation['coverage_gaps']:
        return {'result': 'blocked', 'source_mutation_permitted': False,
                'reasons': evaluation['coverage_gaps']}
    confidence = proposal.get('confidence')
    if not probability(confidence) or confidence < context.confidence_threshold:
        raise ValueError('repair confidence below caller threshold or invalid')
    allowed = _permission(proposal, permission)
    _resolutions(evaluation, proposal)
    outputs = _outputs(proposal, allowed)
    bindings = _candidate_bindings(proposal, outputs, context)
    classification = _preflight(proposal, bindings, context=context, preflight=preflight)
    original = context.source_text(proposal['source'])
    for output in outputs:
        if context.report_contract == 6:
            _local_repair_boundary(proposal, output, original)
        _identity(output, proposal['source'], original, proposal['disposition'], classification)
    return {'result': 'candidate', 'source_mutation_permitted': False,
            'source': proposal['source'], 'context_sha256': context.sha256, 'outputs': bindings,
            'next': ('Independent local evaluation, information preservation, freshness and history before mutation.'
                     if context.report_contract == 6 else
                     'Independent full evaluation, freshness, history and affected-reference checks before mutation.')}


def _local_repair_boundary(proposal: dict[str, Any], output: dict[str, Any], original: str) -> None:
    """Preserve graph targets while allowing unambiguous Carrier-shape repairs."""
    if proposal['disposition'] in ('replacement', 'split') or output['path'] != proposal['source']['path']:
        raise ValueError('identity-changing or outside-path repairs need a separate authorized run')

    def values(value: Any) -> frozenset[str]:
        if value is None:
            return frozenset()
        if isinstance(value, str) and value:
            return frozenset([value])
        if isinstance(value, list) and all(isinstance(v, str) and v for v in value):
            return frozenset(value)
        raise ValueError('ambiguous graph target encoding cannot be repaired in atom_local')

    def targets(raw: str) -> tuple[Any, Any]:
        props = metadata(raw)
        subjects, relations = props.get('subjects', {}), props.get('relations', {})
        if (not isinstance(subjects, dict) or not isinstance(relations, dict)
                or set(subjects) - {'governs', 'depends_on'}):
            raise ValueError('ambiguous graph target encoding cannot be repaired in atom_local')
        return ((values(subjects.get('governs')), values(subjects.get('depends_on'))),
                {kind: values(refs) for kind, refs in relations.items()})

    if targets(original) != targets(output['text']):
        raise ValueError('atom_local repairs must preserve Subject and relation targets')
