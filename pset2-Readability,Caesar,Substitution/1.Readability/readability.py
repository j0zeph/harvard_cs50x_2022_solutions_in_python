#!/usr/bin/env python3

import re


def get_text() -> str:
    """Gets (as user input), the text whose reading level is to be determined"""

    text = input("Text: ")
    return text


def count_letters(text: str) -> int:
    """Counts the letters in the provided text"""

    letter_count = 0

    for char in text:
        if re.match(r"[A-Za-z]", char):
            letter_count += 1

    return letter_count
