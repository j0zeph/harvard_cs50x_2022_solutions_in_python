#!/usr/bin/env python3

import re
import list_utils


class CreditCardChecker:

	def __init__(self, card_number):
		self.credit_as_string = card_number
		self.credit_as_number_list = self.make_into_ints()

	def has_errors(self) -> bool:
		"""Checks whether this credit card number contains invalid characters.
		Spaces are allowed"""

		has_invalid_character = False
		found = re.search("[a-zA-Z/*+_{}()-/!@#$%^&=`~<>?|]", self.credit_as_string)
		if found:
			has_invalid_character = True
		return has_invalid_character

	def make_into_ints(self) -> list:
		"""Returns a list of integers after parsing the string
		that represents this credit card number.
		Returns an empty list if the string contains invalid characters"""

		list_of_ints = []
		if not self.has_errors():
			for item in self.credit_as_string:
				if item == " ":
					continue
				else:
					try:
						list_of_ints.append(int(item))
					except ValueError:
						print("There was an error in the provided number.")
						print("Please try again.\n")
						break
			return list_of_ints
		else:
			return []

	def split_by_every_other_from_end(self) -> None:
		pass

	def is_valid_credit_card_number(self) -> bool:
		"""Returns whether or not this credit card number provided is a valid one"""
		pass

	def get_card_issuer(self):
		"""Returns the card issuer(if any), of this valid credit card"""
		pass
