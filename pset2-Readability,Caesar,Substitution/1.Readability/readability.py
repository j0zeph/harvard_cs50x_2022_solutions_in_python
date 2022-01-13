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

    word_list = re.split(r"\W? +", text.strip())

    empty_string = ("",)

    # Make sure that after stripping a string of only spaces, the empty string
    # left (if any) counts as zero words, and not 1 word.
    if (len(word_list) == 1) and (word_list[0] in empty_string):
        return 0
    return len(word_list)


if __name__ == '__main__':
    main()