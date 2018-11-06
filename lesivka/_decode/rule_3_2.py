# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import translate

TRANSLATE = {
    'Đ': 'ДЖ',
    'Ƶ': 'ДЗ',
}


def get_convert():
    data = TRANSLATE.copy()
    data.update({i.lower(): o.lower() for i, o in TRANSLATE.items()})
    return translate(data)


convert = get_convert()
