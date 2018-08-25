# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, replacer

REPLACE = {
    ACUTE + 'E': 'Є',
    ACUTE + 'U': 'Ю',
    ACUTE + 'A': 'Я',
    'JE': 'Є',
    'JU': 'Ю',
    'JA': 'Я',
}


def _replace():
    replace = REPLACE.copy()
    replace.update({i.title(): o for i, o in REPLACE.items()})
    replace.update({i.lower(): o.lower() for i, o in REPLACE.items()})
    return replacer(replace)


apply = applier(_replace())
