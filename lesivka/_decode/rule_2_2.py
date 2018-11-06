# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import replace

REPLACE = {
    ACUTE + 'E': 'Є',
    ACUTE + 'U': 'Ю',
    ACUTE + 'A': 'Я',
    'JE': 'Є',
    'JU': 'Ю',
    'JA': 'Я',
}


def get_convert():
    data = REPLACE.copy()
    data.update({i.title(): o for i, o in REPLACE.items()})
    data.update({i.lower(): o.lower() for i, o in REPLACE.items()})
    return replace(data)


convert = get_convert()
