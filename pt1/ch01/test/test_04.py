import pytest


def parse(input_val: int):
    return int(input_val)


def test_parse():
    assert parse("5") == 5

    with pytest.raises(ValueError):
        parse("bbb")

    with pytest.raises(ValueError):
        parse("0b11010010")
