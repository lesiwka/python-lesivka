# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import translate

IN, OUT = ACUTE, 'Ь'

convert = translate(IN * 2, OUT + OUT.lower())
