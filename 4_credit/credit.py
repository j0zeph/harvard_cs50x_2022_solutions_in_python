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
			parsed_list.append(int(item))
	return parsed_list

