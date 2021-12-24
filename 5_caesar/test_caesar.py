import unittest
from caesar_logic import Caesar


class CaesarTesting(unittest.TestCase):

    def test_shifting_lower_case_letters_by_a_small_amount(self):
        """Checks that shifting a lower case letter by a small amount gives the
        correct result, while preserving case."""

        caesar = Caesar(5)
        chars_to_shift = ['a', 'm', 'f', 'k', 'u']
        expected = ['f', 'r', 'k', 'p', 'z']
        for char, shifted in zip(chars_to_shift, expected):
            self.assertEqual(shifted, caesar.shift_by_key(char))
