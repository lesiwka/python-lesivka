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


def get_step1():
    data = {}
    for c in AFTER + AFTER.lower():
        for i, o in zip(IN + IN.lower(), OUT + OUT.lower()):
            data[c + i] = c + ACUTE + o

    return replacer(data)


def get_step2():
    data = TRANSLATE.copy()
    data.update({i.lower(): o.lower() for i, o in TRANSLATE.items()})
    return translator(data)


convert = applier(get_step1(), get_step2())
