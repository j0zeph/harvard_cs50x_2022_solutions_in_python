import plurality_class as pclass
import unittest


class PluralityTest(unittest.TestCase):

    def setUp(self) -> None:
        self.plurality = pclass.Plurality()

    def test_that_multiple_winners_are_printed(self):
        candidates = ["Alice", "Bob", "Charlie"]
        self.plurality.populate_candidates(candidates)
        votes_to_cast = {
            "Alice": 4,
            "Bob": 4,
            "Charlie": 2,
        }

        for candidate, votes in votes_to_cast.items():
            votes_left = votes
            while votes_left > 0:
                self.plurality.vote(candidate)
                votes_left -= 1

        winners = ["Alice", "Bob"]
        self.assertEqual(winners, self.plurality.get_winner())
