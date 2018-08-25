# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, translator

IN, OUT = 'J', 'Й'

apply = applier(translator(IN + IN.lower(), OUT + OUT.lower()))
