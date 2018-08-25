# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, replacer

IN, OUT = 'I', 'І'
AFTER = 'AEIOU'


def _step2():
    replace = {}
    for i, o in zip(IN + IN.lower(), OUT + OUT.lower()):
        for c in AFTER + AFTER.lower():
            replace[c + i] = c + o

    return replacer(replace)


def _step3():
    replace = {i: o for i, o in zip(IN + IN.lower(), OUT + OUT.lower())}

    def _replace(text):
        if text.startswith(tuple(replace)):
            return replace[text[0]] + text[1:]
        return text

    return _replace


step1 = replacer({ACUTE + i: o for i, o in
                  zip(IN + IN.lower(), OUT + OUT.lower())})
step2 = _step2()
step3 = _step3()

apply = applier(step1, step2, step3)
