from pathlib import Path

import lesiwka


def test_benchmark(benchmark):
    path = Path(__file__).parent / "lisova.txt"
    text = path.read_text()
    benchmark(lesiwka.encode, text)
