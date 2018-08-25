# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, translator

IN, OUT = 'Щ', 'ŠČ'

apply = applier(translator({IN: OUT, IN.lower(): OUT.lower()}))
