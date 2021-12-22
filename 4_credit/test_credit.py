from credit import CreditCardChecker as ccc
import unittest
import list_utils as lu


class CreditCardChecker(unittest.TestCase):

	def test_faulty_numbers_return_empty_list_of_ints(self):
		"""Checks that an empty list is returned when a faulty credit card number
		attempts to turn into a list of integers"""
		self.assertEqual([], ccc("3782 /82246 310005").make_into_ints())
		self.assertEqual([], ccc("378 282246 310005_").make_into_ints())
		self.assertNotEqual([], ccc("5499 7400 0000 0057").make_into_ints())

	def test_spaces_discarded_after_parsing(self):
		"""Checks that white-spaces are discarded after parsing"""
		self.assertIsInstance(ccc("378 282 246 310 005").make_into_ints()[3], int)
		self.assertIsInstance(ccc("378  282  246 310 005").make_into_ints()[3], int)

	def test_valid_and_invalid_credit_card_numbers(self):
		"""Checks that valid and invalid credit card numbers are reported
		properly"""
		valid_cards = [
			"5499 7400 0000 0057",
			"378282246310005",
			"5105 1051 0510 5100"]

		for card in valid_cards:
			card = ccc(card)
			self.assertTrue(card.is_valid_credit_card_number())

		invalid_cards = [
			"6011 1811 1111 1817",
			"6011601160116612",
			"370300000000002"]

		for card in invalid_cards:
			card = ccc(card)
			self.assertFalse(card.is_valid_credit_card_number())


class ListUtilsChecker(unittest.TestCase):

	def test_double_digit_lists_become_singles(self):
		"""Checks if a list with double-digit numbers in it, is properly
		transformed into a list where the double digits have been split into
		their single-digit components, and added back appropriately"""

		split_list = lu.split_double_digits_into_singles([12, 8, 35, 10])
		self.assertEqual([1, 2, 8, 3, 5, 1, 0], split_list)
		self.assertEqual([1, 2], lu.split_double_digits_into_singles([12]))
		self.assertEqual([], lu.split_double_digits_into_singles([]))

	def test_doubling_each_element(self):
		"""Checks if every element in the list is doubled.
		Assumption: elements in this list are numbers"""
		self.assertEqual([2, 4, 6, 8], lu.double_numbers_in_list([1, 2, 3, 4]))

	def test_getting_every_other_from_some_negative_index(self):
		"""Checks that every other number, looking backwards (starting from the
		second-last element in the list), is returned properly"""

		every_othered_list = lu.get_every_other_from_end([6, 7, 8, 9, 10], -2)
		self.assertEqual([7, 9], every_othered_list)
		self.assertEqual([], lu.get_every_other_from_end([], -1))

		input_list = list("5499740000000057")
		every_othered_list = lu.get_every_other_from_end(input_list, -2)
		expected_list = ['5', '9', '7', '0', '0', '0', '0', '5']
		self.assertEqual(expected_list, every_othered_list)

	def test_getting_every_other_then_doubling(self):
		"""Gets every other element going backwards, then doubles them"""

		input_list = [2, 4, 5, 6, 7, 9]
		every_othered = lu.get_every_other_from_end(input_list, -2)
		doubled = lu.double_numbers_in_list(every_othered)
		self.assertEqual([4, 10, 14], doubled)
