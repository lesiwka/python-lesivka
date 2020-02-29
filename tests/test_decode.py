# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lesivka import decode
from lesivka.diacritics import CARON


@pytest.mark.parametrize('given,expected', (
    ('akula', 'акула'),
    ('babak', 'бабак'),
    ('vovk', 'вовк'),
    ('halka', 'галка'),
    ('gava', 'ґава'),
    ('dub', 'дуб'),
    ('emu', 'ему'),
    ('jenot', 'єнот'),
    ('majbutńe', 'майбутнє'),
    ('žaba', 'жаба'),
    ('zubr', 'зубр'),
    ('kalina', 'калина'),
    ('inšij', 'інший'),
    ('last́ivka', 'ластівка'),
    ('jižak', 'їжак'),
    ('jorž', 'йорж'),
    ('kačka', 'качка'),
    ('leleka', 'лелека'),
    ('muxa', 'муха'),
    ('netopir', 'нетопир'),
    ('orel', 'орел'),
    ('pavič', 'павич'),
    ('ravlik', 'равлик'),
    ('sobaka', 'собака'),
    ('tihr', 'тигр'),
    ('udav', 'удав'),
    ('fretka', 'фретка'),
    ('xovrax', 'ховрах'),
    ('cesarka', 'цесарка'),
    ('čajka', 'чайка'),
    ('špak', 'шпак'),
    ('ščur', 'щур'),
    ('oleń', 'олень'),
    ('junak', 'юнак'),
    ('had́uka', 'гадюка'),
    ('jabluko', 'яблуко'),
    ('d́atel', 'дятел'),
    ('đḿiĺ', 'джміль'),
    ('geƶ́', 'ґедзь'),
    ('hajivka', 'гаївка'),
    ('objizd', "об'їзд"),
    ('praistota', 'праістота'),
    ('znaju', 'знаю'),
    ('śimja', "сім'я"),
    ('bđ́ilka', 'бджілка'),
    ('ƶvonik', 'дзвоник'),
    ('ṕidživiti', 'підживити'),
    ('v́idznačiti', 'відзначити'),
    ('c' + CARON + 'aj', 'чай'),
    ('paṕir', 'папір'),
    ('Nad-Ja', 'Над-Я'),
    ('MakKuin', 'МакКуін'),
    ('Mjač', "М'яч"),
    ('vjo', 'вйо'),
    ('ĹON', 'ЛЬОН'),
))
def test_encode(given, expected):
    assert decode(given) == expected
