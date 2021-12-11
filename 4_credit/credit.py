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
