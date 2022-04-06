# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import product

from ..diacritics import ACUTE, APOSTROPHES
from ..utils import applier, replacer

ZERO_VOWEL = "\uee76"
ZERO_CONSONANT = "\uff63"

AFTER = ZERO_VOWEL + "AEYIOU"
_BEFORE = "БВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ"
BEFORE = _BEFORE + ZERO_CONSONANT + APOSTROPHES
BEFORE_NEXT = _BEFORE + "ЄЇЮЯ"


def add_zero_letters(word):
    suffix = ZERO_CONSONANT

    if word.continues():
        next_word = word.get_next()
        if next_word:
            next_word_value = next_word.word
            if (
                next_word_value
                and next_word_value[0].upper() not in BEFORE_NEXT
            ):
                suffix = ZERO_VOWEL

    return ZERO_VOWEL + word + suffix


def get_convert():
    after = AFTER + AFTER.lower()
    after += "".join(c + ACUTE for c in after)
    before = BEFORE + BEFORE.lower()
    data = {
        "".join(i): "".join(o)
        for i, o in zip(
            product(after, "вВ", before), product(after, "wW", before)
        )
    }
    repl = replacer(data)

    def _(word):
        if word.abbr:
            return word
        return repl(word)

    return _


def strip_zero_letters(word):
    return word.strip(ZERO_VOWEL + ZERO_CONSONANT)


convert = applier(add_zero_letters, get_convert(), strip_zero_letters)
