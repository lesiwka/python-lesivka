# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from . import _decode, _encode
from .diacritics import ACUTE, APOSTROPHES, CARON
from .utils import Converter

CYR = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' + ACUTE + APOSTROPHES
LAT = 'ABCČDĐEFGHIJKLMNOPRSŠTUVXZŽƵ' + ACUTE + CARON + 'ĆĹŃŔŚŹǴḰḾṔ'

decode = Converter('([^\w%s]+)' % (ACUTE + CARON), LAT, _decode.do)
encode = Converter('([^\w%s]+)' % (ACUTE + APOSTROPHES), CYR, _encode.do)
