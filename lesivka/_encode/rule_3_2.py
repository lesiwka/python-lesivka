# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import replacer

PREFIXES = (
    'ВІД',
    'НАД',
    'ОД',
    'ПЕРЕД',
    'ПІД',
    'ПОНАД',
    'ПОПІД',
    'ПРЕД',
    'СЕРЕД',
)

REPLACE = {
    'ДЖ': 'Đ',
    'ДЗ': 'Ƶ',
}


def get_convert():
    data = REPLACE.copy()
    data.update({i.title(): o for i, o in REPLACE.items()})
    data.update({i.lower(): o.lower() for i, o in REPLACE.items()})

    repl = replacer(data)

    def _(text):
        for prefix in PREFIXES:
            if text.upper().startswith(prefix):
                index = len(prefix)
                return text[:index] + repl(text[index:])

        return repl(text)

    return _


convert = get_convert()
