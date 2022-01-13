"""
Coleman-Liau index

index = 0.0588 * L - 0.296 * S - 15.8
where:
L - average number of letters per 100 words.
S - average number of sentences per 100 words.
"""

import readability
import unittest


class ReadabilityTest(unittest.TestCase):

    def test_correct_letter_count(self):
        """Checks that when given a text, the correct number of letters is
        counted."""

        texts_and_counts = {
            "There are no hot-dogs aside the table! Where are they?": 42,
            "Where? What? When? and, Who?": 19,
            "*&^%$##    !!!a": 1,
            "The quick brown __ fox, Jumps!": 21,
            "~`!@#$%^&*()_+1234567890-=": 0
        }
        
        for text, count in texts_and_counts.items():
            letter_count = readability.count_letters(text)
            self.assertEqual(letter_count, count)

    def test_correct_word_count(self):
        """Checks that when given a text, the correct number of words are
        counted.

        Assumption: A word is any sequence of characters that is separated by
        a space."""

        texts_and_word_counts = {
            "": 0,
            "    ": 0,
            "Here,there,everywhere,and,nowhere": 1,
            "       Still                ": 1,
            "Here, there, everywhere. But nowhere at all!!": 7,

            "A large class of computational problems involve the determination "
            "of properties of graphs, digraphs, integers, arrays of integers, "
            "finite families of finite sets, boolean formulas and elements of "
            "other countable domains.": 31,

            "!!! ### &&&": 3
        }

        for text, word_count in texts_and_word_counts.items():
            words_in_text = readability.count_words(text)
            self.assertEqual(words_in_text, word_count)

    def test_correct_sentence_count(self):
        """Checks that when given a text, the correct number of sentences are
        counted."""

        texts_and_sentence_counts = {
            "Here, there, everywhere... But nowhere at all!!!": 2,

            "A large class of computational problems involve the determination "
            "of properties of graphs, digraphs, integers, arrays of integers, "
            "finite families of finite sets, boolean formulas and elements of "
            "other countable domains.": 1,

            "We will count this as a sentence": 1,


        }

        for text, sentence_count in texts_and_sentence_counts.items():
            sentences_in_text = readability.count_sentences(text)
            self.assertEqual(sentences_in_text, sentence_count)