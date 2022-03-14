# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..ascii import deasciilator
from ..diacritics import ACUTE, APOSTROPHES, CARON
from ..utils import Converter, applier
from . import (
    postprocess,
    preprocess,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_6,
    rule_1_7,
    rule_2_2,
    rule_3_1,
    rule_3_2,
)

ORDER = (
    preprocess,
    rule_3_1,
    rule_2_2,
    rule_1_6,
    rule_1_7,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_3_2,
    postprocess,
)

LAT = "ABCČDĐEFGHIJKLMNOPRSŠTUVXYZŽƵ" + ACUTE + CARON + "ĆĹŃŔŚŹǴḰḾṔ"


def decode(text, no_diacritics=False):
    converters = [rule.convert for rule in ORDER]
    split_chars = ACUTE + CARON
    valid = LAT

    if no_diacritics:
        converters.insert(0, deasciilator)
        split_chars += APOSTROPHES
        valid += "QW'"

    split = r"([^\w%s]+)" % split_chars
    return Converter(split, valid, applier(*converters))(text)
