import unittest
from caesar_logic import Caesar
from string import punctuation, digits, whitespace


class CaesarTesting(unittest.TestCase):

    def test_shifting_lower_case_letters_by_a_small_amount(self):
        """Checks that shifting a lower case letter by a small amount gives the
        correct result, while preserving case."""

        caesar = Caesar(5)
        chars_to_shift = ['a', 'm', 'f', 'k', 'u']
        expected = ['f', 'r', 'k', 'p', 'z']
        for char, shifted in zip(chars_to_shift, expected):
            self.assertEqual(shifted, caesar.shift_by_key(char))

    def test_shifting_upper_case_letters_by_a_small_amount(self):
        """Checks that shifting an upper case letter by a small amount gives the
        correct result, while preserving case."""

        caesar = Caesar(10)
        chars_to_shift = ['A', 'M', 'E', 'P']
        expected = ['K', 'W', 'O', 'Z']
        for char, shifted in zip(chars_to_shift, expected):
            self.assertEqual(shifted, caesar.shift_by_key(char))

    def test_that_non_alphabetic_characters_remain_unchanged(self):
        """Checks that non-alphabetical characters remain unchanged."""

        non_letters = punctuation + digits + whitespace
        caesar = Caesar(8)
        for char in non_letters:
            self.assertEqual(char, caesar.shift_by_key(char))
