# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import (
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_6,
    rule_1_7,
    rule_2_1,
    rule_2_2,
    rule_3_1,
    rule_3_2,
)
from ..diacritics import ACUTE, APOSTROPHES
from ..utils import Converter, applier

ORDER = (
    rule_1_6,
    rule_2_2,
    rule_3_2,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_7,
    rule_2_1,
    rule_3_1,
)

CYR = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' + ACUTE + APOSTROPHES

convert = applier(*(rule.convert for rule in ORDER))
encode = Converter('([^\w%s]+)' % (ACUTE + APOSTROPHES), CYR, convert)
