import unittest
from cash import get_min_coins_to_make_change
from cash import get_cents
from cash import check_valid_change


class MinimumCoinsForChangeTest(unittest.TestCase):

	def test_round_decimals(self):
		# Test that decimal inputs give expected results after rounding up or down
		self.assertEqual(get_min_coins_to_make_change(get_cents(2.75)), 11)
		self.assertEqual(get_min_coins_to_make_change(get_cents(2.0068)), 9)
		self.assertEqual(get_min_coins_to_make_change(get_cents(0.009)), 1)

	def test_negative_change_returns_false(self):
		# Test that negative inputs are ignored
		self.assertFalse(check_valid_change(-10))
		self.assertFalse(check_valid_change(-0.1111))

