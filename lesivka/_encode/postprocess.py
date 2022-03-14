# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE


def convert(word):
    return word.lstrip(ACUTE)
