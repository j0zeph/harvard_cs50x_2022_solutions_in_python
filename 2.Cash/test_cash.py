import unittest
from cash import get_min_coins_to_make_change
from cash import get_cents
from cash import check_valid_change


class MinimumCoinsForChangeTest(unittest.TestCase):

	def test_round_decimals(self):
		"""Checks that decimal inputs give expected results after rounding
		up or down"""

		self.assertEqual(get_min_coins_to_make_change(get_cents(2.75)), 11)
		self.assertEqual(get_min_coins_to_make_change(get_cents(2.0068)), 9)
		self.assertEqual(get_min_coins_to_make_change(get_cents(0.009)), 1)

	def test_negative_change_returns_false(self):
		"""Checks that negative inputs are ignored"""

		self.assertFalse(check_valid_change(-10))
		self.assertFalse(check_valid_change(-0.1111))

	def test_correct_minimum_coins_returned_generally(self):
		"""Checks that when given a range of change, the correct minimum
		number of coins required is returned."""

		change_and_coins = {
			5.5: 22,
			17.3: 70,
			25.1: 101,
			43.678: 179,
			100.189: 406,
			1000: 4000,
			1000.777: 4006,
			1000000000: 4000000000,
		}

		for change, coins in change_and_coins.items():
			change_in_cents = get_cents(change)
			min_coins = get_min_coins_to_make_change(change_in_cents)
			self.assertEqual(coins, min_coins)
