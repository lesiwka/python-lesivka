# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import translate

IN, OUT = 'AEIOU', 'АЕИОУ'

convert = translate(IN + IN.lower(), OUT + OUT.lower())
