#!/usr/bin/env python3

import re
import list_utils as lu


class CreditCardChecker:

    def __init__(self, card_number):
        self.credit_as_string = card_number
        self.credit_as_number_list = self.make_into_ints()

    def has_errors(self) -> bool:
        """Checks whether this credit card number contains errors.
        Spaces are allowed within the number.
        An empty card number is an error.
        A card number with invalid characters is an error."""

        if len(str(self.credit_as_string).strip()) == 0:
            return True

        invalid_characters = "[a-zA-Z/*+_{}()-/!@#$%^&=`~<>?|]"
        found = re.search(invalid_characters, self.credit_as_string)
        if found:
            return True
        return False

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
                    list_of_ints.append(int(item))
            return list_of_ints
        else:
            return []

    def is_valid_credit_card_number(self) -> bool:
        """Returns whether or not this credit card number provided is valid"""

        credit_number_as_list = self.credit_as_number_list

        if len(credit_number_as_list) == 0:
            return False

        every_other = lu.get_every_other_from_end(credit_number_as_list, -2)
        every_other_doubled = lu.double_numbers_in_list(every_other)
        singles_made = lu.split_double_digits_into_singles(every_other_doubled)
        singles_summed = lu.add_numbers_in_list(singles_made)

        un_multiplied = lu.get_every_other_from_end(credit_number_as_list, -1)
        un_multiplied_summed = lu.add_numbers_in_list(un_multiplied)

        final_sum = singles_summed + un_multiplied_summed

        return final_sum % 10 == 0

    def get_card_issuer(self) -> str:
        """Returns the card issuer(if any), of this valid credit card.
        Where no issuer exists, INVALID is returned"""

        # issuers listed in the format
        # (starting digit, (possible length of card number)): "ISSUER"
        issuers = {
            (3, (15,)): "AMEX",
            (5, (16,)): "MASTERCARD",
            (4, (13, 16)): "VISA"}

        card_number_length = len(self.credit_as_number_list)

        if card_number_length == 0:
            return "INVALID"

        leading_number = self.credit_as_number_list[0]

        for key in issuers:
            leading_number_matches = leading_number in key
            length_matches = card_number_length in key[1]
            if leading_number_matches and length_matches:
                return issuers[key]

        return "INVALID"


def main():
    while True:
        card_number = input("Enter a credit card number: ")
        if not CreditCardChecker(card_number).has_errors():
            break
        else:
            print("INVALID")

    card = CreditCardChecker(card_number)

    if not card.is_valid_credit_card_number():
        print("INVALID")
    else:
        print(card.get_card_issuer())


if __name__ == "__main__":
    main()
