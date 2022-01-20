import plurality_class as plurality
import sys

MAX_CANDIDATES = plurality.Plurality().MAX_CANDIDATES


def main():
    show_possible_argv_warnings()
    voting_method = plurality.Plurality()

    while True:
        voter_number = input("Number of voters: ")
        if not voter_number_is_valid(voter_number):
            print("{}{}".format("\t", show_message("invalid voter number")))
        else:
            break

    voting_method.voter_number = int(voter_number)
    candidates = sys.argv[1: len(sys.argv)]
    voting_method.populate_candidates(candidates)
    voting_method.run_plurality()
    voting_method.print_winner()


def show_possible_argv_warnings():
    if len(sys.argv) < 2:
        exit(show_message("usage"))


def voter_number_is_valid(voter_number: str) -> bool:
    """Checks that there is a positive number of voters, and
    that the number entered is numeric"""

    try:
        return int(voter_number) >= 0
    except ValueError:
        return False


def show_message(message_type: str):
    warnings = {
        "usage": "Usage: python plurality.py [candidate ...]",
        "max candidates": f"Maximum number of candidates is {MAX_CANDIDATES}",
        "invalid voter number": "Invalid voter number. Try again."
    }
    return warnings[message_type]


if __name__ == "__main__":
    main()
