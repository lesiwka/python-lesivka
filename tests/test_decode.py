# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lesivka import decode
from lesivka.diacritics import CARON


@pytest.mark.parametrize(
    "given,expected",
    (
        ("akula", "акула"),
        ("babak", "бабак"),
        ("vovk", "вовк"),
        ("halka", "галка"),
        ("gava", "ґава"),
        ("dub", "дуб"),
        ("emu", "ему"),
        ("jenot", "єнот"),
        ("majbutńe", "майбутнє"),
        ("žaba", "жаба"),
        ("zubr", "зубр"),
        ("kalyna", "калина"),
        ("yndyk", "индик"),
        ("inšyj", "інший"),
        ("lastivka", "ластівка"),
        ("jižak", "їжак"),
        ("jorž", "йорж"),
        ("kačka", "качка"),
        ("leleka", "лелека"),
        ("muxa", "муха"),
        ("netopyr", "нетопир"),
        ("orel", "орел"),
        ("pavyč", "павич"),
        ("ravlyk", "равлик"),
        ("sobaka", "собака"),
        ("tyhr", "тигр"),
        ("udav", "удав"),
        ("fretka", "фретка"),
        ("xovrax", "ховрах"),
        ("cesarka", "цесарка"),
        ("čajka", "чайка"),
        ("špak", "шпак"),
        ("ščur", "щур"),
        ("oleń", "олень"),
        ("junak", "юнак"),
        ("had́uka", "гадюка"),
        ("jabluko", "яблуко"),
        ("d́atel", "дятел"),
        ("đmiĺ", "джміль"),
        ("geƶ́", "ґедзь"),
        ("hajivka", "гаївка"),
        ("objizd", "об'їзд"),
        ("praistota", "праістота"),
        ("znaju", "знаю"),
        ("simja", "сім'я"),
        ("bđilka", "бджілка"),
        ("ƶvonyk", "дзвоник"),
        ("pidžyvyty", "підживити"),
        ("vidznačyty", "відзначити"),
        ("c" + CARON + "aj", "чай"),
        ("kuṕura", "купюра"),
        ("Nad-Ja", "Над-Я"),
        ("MakKuin", "МакКуін"),
        ("Mjač", "М'яч"),
        ("vjo", "вйо"),
        ("poduščanyj", "подушчаний"),
        ("Melaščyn", "Мелашчин"),
        ("ńi", "нї"),
        ("jy", "ї"),
        ("najimovirnišyj", "найімовірніший"),
    ),
)
def test_decode(given, expected):
    assert decode(given) == expected


@pytest.mark.parametrize(
    ("given", "expected"),
    (
        ("cwajka", "чайка"),
        ("swpak", "шпак"),
        ("zwaba", "жаба"),
        ("swcwur", "щур"),
        ("dqmil'", "джміль"),
        ("gezq'", "ґедзь"),
    ),
)
def test_decode_ascii(given, expected):
    assert decode(given, no_diacritics=True) == expected
