import unittest
import scrabble


class ScrabbleTest(unittest.TestCase):

    def setUp(self) -> None:

        # Dictionary whose key and value pair is of the form:
        # (player1 word, player2 word): winner
        # 1 means player1 wins, 2 means player2 wins,
        # 0 means it is a tie
        self.word_pairs = {
            ("Question?", "Question!"): 0,
            ("Oh,", "hai!"): 2,
            ("COMPUTER", "science"): 1,
            ("Scrabble", "wiNNeR"): 1,
            ("&^%!", "*&^()!@"): 0,
        }

    def test_words_are_scored_accurately(self) -> None:

        for word_pair, winner in self.word_pairs.items():
            score1 = scrabble.compute_score(word_pair[0])
            score2 = scrabble.compute_score(word_pair[1])
            result = winner

            if winner == 0:
                self.assertEqual(score1, score2)
            elif winner == 1:
                self.assertGreater(score1, score2)
            else:
                self.assertGreater(score2, score1)
