import pytest

from lesiwka import encode


@pytest.mark.parametrize(
    "given,expected",
    (
        ("акула", "akula"),
        ("бабак", "babak"),
        ("вовк", "vowk"),
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
        ("ластівка", "lastiwka"),
        ("їжак", "jižak"),
        ("йорж", "jorž"),
        ("качка", "kačka"),
        ("лелека", "leleka"),
        ("муха", "muxa"),
        ("нетопир", "netopyr"),
        ("орел", "orel"),
        ("павич", "pavyč"),
        ("равлик", "rawlyk"),
        ("собака", "sobaka"),
        ("тигр", "tyhr"),
        ("удав", "udaw"),
        ("фретка", "fretka"),
        ("ховрах", "xowrax"),
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
        ("гаївка", "hajiwka"),
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
        # ("сыр", "сыр"),
        ("Є ", "Je "),
        # ("Ь", ""),
        ("йі", "ji"),
        ("передзвонити", "pereƶvonyty"),
        ("передзимовий", "peredzymovyj"),
        ("передз'їздівський", "peredzjizdiwśkyj"),
        ("Укрінформ", "Ukrinform"),
        ("наївся", "najiwśa"),
        ("з'їв", "zjiw"),
        ("нї", "ńi"),
        ("вйо", "wjo"),
        ("братів-українців", "brativ-ukrajinciw"),
        ("в Україну", "v Ukrajinu"),
        ("удав, акула", "udaw, akula"),
        ("удав акулі", "udav akuli"),
        ("удав бабакові", "udaw babakovi"),
        ("впав — упав", "wpaw — upaw"),
        ("ЮНІСЕФ", "JuNISEF"),
        ("ЦДЮТ", "CDJuT"),
        ("ВВР", "VVR"),
        ("ВВП", "VWP"),
        ("бульв. Шевченка", "buĺv. Šewčenka"),
        ("Див. деталі", "Dyv. detali"),
        ("в.о.", "v.o."),
        ("в «Атласі»", "v «Atlasi»"),
        ("в  Європі", "w  Jewropi"),
        ("в'язниця", "wjaznyća"),
        ("в ЄС", "w JeS"),
        ("Та́врія", "Táwrija"),
        (
            "Якось в дні передзимові, "
            "Захотілось вовку крові. "
            "Кров проллється, задзюрчить... "
            "Дзиґа-хвіст не вгомониться, "
            "П'яний ніс, як те бджільництво, "
            "На обличчі аж дзижчить.",
            "Jakoś w dni peredzymovi, "
            "Zaxotiloś vowku krovi. "
            "Krow prolĺet́śa, zaƶ́určyt́... "
            "Ƶyga-xvist ne whomonyt́śa, "
            "Pjanyj nis, jak te bđiĺnyctvo, "
            "Na oblyčči až ƶyžčyt́.",
        ),
        ("вгоджати", "whođaty"),
        ("в'язати", "wjazaty"),
        ("вв'язатися", "wwjazatyśa"),
        ("барвний", "barwnyj"),
        ("Щастя", "Ščast́a"),
        ("вщухати", "wščuxaty"),
        ("чіпляються", "čipĺajut́śa"),
        ("сім'єю", "simjeju"),
    ),
)
def test_encode(given, expected):
    assert encode(given) == expected


@pytest.mark.parametrize(
    ("given", "expected"),
    (
        ("чайка", "cqajka"),
        ("шпак", "sqpak"),
        ("жаба", "zqaba"),
        ("щур", "sqcqur"),
        ("джміль", "dqmil'"),
        ("ґедзь", "geqq'"),
        ("дзвін", "qqvin"),
        ("міжзоряний", "mizqzor'anyj"),
        ("здзвонитися", "zqqvonytys'a"),
    ),
)
def test_encode_ascii(given, expected):
    assert encode(given, no_diacritics=True) == expected
