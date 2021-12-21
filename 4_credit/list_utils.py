def add_numbers_in_list(list_to_total) -> int:
	"""Returns the total got from adding up all numbers in the list"""
	total = 0
	for number in list_to_total:
		total += number
	return total


def split_double_digits_into_singles(list_to_split) -> list:
	"""Returns a new list in which all double-digit numbers have been split
	into single-digit numbers, and put back into the list, at the
	appropriate positions. [1|23|7] becomes [1|2|3|7], for example"""

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
	in the provided list."""
	doubled_list = []
	for number in range(0, len(list_to_multiply)):
		doubled_list.append(list_to_multiply[number] * 2)
	return doubled_list


def get_every_other_from_end(list_to_split, starting_index) -> list:
	"""Returns a list that is a result of getting every other element--starting
	from the starting index, going backwards--in the provided list.
	If the starting index is -2 (the second-last index), [1, 2, 3, 4, 5, 6]
	returns [1, 3, 5].
	[1, 2, 3, 4, 5, 6] returns [2, 4, 6] if the starting index is -1 (the
	last index)"""

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
