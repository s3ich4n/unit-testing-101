def is_string_long(input_val: str):
    return len(input_val) > 5


def test_is_string_long():
    assert is_string_long("abc") is False
