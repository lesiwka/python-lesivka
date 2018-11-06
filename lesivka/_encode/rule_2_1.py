# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, replacer, translator

IN, OUT = 'І', 'I'
AFTER = 'AEIOU' + ACUTE


def get_step2():
    data = zip(AFTER + AFTER.lower(),
               OUT * len(AFTER) + OUT.lower() * len(AFTER))
    repl = replacer({c + ACUTE + i: c + i for c, i in data})

    def convert(text):
        text = repl(text)
        return text.lstrip(ACUTE)

    return convert


step1 = translator({IN: ACUTE + OUT, IN.lower(): ACUTE + OUT.lower()})

convert = applier(step1, get_step2())
