import string_add


def test_add_string_wrong_format():
    wrong_string = "asdfghj"
    result = string_add.add(wrong_string)
    assert result == -1, "Result should be -1"


def test_add_string_no_delimiter_numbers():
    no_delimiter_numbers_string = "1234"
    result = string_add.add(no_delimiter_numbers_string)
    assert result == 1234, "Result should be 1234"


def test_add_string_default_delimiter_numbers():
    default_delimiter_numbers_string = "1,2,3,4"
    result = string_add.add(default_delimiter_numbers_string)
    assert result == 10, "Result should be 10"


def test_add_string_custom_delimiter_numbers():
    custom_delimiter_numbers_string = "2;9;5;12"
    result = string_add.add(custom_delimiter_numbers_string, delimiter=';')
    assert result == 30, "Result should be 30"
