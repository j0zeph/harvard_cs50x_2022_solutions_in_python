#!/usr/bin/env python3

def main():
	while True:
		height = input("Height: ")
		proceed_to_print = check_height_is_valid(height)
		if proceed_to_print:
			print_pyramid(int(height))
			break


def check_height_is_valid(height) -> bool:
	"""Checks if the height entered is between 1 and 8 inclusive."""

	try:
		h = int(height)
		return h >= 1 and h <= 8
	except ValueError:
		return False


def print_pyramid(height: int) -> None:
	"""Prints a pyramid of stars, depending on the given height."""

	middle_spaces = 2

	for row in range(1, height + 1):
		left_spaces = " " * (height - row)
		
		# hashes are mirrored on both sides
		left_hashes = right_hashes = "#" * (height - (height - row))
		middle = " " * middle_spaces
		print("{}{}{}{}".format(left_spaces, left_hashes, middle, right_hashes))


if __name__ == "__main__":
	main()
