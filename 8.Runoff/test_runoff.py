import candidate_class as candidate
import runoff_class as runoff
import unittest


class TestRunoff(unittest.TestCase):

    def setUp(self) -> None:
        self.candidates = ["Marta", "Joni", "Fran", "Linda"]
        self.voter_number = 5
        self.model = runoff.Runoff(self.candidates, self.voter_number)
        self.votes_to_cast = [
            ["Marta", "Joni", "Fran", "Linda"],
            ["Joni", "Marta", "Fran", "Linda"],
            ["Linda", "Marta", "Joni", "Fran"],
            ["Marta", "Joni", "Fran", "Linda"],
            ["Marta", "Fran", "Linda", "Joni"],
        ]

        # cast votes
        for voter_index in range(0, self.voter_number):
            for name in self.votes_to_cast[voter_index]:
                self.model.vote(voter_index, name)

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
        """Checks that ranks of candidates chosen by each voter are
        accurately recorded."""

        expected = self.votes_to_cast
        self.assertEqual(expected, self.model.voter_prefs)

    def test_that_votes_are_tabulated_correctly(self):
        """Checks that the vote counts for the highest preference candidates
        are updated accurately."""

        self.model.tabulate()

        expected = {"Marta": 3, "Joni": 1, "Fran": 0, "Linda": 1}
        actual = self.model.candidates.values()
        for vote, candidate_vote in zip(expected.values(), actual):
            self.assertEqual(vote, candidate_vote.votes)

    def test_that_the_smallest_vote_is_reported_correctly(self):
        """Checks that the smallest number of votes that any remaining (
        non-eliminated) candidates is returned."""

        self.model.tabulate()

        # Fran has no votes.
        expected_minimum = 0

        self.assertEqual(expected_minimum, self.model.find_minimum())

        votes_to_cast = [
            ["Marta", "Joni", "Fran", "Linda"],
            ["Joni", "Marta", "Fran", "Linda"],
            ["Linda", "Marta", "Joni", "Fran"],
            ["Fran", "Joni", "Marta", "Linda"],
            ["Marta", "Fran", "Linda", "Joni"],
        ]

        # reset voter prefs
        self.model.voter_prefs = [[] for x in range(0, self.voter_number)]

        # cast votes
        for voter_index in range(0, self.voter_number):
            for name in votes_to_cast[voter_index]:
                self.model.vote(voter_index, name)

        self.model.tabulate()

        expected_minimum = 1

        self.assertEqual(expected_minimum, self.model.find_minimum())

    def test_that_a_tied_election_is_recognized(self):
        voter_number = 3
        self.model = runoff.Runoff(self.candidates, voter_number)

        votes_to_cast = [
            ["Joni", "Marta", "Fran", "Linda"],
            ["Fran", "Marta", "Fran", "Linda"],
            ["Joni", "Linda", "Joni", "Fran"],
        ]

        # Artificially eliminate Joni
        self.model.candidates["Joni"].eliminated = True

        # cast votes
        for voter_index in range(0, voter_number):
            for name in votes_to_cast[voter_index]:
                self.model.vote(voter_index, name)
        minimum_vote = self.model.find_minimum()

        # Marta has 0 votes
        self.assertEqual(minimum_vote, 0)

        self.assertTrue(self.model.is_tie(minimum_vote))

        # reset

        new_candidates = ["Joni", "Marta", "Meg", "Fran", "Linda", "Ransom"]
        new_voter_number = 4
        self.model = runoff.Runoff(new_candidates, new_voter_number)

        votes_to_cast = [
            ["Joni", "Marta", "Meg", "Fran", "Linda", "Ransom"],
            ["Fran", "Joni", "Ransom", "Marta", "Meg", "Linda"],
            ["Joni", "Linda", "Marta", "Ransom", "Fran", "Meg"],
            ["Meg", "Linda", "Joni", "Marta", "Ransom", "Fran"],
        ]

        # cast votes
        for voter_index in range(0, new_voter_number):
            for name in votes_to_cast[voter_index]:
                self.model.vote(voter_index, name)

        # Artificially eliminate Joni and Fran
        self.model.candidates["Joni"].eliminated = True
        self.model.candidates["Fran"].eliminated = True

        self.model.tabulate()

        minimum_vote = self.model.find_minimum()

        # Joni and Fran's 0 votes do not count, because they are eliminated.
        self.assertEqual(minimum_vote, 1)

        self.assertTrue(self.model.is_tie(minimum_vote))

