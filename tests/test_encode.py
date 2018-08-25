# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lesivka import encode


@pytest.mark.parametrize('given,expected', (
    ('акула', 'akula'),
    ('бабак', 'babak'),
    ('вовк', 'vovk'),
    ('галка', 'halka'),
    ('ґава', 'gava'),
    ('дуб', 'dub'),
    ('ему', 'emu'),
    ('єнот', 'jenot'),
    ('майбутнє', 'majbutńe'),
    ('жаба', 'žaba'),
    ('зубр', 'zubr'),
    ('калина', 'kalina'),
    ('інший', 'inšij'),
    ('ластівка', 'last́ivka'),
    ('їжак', 'jižak'),
    ('йорж', 'jorž'),
    ('качка', 'kačka'),
    ('лелека', 'leleka'),
    ('муха', 'muxa'),
    ('нетопир', 'netopir'),
    ('орел', 'orel'),
    ('павич', 'pavič'),
    ('равлик', 'ravlik'),
    ('собака', 'sobaka'),
    ('тигр', 'tihr'),
    ('удав', 'udav'),
    ('фретка', 'fretka'),
    ('ховрах', 'xovrax'),
    ('цесарка', 'cesarka'),
    ('чайка', 'čajka'),
    ('шпак', 'špak'),
    ('щур', 'ščur'),
    ('олень', 'oleń'),
    ('юнак', 'junak'),
    ('гадюка', 'had́uka'),
    ('яблуко', 'jabluko'),
    ('дятел', 'd́atel'),
    ('джміль', 'đḿiĺ'),
    ('ґедзь', 'geƶ́'),
    ('гаївка', 'hajivka'),
    ("об'їзд", 'objizd'),
    ('праістота', 'praistota'),
    ('знаю', 'znaju'),
    ("сім'я", 'śimja'),
    ('бджілка', 'bđ́ilka'),
    ('дзвоник', 'ƶvonik'),
    ('підживити', 'ṕidživiti'),
    ('відзначити', 'v́idznačiti'),
))
def test_encode(given, expected):
    assert encode(given) == expected
