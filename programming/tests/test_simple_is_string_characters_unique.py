import pytest
from programming.simple_is_string_characters_unique import is_string_unique

@pytest.mark.parametrize("test_input,expected", [
    ("abcde", True),          # all unique
    ("", True),               # empty string → considered unique
    ("a", True),              # single character
    ("aa", False),            # duplicate characters
    ("abcdA", True),          # case-sensitive: 'a' and 'A' are different
    ("hello", False),         # 'l' repeats
    ("12345", True),          # numeric characters
    ("112345", False),        # repeated digit
    ("!@#$%", True),          # special characters all unique
    ("!@#!!", False),         # duplicate special character
])
def test_is_string_unique(test_input, expected):
    assert is_string_unique(test_input) == expected
