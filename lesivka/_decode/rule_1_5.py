# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, translator

IN, OUT = 'J', 'Й'

do = translator(IN + IN.lower(), OUT + OUT.lower())
