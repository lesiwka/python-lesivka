# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, replacer

APOSTROPHES = "'`’’''"

apply = applier(replacer({c: '' for c in APOSTROPHES}))
