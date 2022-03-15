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

EXCLUDES = (
    "ПЕРЕДЗВЕН",
    "ПЕРЕДЗВІН",
    "ПЕРЕДЗВОН",
    "ПЕРЕДЗИЖЧ",
)


def get_convert():
    data = REPLACE.copy()
    data.update({i.title(): o for i, o in REPLACE.items()})
    data.update({i.lower(): o.lower() for i, o in REPLACE.items()})

    repl = replacer(data)

    def _(word):
        text = word.word.upper()
        for prefix in PREFIXES:
            if text.startswith(prefix) and not text.startswith(EXCLUDES):
                index = len(prefix)
                return word.apply(repl, index)

        return repl(word)

    return _


convert = get_convert()
