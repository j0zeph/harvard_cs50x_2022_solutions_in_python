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
