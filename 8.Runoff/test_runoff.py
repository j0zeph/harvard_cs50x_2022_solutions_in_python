import candidate_class as candidate
import runoff_class as runoff
import unittest


class TestRunoff(unittest.TestCase):

    def setUp(self) -> None:
        self.candidates = ["Marta", "Joni", "Fran", "Linda"]
        self.voter_number = 5
        self.model = runoff.Runoff(self.candidates, self.voter_number)

    def test_that_candidates_are_populated_correctly(self):
        candidate_names = self.model.candidates.keys()
        for name, person in zip(self.candidates, candidate_names):
            self.assertEqual(name, person)

    def test_that_invalid_candidates_are_caught(self):
        """Checks that the candidate being voted for is in the list of
        valid candidates"""

        people_validity = {
            "Marta": True,
            "Benoit": False,
            "Joni": True,
            "Ransom": False,
        }

        model = self.model

        for person, validity in people_validity.items():
            self.assertEqual(validity, model.candidate_is_valid(person))

    def test_that_voter_preferences_are_recorded_correctly(self):
        voter_num = self.voter_number
        votes_cast = [
            ["Marta", "Joni", "Fran", "Linda"],
            ["Joni", "Marta", "Fran", "Linda"],
            ["Joni", "Marta", "Linda", "Fran"],
            ["Marta", "Joni", "Fran", "Linda"],
            ["Marta", "Fran", "Linda", "Joni"],
        ]

        for voter_index in range(0, voter_num):
            for name in votes_cast[voter_index]:
                self.model.vote(voter_index, name)

        expected = votes_cast
        self.assertEqual(expected, self.model.voter_prefs)

    def test_that_votes_are_tabulated_correctly(self):
        voter_num = self.voter_number
        votes_cast = [
            ["Marta", "Joni", "Fran", "Linda"],
            ["Joni", "Marta", "Fran", "Linda"],
            ["Linda", "Marta", "Joni", "Fran"],
            ["Marta", "Joni", "Fran", "Linda"],
            ["Marta", "Fran", "Linda", "Joni"],
        ]

        for voter_index in range(0, voter_num):
            for name in votes_cast[voter_index]:
                self.model.vote(voter_index, name)

        self.model.tabulate()

        expected = {"Marta": 3, "Joni": 1, "Fran": 0, "Linda": 1}
        actual = self.model.candidates.values()
        for vote, candidate_vote in zip(expected.values(), actual):
            self.assertEqual(vote, candidate_vote.votes)
