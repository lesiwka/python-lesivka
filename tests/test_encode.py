# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lesivka import encode


@pytest.mark.parametrize(
    "given,expected",
    (
        ("акула", "akula"),
        ("бабак", "babak"),
        ("вовк", "vovk"),
        ("галка", "halka"),
        ("ґава", "gava"),
        ("дуб", "dub"),
        ("ему", "emu"),
        ("єнот", "jenot"),
        ("майбутнє", "majbutńe"),
        ("жаба", "žaba"),
        ("зубр", "zubr"),
        ("калина", "kalyna"),
        ("индик", "yndyk"),
        ("інший", "inšyj"),
        ("ластівка", "lastivka"),
        ("їжак", "jižak"),
        ("йорж", "jorž"),
        ("качка", "kačka"),
        ("лелека", "leleka"),
        ("муха", "muxa"),
        ("нетопир", "netopyr"),
        ("орел", "orel"),
        ("павич", "pavyč"),
        ("равлик", "ravlyk"),
        ("собака", "sobaka"),
        ("тигр", "tyhr"),
        ("удав", "udav"),
        ("фретка", "fretka"),
        ("ховрах", "xovrax"),
        ("цесарка", "cesarka"),
        ("чайка", "čajka"),
        ("шпак", "špak"),
        ("щур", "ščur"),
        ("олень", "oleń"),
        ("юнак", "junak"),
        ("гадюка", "had́uka"),
        ("яблуко", "jabluko"),
        ("дятел", "d́atel"),
        ("джміль", "đmiĺ"),
        ("ґедзь", "geƶ́"),
        ("гаївка", "hajivka"),
        ("об'їзд", "objizd"),
        ("праістота", "praistota"),
        ("знаю", "znaju"),
        ("сім'я", "simja"),
        ("бджілка", "bđilka"),
        ("дзвоник", "ƶvonyk"),
        ("підживити", "pidžyvyty"),
        ("відзначити", "vidznačyty"),
        ("абе́тка", "abétka"),
        ("Яблуко", "Jabluko"),
        ("Я, РОБОТ", "JA, ROBOT"),
        ("Над-Я", "Nad-Ja"),
        ("ПП", "PP"),
        ("МакКуін", "MakKuin"),
        ("Це \u2019риба\u2019.", "Ce \u2019ryba\u2019."),
        ("\u2019пір\u2019я\u2019", "\u2019pirja\u2019"),
        ("'м'яч'", "'mjač'"),
        ("'", "'"),
        ("сыр", "сыр"),
        ("Є ", "Je "),
        ("Ь", ""),
        ("йі", "ji"),
        ("передзвонити", "pereƶvonyty"),
        ("передзимовий", "peredzymovyj"),
        ("передз'їздівський", "peredzjizdivśkyj"),
        ("Укрінформ", "Ukrinform"),
        ("наївся", "najivśa"),
        ("з'їв", "zjiv"),
        ("нї", "ńi"),
    ),
)
def test_encode(given, expected):
    assert encode(given) == expected


@pytest.mark.parametrize(
    ("given", "expected"),
    (
        ("чайка", "cwajka"),
        ("шпак", "swpak"),
        ("жаба", "zwaba"),
        ("щур", "swcwur"),
        ("джміль", "dqmil'"),
        ("ґедзь", "gezq'"),
    ),
)
def test_encode_ascii(given, expected):
    assert encode(given, no_diacritics=True) == expected
