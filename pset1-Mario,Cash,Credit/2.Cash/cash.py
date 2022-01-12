#!/usr/bin/env python3

def main():
	while True:
		change_asked = input("Change owed: ")
		proceed = check_valid_change(change_asked)
		if proceed:
			change_in_cents = get_cents(float(change_asked))
			minimum_coins_used = get_min_coins_to_make_change(change_in_cents)
			break
	print(minimum_coins_used)


def check_valid_change(change_to_check) -> bool:
	"""Checks that the change provided is a positive number"""
	try:
		change = float(change_to_check)
		return change >= 0
	except ValueError:
		return False


def get_cents(dollar_value: float) -> int:
	"""Returns the rounded equivalent amount of change, in cents"""
	return round(dollar_value * 100)


def get_min_coins_to_make_change(total_cents: int) -> int:
	"""Returns the minimum number of coins (quarters, dimes, nickels, cents),
	that it would take to make the total number of cents provided"""

	# dictionary of the value (in cents) of a quarter, dime, nickel, and cent
	coin_type = {"quarter": 25, "dime": 10, "nickel": 5, "cent": 1}
	total_coins_used = 0
	change_remaining = total_cents

	while not change_remaining == 0:

		if not (change_remaining // coin_type["quarter"] == 0):
			quarters_used = change_remaining // coin_type["quarter"]
			total_coins_used += quarters_used
			change_remaining -= quarters_used * coin_type["quarter"]

		elif not (change_remaining // coin_type["dime"] == 0):
			dimes_used = change_remaining // coin_type["dime"]
			total_coins_used += dimes_used
			change_remaining -= dimes_used * coin_type["dime"]

		elif not (change_remaining // coin_type["nickel"] == 0):
			nickels_used = change_remaining // coin_type["nickel"]
			total_coins_used += nickels_used
			change_remaining -= nickels_used * coin_type["nickel"]

		else:
			cents_used = change_remaining // coin_type["cent"]
			total_coins_used += cents_used
			change_remaining -= cents_used * coin_type["cent"]

	return total_coins_used


if __name__ == "__main__":
	main()
