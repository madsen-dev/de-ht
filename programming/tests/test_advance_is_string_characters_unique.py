import pytest
from programming.advanced_is_string_characters_unique import analyze_string_uniqueness

class TestAnalyzeStringUniqueness:
    
    @pytest.mark.parametrize("test_input,expected_is_unique,expected_unique,expected_repeated", [
        # Test cases with all unique characters
        ("abcde", True, {"a", "b", "c", "d", "e"}, set()),
        ("", True, set(), set()),
        ("a", True, {"a"}, set()),
        ("12345", True, {"1", "2", "3", "4", "5"}, set()),
        ("!@#$%", True, {"!", "@", "#", "$", "%"}, set()),
        
        # Test cases with repeated characters
        ("aa", False, set(), {"a"}),
        ("hello", False, {"h", "e", "o"}, {"l"}),
        ("aabbcc", False, set(), {"a", "b", "c"}),
        ("112345", False, {"2", "3", "4", "5"}, {"1"}),
        ("programming", False, {"p", "o", "a", "i", "n"}, {"r", "g", "m"}),
        
        # Test cases with mixed unique and repeated characters
        ("abcaa", False, {"b", "c"}, {"a"}),
        ("hello world", False, {"h", "e", "w", "r", "d"}, {"l", "o"}),  # spaces removed
        ("test123test", False, {"1", "2", "3"}, {"t", "e", "s"}),
        
        # Test cases with spaces (should be ignored)
        ("a b c d e", True, {"a", "b", "c", "d", "e"}, set()),
        ("a a b b", False, set(), {"a", "b"}),
        ("   ", True, set(), set()),  # only spaces
        ("a   b", True, {"a", "b"}, set()),
        
        # Test cases with case sensitivity
        ("aA", True, {"a", "A"}, set()),
        ("AaBbCc", True, {"A", "a", "B", "b", "C", "c"}, set()),
        ("AaAa", False, set(), {"A", "a"}),
        
        # Test cases with special characters and numbers
        ("!@#!@#", False, set(), {"!", "@", "#"}),
        ("123!@#", True, {"1", "2", "3", "!", "@", "#"}, set()),
        ("a1!a1!", False, set(), {"a", "1", "!"}),
        
        # Edge cases
        ("abcdefghijklmnopqrstuvwxyz", True, set("abcdefghijklmnopqrstuvwxyz"), set()),
        ("aaaaaa", False, set(), {"a"}),
        ("ab cd ef gh", True, {"a", "b", "c", "d", "e", "f", "g", "h"}, set()),
    ])
    def test_analyze_string_uniqueness(self, test_input, expected_is_unique, expected_unique, expected_repeated):
        is_unique, unique_chars, repeated_chars = analyze_string_uniqueness(test_input)
        
        assert is_unique == expected_is_unique, f"Expected is_unique={expected_is_unique}, got {is_unique}"
        assert unique_chars == expected_unique, f"Expected unique_chars={expected_unique}, got {unique_chars}"
        assert repeated_chars == expected_repeated, f"Expected repeated_chars={expected_repeated}, got {repeated_chars}"

    def test_return_types(self):
        """Test that the function returns the correct types"""
        is_unique, unique_chars, repeated_chars = analyze_string_uniqueness("test")
        
        assert isinstance(is_unique, bool)
        assert isinstance(unique_chars, set)
        assert isinstance(repeated_chars, set)

    def test_spaces_are_removed(self):
        """Test that spaces are properly removed from analysis"""
        # These should be equivalent since spaces are removed
        result1 = analyze_string_uniqueness("abc")
        result2 = analyze_string_uniqueness("a b c")
        result3 = analyze_string_uniqueness("  a  b  c  ")
        
        assert result1 == result2 == result3

    def test_no_overlap_between_unique_and_repeated(self):
        """Test that unique_chars and repeated_chars never overlap"""
        test_cases = ["hello", "programming", "test123", "a!b@c#a!", ""]
        
        for test_input in test_cases:
            is_unique, unique_chars, repeated_chars = analyze_string_uniqueness(test_input)
            
            # Sets should not have any intersection
            assert unique_chars.isdisjoint(repeated_chars), \
                f"unique_chars and repeated_chars should not overlap for input '{test_input}'"

    def test_all_chars_accounted_for(self):
        """Test that every character (except spaces) appears in either unique or repeated sets"""
        test_cases = ["hello", "programming", "test123", "a!b@c#a!"]
        
        for test_input in test_cases:
            is_unique, unique_chars, repeated_chars = analyze_string_uniqueness(test_input)
            
            # Get all unique characters from input (spaces removed)
            input_chars = set(test_input.replace(" ", ""))
            result_chars = unique_chars | repeated_chars
            
            assert input_chars == result_chars, \
                f"All characters should be accounted for in input '{test_input}'"

    def test_is_unique_logic(self):
        """Test that is_unique is True only when repeated_chars is empty"""
        test_cases = ["hello", "abcde", "", "aa", "programming", "123", "a b c d"]
        
        for test_input in test_cases:
            is_unique, unique_chars, repeated_chars = analyze_string_uniqueness(test_input)
            
            expected_is_unique = len(repeated_chars) == 0
            assert is_unique == expected_is_unique, \
                f"is_unique should be {expected_is_unique} for input '{test_input}'"