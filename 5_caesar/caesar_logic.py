from sys import argv
import caesar_utils as cutils
from string import ascii_lowercase, ascii_uppercase


class Caesar:

    def __init__(self, key_to_shift_by):
        self.key = key_to_shift_by


    def shift_by_key(self, char) -> str:
        """Returns a string that represents a character, which is a result of
        shifting the provided char by `key` times."""

        # do not shift non-letters
        if not char.isalpha():
            return char

        ASCII_value = ord(char)

        shifted_char = (((ASCII_value + self.key) - 97) % 26) + 97
        if char.isupper():
            return chr(shifted_char.upper())
        return chr(shifted_char)
