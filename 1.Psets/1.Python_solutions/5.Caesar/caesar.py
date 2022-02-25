#!/usr/bin/env python3

from sys import argv
from caesar_class import Caesar


def main():

    if not argv_is_valid(argv):
        exit("Usage: python caesar.py key")

    key = argv[1]
    caesar = Caesar(int(key))
    plain_text = input("plaintext: ")
    print("ciphertext: ", end="")

    for char in plain_text:
        print(caesar.shift_by_key(char), end="")
    print()


def get_ascii_value(self, character):
    """Returns the ASCII value of the character provided."""

    return ord(character)


def argv_is_valid(argv_list):
    """Returns whether or not the commandline arguments provided are valid."""

    try:
        correct_length = len(argv_list) == 2
        second_arg_is_numeric = argv_list[1].isnumeric()
        return correct_length and second_arg_is_numeric
    except IndexError:
        return False


if __name__ == "__main__":
    main()
