from credit import number_contains_errors
from credit import make_single_numbers
import unittest


class CreditCardChecker(unittest.TestCase):

	def test_catching_errors_in_number(self):
		# Checks that invalid characters within the number are caught
		self.assertFalse(number_contains_errors("3782 82246 310005"))
		self.assertTrue(number_contains_errors("3782 /82246 310005"))
		self.assertFalse(number_contains_errors("378 282 246 310 005"))
		self.assertTrue(number_contains_errors("378_282246 310005"))

	def test_spaces_discarded_after_parsing(self):
		# Checks that whitespace is discarded after parsing
		self.assertIsInstance(make_single_numbers("378 282 246 310 005")[3], int)
		self.assertEqual(make_single_numbers("378      282 246 310 005")[3], 2)
