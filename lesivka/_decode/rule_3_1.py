# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import replacer

AFTER = 'BVHGDZKLMNPRSTFXC' + 'ŽČŠ'

convert = replacer({
    i + o: i + "'" + o for i, o in
    zip(AFTER + AFTER.lower(), 'J' * len(AFTER) + 'j' * len(AFTER))
})
