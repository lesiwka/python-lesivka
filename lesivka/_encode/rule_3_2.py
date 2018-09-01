# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, replacer

PREFIXES = (
    'ВІД',
    'НАД',
    'ОД',
    'ПЕРЕД',
    'ПІД',
    'ПОНАД',
    'ПРЕД',
    'СЕРЕД',
)

REPLACE = {
    'ДЖ': 'Đ',
    'ДЗ': 'Ƶ',
}


def new_affricates():
    replace = REPLACE.copy()
    replace.update({i.title(): o for i, o in REPLACE.items()})
    replace.update({i.lower(): o.lower() for i, o in REPLACE.items()})

    _replacer = replacer(replace)

    def _replace(text):
        for prefix in PREFIXES:
            if text.upper().startswith(prefix):
                index = len(prefix)
                return text[:index] + _replacer(text[index:])

        return _replacer(text)

    return _replace


do = new_affricates()
