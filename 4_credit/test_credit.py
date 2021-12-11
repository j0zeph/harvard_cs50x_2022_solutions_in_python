from credit import number_contains_errors
import unittest


class CreditCardChecker(unittest.TestCase):

	def test_catching_errors_in_number(self):
		# Checks that invalid characters within the number are caught
		self.assertFalse(number_contains_errors("3782 82246 310005"))
		self.assertTrue(number_contains_errors("3782 /82246 310005"))
		self.assertFalse(number_contains_errors("378282246 310005"))
		self.assertTrue(number_contains_errors("378_282246 310005"))
