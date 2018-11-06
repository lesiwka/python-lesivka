# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, replace

IN, OUT = 'I', 'І'
AFTER = 'AEIOU'


def get_step2():
    data = {}
    for i, o in zip(IN + IN.lower(), OUT + OUT.lower()):
        for c in AFTER + AFTER.lower():
            data[c + i] = c + o

    return replace(data)


def get_step3():
    data = {i: o for i, o in zip(IN + IN.lower(), OUT + OUT.lower())}

    def convert(text):
        if text.startswith(tuple(data)):
            return data[text[0]] + text[1:]
        return text

    return convert


step1 = replace({ACUTE + i: o for i, o in
                 zip(IN + IN.lower(), OUT + OUT.lower())})

convert = applier(step1, get_step2(), get_step3())
