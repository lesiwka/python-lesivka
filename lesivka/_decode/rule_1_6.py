# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import replace

IN, OUT = 'JI', 'Ї'

convert = replace({IN: OUT, IN.title(): OUT, IN.lower(): OUT.lower()})
