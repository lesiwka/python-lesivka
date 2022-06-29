from pathlib import Path

import pytest


@pytest.fixture
def sample():
    path = Path(__file__).parent / "lisova.txt"
    return path.read_text()
