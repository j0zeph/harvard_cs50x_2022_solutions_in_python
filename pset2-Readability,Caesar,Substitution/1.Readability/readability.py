#!/usr/bin/env python3

import re


def main():
    # Keep prompting if an empty string was provided.
    while True:
        text = input("Text: ")

        if len(text) > 0:
            break
    letter_count = count_letters(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)

    print(get_grade(get_index(letter_count, word_count, sentence_count)))


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

    """Splitting the text by `Zero or more non-word characters, that are 
    followed by one or more spaces.` 
    Non-word characters are those not in the range [A-Za-z0-9_]"""

    word_list = re.split(r"\W? +", text.strip())

    # Make sure that after stripping a string of only spaces, the empty string
    # left (if any) counts as zero words, and not 1 word.
    if (len(word_list) == 1) and (word_list[0] in ""):
        return 0

    return len(word_list)


def count_sentences(text: str) -> int:
    """Counts the number of sentences in the provided text.\n
    Assumptions:
    1.Any period, exclamation point, or question mark denotes then end
    of a sentence\n
    """

    sentence_list = re.split(r"[.!?]+", text)

    # Make sure that there are no empty strings left over in the sentence list.
    filtered_list = list(filter(lambda x: len(str(x)) > 0, sentence_list))

    return len(filtered_list)


def get_index(chars: int, words: int, sentences: int) -> int:
    """Returns the reading grade(using the Coleman-Liau index), given the\n
    number of characters, words, and sentences in a text.\n\n

    index = 0.0588 * L - 0.296 * S - 15.8 where:
        L - average number of letters per 100 words.
        S - average number of sentences per 100 words."""

    L = chars / (words / 100)
    S = sentences / (words / 100)

    return round((0.0588 * L) - (0.296 * S) - 15.8)


def get_grade(index: int) -> str:
    """Returns a reading grade, depending on the provided Coleman-Liau index"""

    # Set of grades from 1 to 15.
    one_to_fifteen = set(grade for grade in range(1, 16))

    if index < 1:
        return "Before Grade 1"
    elif index in one_to_fifteen:
        return "Grade " + str(index)
    else:
        return "Grade 16+"


if __name__ == '__main__':
    main()
