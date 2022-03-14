# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from ..diacritics import APOSTROPHES


def get_convert():
    pattern = re.compile(r'(\w)[%s](\w)' % APOSTROPHES, re.UNICODE)

    def _(word):
        return word.re_replace(pattern, "")

    return _


convert = get_convert()
