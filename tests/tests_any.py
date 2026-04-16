import pytest
from calculator import plus


def test_plus():
    assert plus(2, 3) == 5
