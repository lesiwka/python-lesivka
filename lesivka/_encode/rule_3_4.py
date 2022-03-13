# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import product

from ..utils import applier, replacer

ZERO_VOWEL = "\uee76"
ZERO_CONSONANT = "\uff63"

AFTER = ZERO_VOWEL + "AEYIOU"
BEFORE = ZERO_CONSONANT + "BVHGDZKLMNPRSTFXCŽČŠĐƵ"


def add_zero_letters(text):
    return ZERO_VOWEL + text + ZERO_CONSONANT


def get_convert():
    after = AFTER + AFTER.lower()
    before = BEFORE + BEFORE.lower()
    data = {
        "".join(i): "".join(o)
        for i, o in zip(
            product(after, "vV", before), product(after, "wW", before)
        )
    }
    return replacer(data)


def strip_zero_letters(text):
    return text.strip(ZERO_VOWEL + ZERO_CONSONANT)


convert = applier(add_zero_letters, get_convert(), strip_zero_letters)
