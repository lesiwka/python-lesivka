# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import translate

IN, OUT = 'Ь', ACUTE

convert = translate(IN + IN.lower(), OUT * 2)
