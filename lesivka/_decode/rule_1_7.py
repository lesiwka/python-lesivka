# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, replacer

IN, OUT = 'ŠČ', 'Щ'

do = replacer({IN: OUT, IN.title(): OUT, IN.lower(): OUT.lower()})
