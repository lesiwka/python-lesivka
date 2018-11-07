# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import replacer

AFTER = 'BVHGDZKLMNPRSTFXC' + 'ŽČŠ'

convert = replacer({
    i + o: i + "'" + o for i, o in
    zip(AFTER * 2 + AFTER.lower() * 2,
        ('J' * len(AFTER) + 'j' * len(AFTER)) * 2)
})
