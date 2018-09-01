# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, replacer, translator

IN, OUT = 'І', 'I'
AFTER = 'AEIOU' + ACUTE


def _step2():
    replace = zip(AFTER + AFTER.lower(),
                  OUT * len(AFTER) + OUT.lower() * len(AFTER))
    _replacer = replacer({c + ACUTE + i: c + i for c, i in replace})

    def _strip_replace(text):
        text = _replacer(text)
        return text.lstrip(ACUTE)

    return _strip_replace


step1 = translator({IN: ACUTE + OUT, IN.lower(): ACUTE + OUT.lower()})

do = applier(step1, _step2())
