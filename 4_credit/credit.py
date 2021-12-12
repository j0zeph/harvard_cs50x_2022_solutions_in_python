#!/usr/bin/env python3

import re


def number_contains_errors(number) -> bool:
	"""Checks whether the number provided has any non-numeric characters in it.
	Spaces do not count as invalid."""

	has_invalid = False
	found = re.search("[a-zA-Z/*+_{}()-/!@#$%^&=`~<>?|]", number)
	if found:
		has_invalid = True
	return has_invalid


def make_single_numbers(string_to_parse) -> list:
	"""Returns a list of integers, as a result of parsing the provided string"""
	parsed_list = []
	for item in string_to_parse:
		if item == " ":
			continue
		else:
			try:
				parsed_list.append(int(item))
			except ValueError:  # In case an invalid character was missed.
				print("There was an error in the provided number.")
				print("Please try again.\n")
				break
	return parsed_list


def twice_every_other_from_second_last(list) -> list:
	"""Returns a new list of numbers that are the result of multiplying
	every other number in the provided list--starting from the second last
	number--by 2"""
	pass
