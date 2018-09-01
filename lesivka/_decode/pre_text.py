# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE, CARON
from ..utils import applier, replacer

COMBININGS = {
    'C' + CARON: 'Č',
    'S' + CARON: 'Š',
    'Z' + CARON: 'Ž',
    'Ć': 'C' + ACUTE,
    'Ĺ': 'L' + ACUTE,
    'Ń': 'N' + ACUTE,
    'Ŕ': 'R' + ACUTE,
    'Ś': 'S' + ACUTE,
    'Ź': 'Z' + ACUTE,
    'Ǵ': 'G' + ACUTE,
    'Ḱ': 'K' + ACUTE,
    'Ḿ': 'M' + ACUTE,
    'Ṕ': 'P' + ACUTE,
}


def fix_combinings():
    combinings = COMBININGS.copy()

    for i, o in COMBININGS.items():
        combinings[i.lower()] = o.lower()

    return replacer(combinings)


do = fix_combinings()
