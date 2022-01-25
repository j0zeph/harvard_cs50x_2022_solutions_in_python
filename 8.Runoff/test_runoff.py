import candidate_class as candidate
import runoff_class as runoff
import unittest


class TestRunoff(unittest.TestCase):

    def setUp(self) -> None:
        self.candidates = ["Marta", "Joni", "Fran", "Linda"]
        self.voter_number = 5
        self.voting_model = runoff.Runoff(self.candidates, self.voter_number)

    def test_that_candidates_are_populated_correctly(self):

        for index in range(0, len(self.candidates)):
            person = self.voting_model.candidates[index]
            name = self.candidates[index]
            self.assertEqual(person.name, name)

    def test_that_invalid_candidates_are_caught(self):
        """Checks that the candidate being voted for is in the list of
        valid candidates"""

        people_validity = {
            "Marta": True,
            "Benoit": False,
            "Joni": True,
            "Ransom": False,
        }

        model = self.voting_model

        for person, validity in people_validity.items():
            self.assertEqual(validity, model.candidate_is_valid(person))
