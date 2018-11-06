# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import translate

IN, OUT = 'Ї', 'JI'

convert = translate({IN: OUT, IN.lower(): OUT.lower()})
