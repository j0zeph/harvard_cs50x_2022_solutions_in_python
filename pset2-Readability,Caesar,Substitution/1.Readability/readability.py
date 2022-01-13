#!/usr/bin/env python3

import re


def main():
    text = input("Text: ")


def count_letters(text: str) -> int:
    """Counts the letters in the provided text"""

    letter_count = 0

    for char in text:
        if re.match(r"[A-Za-z]", char):
            letter_count += 1

    return letter_count


if __name__ == '__main__':
    main()