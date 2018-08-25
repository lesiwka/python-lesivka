# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from . import _decode, _encode
from .diacritics import ACUTE
from .utils import splitter


decode = splitter('([^\w%s]+)' % ACUTE, _decode)
encode = splitter('(\W+)', _encode)
