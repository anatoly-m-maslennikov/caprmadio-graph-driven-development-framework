"""Explicit caller-selected ordering of canonical Atom IDs, not graph order."""
from __future__ import annotations

import re
from typing import Any

_ATOM_ID = re.compile(r'([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*)-([0-9]{1,100})')
_POLICY_FIELDS = {'key', 'direction', 'source', 'instruction', 'provenance'}


def validate_ordering_policy(value: Any) -> dict[str, str] | None:
    """Validate caller input; a provenance string does not establish permission."""
    if value is None:
        return None
    if (not isinstance(value, dict) or set(value) != _POLICY_FIELDS
            or any(not isinstance(v, str) or not v.strip() for v in value.values())
            or value['key'] != 'atom_id' or value['direction'] != 'ascending'
            or value['source'] != 'operator_input'):
        raise ValueError('requires explicit caller-bound Atom-ID ordering policy')
    return dict(value)


def atom_id_key(value: Any) -> tuple[str, int, str]:
    """Use namespace/role and numeric serial, then exact ID for padding ties.

    All components come from the Atom ID itself. No path, Summary or Revision
    is read. Unsupported reference forms are not converted or guessed.
    """
    match = _ATOM_ID.fullmatch(value) if isinstance(value, str) else None
    if match is None:
        raise ValueError('ordering requires a canonical Atom ID, not a locator or revision reference')
    return match[1], int(match[2]), value


def ordered_atom_ids(values: Any) -> list[str]:
    """Return a permutation only; never drop duplicate or malformed references."""
    if not isinstance(values, list):
        raise ValueError('relation targets must be a list')
    for value in values:
        atom_id_key(value)
    if len(set(values)) != len(values):
        raise ValueError('duplicate Atom ID targets require a separate repair')
    return sorted(values, key=atom_id_key)
