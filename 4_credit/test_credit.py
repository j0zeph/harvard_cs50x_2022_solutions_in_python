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


class ListUtilsChecker(unittest.TestCase):

	def test_double_digit_lists_become_singles(self):
		"""Checks if a list with double-digit numbers in it, is properly
		transformed into a list where the double digits have been split into
		their single-digit components, and added back appropriately"""
		self.assertEqual([1, 2, 8, 3, 5, 1, 0], lu.split_double_digits_into_singles
																			([12, 8, 35, 10]))
		self.assertEqual([1, 2], lu.split_double_digits_into_singles([12]))
		self.assertEqual([], lu.split_double_digits_into_singles([]))

	def test_doubling_each_element(self):
		"""Checks if every element in the list is doubled.
		Assumption: elements in this list are numbers"""
		self.assertEqual([2, 4, 6, 8], lu.double_numbers_in_list([1, 2, 3, 4]))
