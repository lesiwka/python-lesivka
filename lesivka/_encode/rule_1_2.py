# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import translator

IN, OUT = 'БВГҐДЗКЛМНПРСТФХЦ', 'BVHGDZKLMNPRSTFXC'

do = translator(IN + IN.lower(), OUT + OUT.lower())
