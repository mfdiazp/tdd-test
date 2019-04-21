import string_add


def test_add_string_wrong_format():
    wrong_string = "asdfghj"
    result = string_add.add(wrong_string)
    assert result == -1, "Result should be -1"


def test_add_string_no_delimiter_numbers():
    no_delimiter_numbers_string = "1234"
    result = string_add.add(no_delimiter_numbers_string)
    assert result == 1234, "Result should be 1234"
