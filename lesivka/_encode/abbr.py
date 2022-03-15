from ..utils import applier
from . import rule_1_1, rule_1_2, rule_1_3, rule_2_2

ABBR = [
    "АВМ",
    "БДЮТ",
    "БЮТ",
    "ВВВ",
    "ВВІР",
    "ВВНЗ",
    "ВВР",
    "ВГК",
    "ВГСУ",
    "ВД",
    "ВДАІ",
    "ВДВ",
    "ВДЕ",
    "ВДНГ",
    "ВДПУ",
    "ВЗ",
    "ВЗУН",
    "ВК",
    "ВКВ",
    "ВККС",
    "ВККСУ",
    "ВКЛ",
    "ВМД",
    "ВМС",
    "ВМСУ",
    "ВМФ",
    "ВНАУ",
    "ВНЗ",
    "ВНО",
    "ВНП",
    "ВНТ",
    "ВНТУ",
    "ВП",
    "ВПК",
    "ВПЛ",
    "ВПС",
    "ВПУ",
    "ВР",
    "ВРП",
    "ВРУ",
    "ВРХ",
    "ВРЮ",
    "ВС",
    "ВСП",
    "ВССУ",
    "ВСУ",
    "ВТС",
    "ВТССУМ",
    "ВЦА",
    "ВЯП",
    "ДЄС",
    "ДНЯЗ",
    "ДЮСШ",
    "ДЮСШОР",
    "ДЮФЛ",
    "ЄАЕС",
    "ЄАНТК",
    "ЄАР",
    "ЄБА",
    "ЄБРР",
    "ЄВС",
    "ЄГФ",
    "ЄДАПС",
    "ЄДЕБО",
    "ЄДІ",
    "ЄДКІ",
    "ЄДР",
    "ЄДРПОУ",
    "ЄЕК",
    "ЄЕП",
    "ЄЕС",
    "ЄЕСУ",
    "ЄІБ",
    "ЄК",
    "ЄКА",
    "ЄКВ",
    "ЄКП",
    "ЄКПЛ",
    "ЄКРН",
    "ЄНП",
    "ЄНР",
    "ЄОВС",
    "ЄП",
    "ЄПС",
    "ЄР",
    "ЄРДР",
    "ЄРПН",
    "ЄРЦ",
    "ЄС",
    "ЄСВ",
    "ЄСВС",
    "ЄСПЛ",
    "ЄУ",
    "ЄХБ",
    "ЄЦ",
    "ЄЦБ",
    "ЗЄС",
    "КДЮСШ",
    "ЛЄ",
    "НАЗЯВО",
    "НБСЄ",
    "НУВГП",
    "ОАЄ",
    "ОБСЄ",
    "ОВД",
    "ОВК",
    "ОВП",
    "ОВТ",
    "ОДЮСШ",
    "ОІЯД",
    "ПАРЄ",
    "РЄ",
    "СДЮШО",
    "СДЮШОР",
    "СЄПН",
    "СРЮ",
    "СФРЮ",
    "ТЮГ",
    "УАВПП",
    "УВВ",
    "УВК",
    "УВКБ",
    "УВКПЛ",
    "УВП",
    "УЄФА",
    "УЄЦАВ",
    "УЦОЯО",
    "ХВЄ",
    "ХДАВП",
    "ЦДЮТ",
    "ЦОВВ",
    "ЦСВЯП",
    "ЦСЄ",
    "ЧЄ",
    "ЮВТ",
    "ЮНЕП",
    "ЮНЕСКО",
    "ЮНІДО",
    "ЮНІСЕФ",
    "ЮНКТАД",
    "ЮНОПС",
    "ЮНСІТРАЛ",
    "ЮРС",
    "ЮУАЕС",
    "ЮФ",
    "ЯМР",
]

ABBR_W_EXCLUDES = {
    "БВПД": "BWPD",
    "ВВП": "VWP",
    "ГУМВС": "HUMWS",
    "ДВЗ": "DWZ",
    "ЄАВТ": "JeAVT",
    "ЄОВС": "JeOVS",
    "МВС": "MWS",
    "МВСУ": "MWSU",
    "НКВД": "NKWD",
    "НКВC": "NKWS",
    "ПВЗВТ": "PWZVT",
    "СВПД": "SWPD",
    "СВР": "SWR",
    "УМВС": "UMWS",
    "УМВСУ": "UMWSU",
    "УНКВД": "UNKWD",
    "УНКВC": "UNKWS",
    "ФГВФО": "FHWFO",
    "ЦОВВ": "COVW",
}

ABBR_W_DOT_EXCLUDES = [
    "В",
    "ГВ",
    "ДИВ",
    "ЗАВ",
    "ЗВ",
    "ІВ",
    "ІНВ",
    "КВ",
    "ПЕРЕВ",
    "ПОВ",
    "ПРОВ",
    "РОДОВ",
    "СВ",
    "СВВ",
    "СЛОВ",
    "ТОВ",
]


abbr = applier(
    rule_1_1.convert,
    rule_1_2.convert,
    rule_1_3.convert,
    rule_2_2.convert,
)


def convert(word):
    if word.word.upper() in ABBR_W_DOT_EXCLUDES and word.has_stop():
        word.abbr = True
    elif word.word in ABBR_W_EXCLUDES:
        word.word = ABBR_W_EXCLUDES[word.word]
        word.abbr = True
    elif word.word in ABBR:
        word.word = "".join(abbr(c).title() for c in word.word)
        word.abbr = True
    return word
