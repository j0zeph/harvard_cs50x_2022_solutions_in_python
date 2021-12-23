from sys import argv
import caesar_utils as cutils
from string import ascii_lowercase, ascii_uppercase


class Caesar:

    def __init__(self, key):
        self.key = key

    def shift_by_key(self, char) -> str:
        """Returns a string that represents a char, which is a result of
        shifting the provided char by `key` times."""
        pass
