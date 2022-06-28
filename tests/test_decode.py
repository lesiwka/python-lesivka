import pytest

from lesivka import decode
from lesivka.diacritics import CARON


@pytest.mark.parametrize(
    "given,expected",
    (
        ("akula", "акула"),
        ("babak", "бабак"),
        ("vowk", "вовк"),
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
        ("lastiwka", "ластівка"),
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
        ("udaw", "удав"),
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
        ("hajiwka", "гаївка"),
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
        ("cqajka", "чайка"),
        ("sqpak", "шпак"),
        ("zqaba", "жаба"),
        ("sqcqur", "щур"),
        ("dqmil'", "джміль"),
        ("geqq'", "ґедзь"),
        ("qqvin", "дзвін"),
        ("mizqzor'anyj", "міжзоряний"),
        ("zqqvonytys'a", "здзвонитися"),
    ),
)
def test_decode_ascii(given, expected):
    assert decode(given, no_diacritics=True) == expected
