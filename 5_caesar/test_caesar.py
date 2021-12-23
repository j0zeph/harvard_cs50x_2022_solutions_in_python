import unittest
from caesar_logic import Caesar


class CaesarTesting(unittest.TestCase):

    def test_shifting_by_a_small_amount(self):
        """Checks that shifting by a small amount gives the correct result.
        Shifting preserves case."""

        caesar = Caesar(5)
        chars_to_shift = ['a', 'm', 'f', 'k', 'u']
        expected = ['f', 'r', 'k', 'p', 'z']
        for char, shifted in zip(chars_to_shift, expected):
            self.assertEqual(shifted, caesar.shift_by_key(char))
