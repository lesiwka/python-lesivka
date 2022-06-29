import lesiwka


def test_benchmark(benchmark, sample):
    benchmark(lesiwka.encode, sample)
