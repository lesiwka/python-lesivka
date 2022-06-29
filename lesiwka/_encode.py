import re

from .ascii import asciilator
from .diacritics import ACUTE
from .punctuation import APOSTROPHES, DELIMITERS

vowels_lower_cyr = "аеиіоу"
vowels_upper_cyr = vowels_lower_cyr.upper()
vowels_cyr = vowels_lower_cyr + vowels_upper_cyr

vowels_lower_lat = "aeyiou"
vowels_upper_lat = vowels_lower_lat.upper()
vowels_lat = vowels_lower_lat + vowels_upper_lat

iotted_lower_cyr = "єїюя"
iotted_upper_cyr = iotted_lower_cyr.upper()
iotted_cyr = iotted_lower_cyr + iotted_upper_cyr

iotted_lower_out = "еіуа"
iotted_upper_out = iotted_lower_out.upper()

iot_lower_cyr = "й"
iot_upper_cyr = iot_lower_cyr.upper()

consonants_lower_cyr = "бвдгґжзйклмнпрстфхцчш"
consonants_upper_cyr = consonants_lower_cyr.upper()
consonants_cyr = consonants_lower_cyr + consonants_upper_cyr

consonants_lower_lat = "bvdhgžzjklmnprstfxcčš"
consonants_upper_lat = consonants_lower_lat.upper()
consonants_lat = consonants_lower_lat + consonants_upper_lat

soft_sign_lower_cyr = "ь"
soft_sign_upper_cyr = soft_sign_lower_cyr.upper()
soft_sign_cyr = soft_sign_lower_cyr + soft_sign_upper_cyr

soft_sign_lat = ACUTE * 2

sqcq_lower_cyr = "щ"
sqcq_upper_cyr = sqcq_lower_cyr.upper()
sqcq_cyr = sqcq_lower_cyr + sqcq_upper_cyr

sqcq_lower_lat = "šč"
sqcq_upper_lat = sqcq_lower_lat.upper()

lower_cyr = (
    vowels_lower_cyr + iotted_lower_cyr + consonants_lower_cyr + sqcq_lower_cyr
)
all_cyr = vowels_cyr + iotted_cyr + consonants_cyr + soft_sign_cyr + sqcq_cyr

abbr = (
    ("ЄІБ", "JeIB"),
    ("ЄАВТ", "JeAVT"),
    ("ЄАЕС", "JeAES"),
    ("ЄАНТК", "JeANTK"),
    ("ЄАР", "JeAR"),
    ("ЄБА", "JeBA"),
    ("ЄБРР", "JeBRR"),
    ("ЄВС", "JeVS"),
    ("ЄГФ", "JeHF"),
    ("ЄДІ", "JeDI"),
    ("ЄДАПС", "JeDAPS"),
    ("ЄДЕБО", "JeDEBO"),
    ("ЄДКІ", "JeDKI"),
    ("ЄДР", "JeDR"),
    ("ЄДРПОУ", "JeDRPOU"),
    ("ЄЕК", "JeEK"),
    ("ЄЕП", "JeEP"),
    ("ЄЕС", "JeES"),
    ("ЄЕСУ", "JeESU"),
    ("ЄК", "JeK"),
    ("ЄКА", "JeKA"),
    ("ЄКВ", "JeKV"),
    ("ЄКП", "JeKP"),
    ("ЄКПЛ", "JeKPL"),
    ("ЄКРН", "JeKRN"),
    ("ЄНП", "JeNP"),
    ("ЄНР", "JeNR"),
    ("ЄОВС", "JeOVS"),
    ("ЄП", "JeP"),
    ("ЄПС", "JePS"),
    ("ЄР", "JeR"),
    ("ЄРДР", "JeRDR"),
    ("ЄРПН", "JeRPN"),
    ("ЄРЦ", "JeRC"),
    ("ЄС", "JeS"),
    ("ЄСВ", "JeSV"),
    ("ЄСВС", "JeSVS"),
    ("ЄСПЛ", "JeSPL"),
    ("ЄУ", "JeU"),
    ("ЄХБ", "JeXB"),
    ("ЄЦ", "JeC"),
    ("ЄЦБ", "JeCB"),
    ("АВМ", "AVM"),
    ("БВПД", "BWPD"),
    ("БДЮТ", "BDJuT"),
    ("БЮТ", "BJuT"),
    ("ВВІР", "VVIR"),
    ("ВВВ", "VVV"),
    ("ВВНЗ", "VVNZ"),
    ("ВВП", "VWP"),
    ("ВВР", "VVR"),
    ("ВГК", "VHK"),
    ("ВГСУ", "VHSU"),
    ("ВД", "VD"),
    ("ВДАІ", "VDAI"),
    ("ВДВ", "VDV"),
    ("ВДЕ", "VDE"),
    ("ВДНГ", "VDNH"),
    ("ВДПУ", "VDPU"),
    ("ВЗ", "VZ"),
    ("ВЗУН", "VZUN"),
    ("ВК", "VK"),
    ("ВКВ", "VKV"),
    ("ВККС", "VKKS"),
    ("ВККСУ", "VKKSU"),
    ("ВКЛ", "VKL"),
    ("ВМД", "VMD"),
    ("ВМС", "VMS"),
    ("ВМСУ", "VMSU"),
    ("ВМФ", "VMF"),
    ("ВНАУ", "VNAU"),
    ("ВНЗ", "VNZ"),
    ("ВНО", "VNO"),
    ("ВНП", "VNP"),
    ("ВНТ", "VNT"),
    ("ВНТУ", "VNTU"),
    ("ВП", "VP"),
    ("ВПК", "VPK"),
    ("ВПЛ", "VPL"),
    ("ВПС", "VPS"),
    ("ВПУ", "VPU"),
    ("ВР", "VR"),
    ("ВРП", "VRP"),
    ("ВРУ", "VRU"),
    ("ВРХ", "VRX"),
    ("ВРЮ", "VRJu"),
    ("ВС", "VS"),
    ("ВСП", "VSP"),
    ("ВССУ", "VSSU"),
    ("ВСУ", "VSU"),
    ("ВТС", "VTS"),
    ("ВТССУМ", "VTSSUM"),
    ("ВЦА", "VCA"),
    ("ВЯП", "VJaP"),
    ("ГУМВС", "HUMWS"),
    ("ДЄС", "DJeS"),
    ("ДВЗ", "DWZ"),
    ("ДНЯЗ", "DNJaZ"),
    ("ДЮСШ", "DJuSŠ"),
    ("ДЮСШОР", "DJuSŠOR"),
    ("ДЮФЛ", "DJuFL"),
    ("ЗЄС", "ZJeS"),
    ("КДЮСШ", "KDJuSŠ"),
    ("ЛЄ", "LJe"),
    ("МВС", "MWS"),
    ("МВСУ", "MWSU"),
    ("НАЗЯВО", "NAZJaVO"),
    ("НБСЄ", "NBSJe"),
    ("НКВC", "NKWS"),
    ("НКВД", "NKWD"),
    ("НУВГП", "NUVHP"),
    ("ОІЯД", "OIJaD"),
    ("ОАЄ", "OAJe"),
    ("ОБСЄ", "OBSJe"),
    ("ОВД", "OVD"),
    ("ОВК", "OVK"),
    ("ОВП", "OVP"),
    ("ОВТ", "OVT"),
    ("ОДЮСШ", "ODJuSŠ"),
    ("ПАРЄ", "PARJe"),
    ("ПВЗВТ", "PWZVT"),
    ("РЄ", "RJe"),
    ("СЄПН", "SJePN"),
    ("СВПД", "SWPD"),
    ("СВР", "SWR"),
    ("СДЮШО", "SDJuŠO"),
    ("СДЮШОР", "SDJuŠOR"),
    ("СРЮ", "SRJu"),
    ("СФРЮ", "SFRJu"),
    ("ТЮГ", "TJuH"),
    ("УЄФА", "UJeFA"),
    ("УЄЦАВ", "UJeCAV"),
    ("УАВПП", "UAVPP"),
    ("УВВ", "UVV"),
    ("УВК", "UVK"),
    ("УВКБ", "UVKB"),
    ("УВКПЛ", "UVKPL"),
    ("УВП", "UVP"),
    ("УМВС", "UMWS"),
    ("УМВСУ", "UMWSU"),
    ("УНКВC", "UNKWS"),
    ("УНКВД", "UNKWD"),
    ("УЦОЯО", "UCOJaO"),
    ("ФГВФО", "FHWFO"),
    ("ХВЄ", "XVJe"),
    ("ХДАВП", "XDAVP"),
    ("ЦДЮТ", "CDJuT"),
    ("ЦОВВ", "COVW"),
    ("ЦСЄ", "CSJe"),
    ("ЦСВЯП", "CSVJaP"),
    ("ЧЄ", "ČJe"),
    ("ЮВТ", "JuVT"),
    ("ЮНІДО", "JuNIDO"),
    ("ЮНІСЕФ", "JuNISEF"),
    ("ЮНЕП", "JuNEP"),
    ("ЮНЕСКО", "JuNESKO"),
    ("ЮНКТАД", "JuNKTAD"),
    ("ЮНОПС", "JuNOPS"),
    ("ЮНСІТРАЛ", "JuNSITRAL"),
    ("ЮРС", "JuRS"),
    ("ЮУАЕС", "JuUAES"),
    ("ЮФ", "JuF"),
    ("ЯМР", "JaMR"),
)
abbr_dot_pattern = (
    r"(?i:(?<=)|(?<=буль)|(?<=г)|(?<=ди)|(?<=за)|(?<=з)|"
    r"(?<=і)|(?<=ін)|(?<=к)|(?<=пере)|(?<=по)|(?<=про)|"
    r"(?<=родо)|(?<=с)|(?<=св)|(?<=сло)|(?<=то)){0}(?=\.)"
)

w_pattern = (
    r"((?<=\b)|(?<=[%s])){0}((?=[%s])|(?=\W*$)|"
    r"(?=\W*[%s](?:\W|$))|(?=\W+[%s]))"
    % (
        all_cyr,
        consonants_cyr + sqcq_cyr,
        DELIMITERS,
        consonants_cyr + sqcq_cyr + iotted_cyr + consonants_lat,
    )
)

apostrophe_pattern = r"(?<=\w)[%s]{0}" % APOSTROPHES
iotted_pattern = r"((?<=\b)|(?<=[%s])){0}" % (vowels_cyr + iotted_cyr)
ending_pattern = r"(?=[%s]|\W*$)" % (lower_cyr + "w")
acuted_pattern = r"(?<=[%s]){0}" % (consonants_cyr + sqcq_cyr)

affricate_exclude_pattern = (
    r"(?i:(?<=\bпере))({0}(?i:з))(?i:(?=вен|він|вон|ижч))"
)
affricate_pattern = (
    r"(?i:(?!(?<=\bві)|(?<=\bна)|(?<=\bо)|(?<=\bпере)|(?<=\bпі)|"
    r"(?<=\bпона)|(?<=\bпопі)|(?<=\bпре)|(?<=\bсере))){0}"
)

patterns = ()
patterns += (
    (abbr_dot_pattern.format("в"), "v"),
    (abbr_dot_pattern.format("В"), "V"),
)
patterns += tuple((r"\b{0}\b".format(cyr), lat) for cyr, lat in abbr)
patterns += tuple((w_pattern.format(cyr), lat) for cyr, lat in zip("вВ", "wW"))

patterns += ((sqcq_upper_cyr + ending_pattern, sqcq_lower_lat.title()),)

patterns += tuple(
    (apostrophe_pattern.format(cyr), iot_lower_cyr + out)
    for cyr, out in zip(iotted_lower_cyr, iotted_lower_out)
)
patterns += tuple(
    (apostrophe_pattern.format(cyr) + ending_pattern, iot_upper_cyr + out)
    for cyr, out in zip(iotted_upper_cyr, iotted_lower_out)
)
patterns += tuple(
    (apostrophe_pattern.format(cyr), iot_upper_cyr + out)
    for cyr, out in zip(iotted_upper_cyr, iotted_upper_out)
)
patterns += tuple(
    (iotted_pattern.format(cyr), iot_lower_cyr + out)
    for cyr, out in zip(iotted_lower_cyr, iotted_lower_out)
)
patterns += tuple(
    (iotted_pattern.format(cyr) + ending_pattern, iot_upper_cyr + out)
    for cyr, out in zip(iotted_upper_cyr, iotted_lower_out)
)
patterns += tuple(
    (iotted_pattern.format(cyr), iot_upper_cyr + out)
    for cyr, out in zip(iotted_upper_cyr, iotted_upper_out)
)
patterns += tuple(
    (acuted_pattern.format(cyr), ACUTE + out)
    for cyr, out in zip(iotted_lower_cyr, iotted_lower_out)
)
patterns += tuple(
    (acuted_pattern.format(cyr), ACUTE + out)
    for cyr, out in zip(iotted_upper_cyr, iotted_upper_out)
)

patterns += (
    (affricate_exclude_pattern.format("д"), "ƶ"),
    (affricate_exclude_pattern.format("Д"), "Ƶ"),
)
patterns += (
    (affricate_pattern.format("дж"), "đ"),
    (affricate_pattern.format("Дж"), "Đ"),
    (affricate_pattern.format("дз"), "ƶ"),
    (affricate_pattern.format("Дз"), "Ƶ"),
)

table = dict(
    zip(
        vowels_cyr + consonants_cyr + soft_sign_cyr,
        vowels_lat + consonants_lat + soft_sign_lat,
    )
)
table[sqcq_lower_cyr] = sqcq_lower_lat
table[sqcq_upper_cyr] = sqcq_upper_lat
table = str.maketrans(table)


def encode(text, no_diacritics=False):
    result = text

    for pattern, repl in patterns:
        result = re.sub(pattern, repl, result)

    result = result.translate(table)

    if no_diacritics:
        result = asciilator(result)

    return result
