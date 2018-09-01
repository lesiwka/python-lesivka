# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from ..diacritics import APOSTROPHES


def remove_apostrophe():
    pattern = re.compile('(\w)([%s])(\w)' % APOSTROPHES, re.UNICODE)

    def remove(text):
        print(pattern.split(text))
        return ''.join(t for t in pattern.split(text) if t not in APOSTROPHES)

    return remove


do = remove_apostrophe()
