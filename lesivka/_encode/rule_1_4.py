# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import applier, translator

IN, OUT = 'Ь', ACUTE

apply = applier(translator(IN + IN.lower(), OUT * 2))
