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

    def test_correct_reading_grade_is_returned(self):
        """Checks that when given a text, the correct reading grade is
        returned, as per the Coleman-Liau index"""

        texts_and_grades = {
            "One fish. Two fish. Red fish. Blue fish.": "Before Grade 1",

            "Would you like them here or there? I would not like them here or "
            "there. I would not like them anywhere.": "Grade 2",
            
            "Congratulations! Today is your day. You're off to Great Places! "
            "You're off and away!": "Grade 3",

            "Harry Potter was a highly unusual boy in many ways. For one "
            "thing, he hated the summer holidays more than any other time of "
            "year. For another, he really wanted to do his homework, but was "
            "forced to do it in secret, in the dead of the night. And he also "
            "happened to be a wizard.": "Grade 5",

            "In my younger and more vulnerable years my father gave me some "
            "advice that I've been turning "
            "over in my mind ever since.": "Grade 7",

            "Alice was beginning to get very tired of sitting by her sister "
            "on the bank, and of having nothing to do: once or twice she had "
            "peeped into the book her sister was reading, but it had no "
            "pictures or conversations in it, \"and what is the use of a "
            "book,\" thought Alice \"without "
            "pictures or conversation?\"": "Grade 8",
            
            "When he was nearly thirteen, my brother Jem got his arm badly "
            "broken at the elbow. When it healed, and Jem's fears of never "
            "being able to play football were assuaged, he was seldom "
            "self-conscious about his injury. His left arm was somewhat "
            "shorter than his right; when he stood or walked, the back of his "
            "hand was at right angles to his body, his thumb parallel to his "
            "thigh.": "Grade 8",

            "There are more things in Heaven and Earth, Horatio, than are "
            "dreamt of in your philosophy.": "Grade 9",

            "It was a bright cold day in April, and the clocks were striking "
            "thirteen. Winston Smith, his chin nuzzled into his breast in an "
            "effort to escape the vile wind, slipped quickly through the glass "
            "doors of Victory Mansions, though not quickly enough to prevent a "
            "swirl of gritty dust from entering along with him.": "Grade 10",

            "A large class of computational problems involve the determination "
            "of properties of graphs, digraphs, integers, arrays of integers, "
            "finite families of finite sets, boolean formulas and elements of "
            "other countable domains.": "Grade 16+",
        }

        for text, reading_grade in texts_and_grades.items():

            chars = readability.count_letters(text)
            words = readability.count_words(text)
            sentences = readability.count_sentences(text)

            index = readability.get_index(chars, words, sentences)
            grade = readability.get_grade(index)
            self.assertEqual(grade, reading_grade)
