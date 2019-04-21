import string_add


def test_add_string_wrong_format():
    wrong_string = "asdfghj"
    result = string_add.add(wrong_string)
    assert result == -1, "Result should be -1"
