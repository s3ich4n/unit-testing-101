def is_string_long(input_val: str):
    if len(input_val) > 5:
        return True
    return False


def test_is_string_long():
    assert is_string_long("abc") is False
    assert is_string_long("abcdef") is True
