# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, replacer, translator

IN, OUT = 'І', ACUTE + 'I'
AFTER = 'AEIOU'


def _step2():
    _replacer = replacer({c + ACUTE: c for c in AFTER + AFTER.lower()})

    def _strip_replace(text):
        text = _replacer(text)
        return text.lstrip(ACUTE)

    return _strip_replace


step1 = translator({IN: OUT, IN.lower(): OUT.lower()})
step2 = _step2()

apply = applier(step1, step2)
