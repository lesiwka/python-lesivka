# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, replacer

APOSTROPHES = "'`\u2018\u2019\u201b\u2032\u2035"

apply = applier(replacer({c: '' for c in APOSTROPHES}))
