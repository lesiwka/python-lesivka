# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, translator

IN, OUT = ACUTE, 'Ь'

do = translator(IN * 2, OUT + OUT.lower())
