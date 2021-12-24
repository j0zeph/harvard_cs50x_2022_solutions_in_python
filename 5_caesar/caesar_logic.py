from sys import argv
import caesar_utils as cutils
from string import ascii_lowercase, ascii_uppercase


class Caesar:

    def __init__(self, key_to_shift_by):
        self.key = key_to_shift_by
        self.ascii_of_a = 97
        self.ascii_of_A = 65

    def shift_by_key(self, char) -> str:
        """Returns a string that represents a character, which is a result of
        shifting the provided char by `key` times."""

        # do not shift non-letters
        if not char.isalpha():
            return char

        key = self.key
        ascii_of_char = ord(char)
        value_of_a = self.ascii_of_A if char.isupper() else self.ascii_of_a

        shifted_char = (((ascii_of_char + key) - value_of_a) % 26) + value_of_a

        return chr(shifted_char)
