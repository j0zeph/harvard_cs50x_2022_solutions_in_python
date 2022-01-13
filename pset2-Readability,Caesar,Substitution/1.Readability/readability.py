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


def count_words(text: str) -> int:
    """Counts the number of words in the provided text.\n
    Assumptions:
        1.The text will not start or end with a space.\n
        2.Words will be separated by a single space.\n
        3.The sentence will not have multiple consecutive spaces in row.\n
    """

    """Splitting the text by `Zero or more non-word characters, that are followed by 
    one or more spaces.` 
    Non-word characters are those not in the range [A-Za-z0-9_]"""

    list_of_words_in_text = re.split(r"\W? +", text)
    return len(list_of_words_in_text)


if __name__ == '__main__':
    main()