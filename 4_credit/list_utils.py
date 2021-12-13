def add_numbers_in_list(list_to_total) -> int:
	"""Returns the total got from adding up all numbers in the list"""
	total = 0
	for number in list_to_total:
		total += number
	return total


def split_double_digits_into_singles(list_to_split) -> list:
	"""Returns a new list in which all double digit numbers have been split
	into separate, single-digit numbers. 12 becomes 1 and 2, for example"""

	single_digits = []
	for number in list_to_split:
		if number > 9:
			single_digits.append(number//10)  # add left half of two-digit number
			single_digits.append(number % 10)  # add right half of two-digit number
		else:
			single_digits.append(number)
	return single_digits

def double_numbers_in_list(list_to_multiply) -> list:
	"""Returns a new list that is a result of multiplying every element
	in the provided list."""
	doubled_list = []
	for number in range(0, len(list_to_multiply)-1):
		doubled_list.append(list_to_multiply[number] * 2)
	return doubled_list