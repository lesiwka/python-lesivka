from pathlib import Path

import lesivka


def test_benchmark(benchmark):
    path = Path(__file__).parent / "lisova.txt"
    text = path.read_text()
    benchmark(lesivka.encode, text)
