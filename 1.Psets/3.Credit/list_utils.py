def add_numbers_in_list(list_to_total) -> int:
	"""Returns the total got from adding up all numbers in the list"""
	total = 0
	for number in list_to_total:
		total += number
	return total


def split_double_digits_into_singles(list_to_split) -> list[int]:
	"""Returns a new list in which all double-digit numbers in the provided list
	have been split into single-digit numbers.
	The new list maintains the order of digits in the provided list.

	[1, 23, 7] returns [1, 2, 3, 7], and
	[11, 34, 8] returns [1, 1, 3, 4, 8]"""

	single_digits = []
	for number in list_to_split:
		if number > 9:
			
			# add left half of two-digit number
			single_digits.append(number//10)
			
			# add right half of two-digit number
			single_digits.append(number % 10)
		else:
			single_digits.append(number)
	return single_digits


def double_numbers_in_list(list_to_multiply) -> list:
	"""Returns a new list that is a result of multiplying every element
	in the provided list by 2."""
	doubled_list = []
	for number in range(0, len(list_to_multiply)):
		doubled_list.append(list_to_multiply[number] * 2)
	return doubled_list


def get_every_other_from_end(list_to_split, starting_index) -> list:
	"""Returns a list that is a result of getting every other element--starting
	from some negative index, going backwards--in the provided list.

	If the starting index is -2 (the second-last index) then:
	[1, 2, 3, 4, 5, 6] returns [1, 3, 5], and
	[7, 8, 9, 19] returns [7, 9].

	If the starting index is -1 (the last index) then:
	[1, 2, 3, 4, 5, 6] returns [2, 4, 6], and
	[7, 8, 9, 19] returns [7, 9]."""

	every_other_from_end = []
	list_length = len(list_to_split)

	# Do not go beyond the first element, when looking backwards
	# The + 1 is for the sake of the range() function
	stop_index = -(list_length + 1)
	skip = -2

	for index in range(starting_index, stop_index, skip):
		every_other_from_end.append(list_to_split[index])
	every_other_from_end.reverse()

	return every_other_from_end


def remove_spaces(string_to_compact: str) -> str:
	"""Takes a string with whitespaces, and returns the same string without
	whitespaces."""

	compact_string = ""
	for character in string_to_compact:
		if character not in " ":
			compact_string += character

	return compact_string
