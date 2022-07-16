import lesivka


def test_encode():
    assert lesivka.encode("лесівка") == "lesiwka"


def test_encode_ascii():
    assert lesivka.encode("чайка", no_diacritics=True) == "cqajka"
