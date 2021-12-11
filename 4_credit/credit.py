#!/usr/bin/env python3

def number_contains_errors(number) -> bool:
	"""Checks whether the number provided has any non-numeric characters in it.
	Spaces do not count as invalid."""

	invalid_characters = "(){}/*+-!@#$%^&_=`~,.?\\\"\'/;:|"
	has_invalid = False
	for character in number:
		if character in invalid_characters:
			has_invalid = True

	return has_invalid
