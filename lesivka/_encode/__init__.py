# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..ascii import asciilator
from ..diacritics import ACUTE, APOSTROPHES
from ..utils import Converter, applier
from . import (
    abbr,
    postprocess,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_7,
    rule_2_2,
    rule_3_1,
    rule_3_2,
    rule_3_4,
)

ORDER = (
    abbr,
    rule_2_2,
    rule_3_2,
    rule_1_1,
    rule_3_4,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_7,
    rule_3_1,
    postprocess,
)

CYR = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' + ACUTE + APOSTROPHES


def encode(text, no_diacritics=False):
    converters = [rule.convert for rule in ORDER]
    if no_diacritics:
        converters.append(asciilator)

    split = r"([^\w%s]+)" % (ACUTE + APOSTROPHES)
    return Converter(split, CYR, applier(*converters))(text)
