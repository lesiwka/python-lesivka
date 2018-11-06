# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import replace

AFTER = 'BVHGDZKLMNPRSTFXC' + 'ŽČŠ'

convert = replace({
    i + o: i + "'" + o for i, o in
    zip(AFTER + AFTER.lower(), 'J' * len(AFTER) + 'j' * len(AFTER))
})
