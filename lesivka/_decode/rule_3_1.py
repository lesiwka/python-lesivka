# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, replacer

AFTER = 'BVHGDZKLMNPRSTFXC' + 'ŽČŠ'

apply = applier(replacer({
    i + o: i + "'" + o for i, o in
    zip(AFTER + AFTER.lower(), 'J' * len(AFTER) + 'j' * len(AFTER))
}))
