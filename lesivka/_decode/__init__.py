# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import (
    preprocess,
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
from ..diacritics import ACUTE, CARON
from ..utils import Converter, applier

ORDER = (
    preprocess,
    rule_3_1,
    rule_2_1,
    rule_2_2,
    rule_1_6,
    rule_1_7,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_3_2,
)

LAT = 'ABCČDĐEFGHIJKLMNOPRSŠTUVXZŽƵ' + ACUTE + CARON + 'ĆĹŃŔŚŹǴḰḾṔ'

convert = applier(*(rule.convert for rule in ORDER))
decode = Converter('([^\w%s]+)' % (ACUTE + CARON), LAT, convert)
