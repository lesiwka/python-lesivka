# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import replace

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


def get_convert():
    data = REPLACE.copy()
    data.update({i.title(): o for i, o in REPLACE.items()})
    data.update({i.lower(): o.lower() for i, o in REPLACE.items()})

    repl = replace(data)

    def convert(text):
        for prefix in PREFIXES:
            if text.upper().startswith(prefix):
                index = len(prefix)
                return text[:index] + repl(text[index:])

        return repl(text)

    return convert


convert = get_convert()
