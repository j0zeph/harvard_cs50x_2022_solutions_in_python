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
