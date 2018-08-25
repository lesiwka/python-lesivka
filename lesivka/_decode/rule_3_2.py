# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import applier, translator

TRANSLATE = {
    'Đ': 'ДЖ',
    'Ƶ': 'ДЗ',
}


def affricates():
    translate = TRANSLATE.copy()
    translate.update({i.lower(): o.lower() for i, o in TRANSLATE.items()})
    return translator(translate)


apply = applier(affricates())
