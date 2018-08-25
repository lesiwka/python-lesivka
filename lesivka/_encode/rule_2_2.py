# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, replacer, translator

IN, OUT = 'ЄЮЯ', 'EUA'
AFTER = 'БВГҐДЖЗКЛМНПРСТФХЦЧШЩ'

TRANSLATE = {
    'Є': 'JE',
    'Ю': 'JU',
    'Я': 'JA',
}


def _step1():
    replace = {}
    for c in AFTER + AFTER.lower():
        for i, o in zip(IN + IN.lower(), OUT + OUT.lower()):
            replace[c + i] = c + ACUTE + o

    return replacer(replace)


def _step2():
    translate = TRANSLATE.copy()
    translate.update({i.lower(): o.lower() for i, o in TRANSLATE.items()})
    return translator(translate)


step1, step2 = _step1(), _step2()

apply = applier(step1, step2)
