import runoff_class as runoff
import sys

MAX_VOTERS = 100
MAX_CANDIDATES = 9


def main():
    show_possible_argv_warnings()
    voters = input("Number of voters: ")
    if not is_valid_voter_number(voters):
        exit(show_warning("max voters"))
    voters = int(voters)

    candidate_names = sys.argv[1: len(sys.argv)]

    model = runoff.Runoff(candidate_names, voters)

    for voter in list(range(0, voters)):
        for rank in list(range(0, len(candidate_names))):

            name = input(f"Rank {rank + 1}: ")

            if not model.candidate_is_valid(name):
                exit(show_warning("invalid vote"))
            model.vote(voter, name)
        print()

    # Keep holding runoffs until a winner exists
    while True:
        model.tabulate()

        winner_present = model.print_winner()
        if winner_present:
            break

        minimum_vote = model.find_minimum()
        tie = model.is_tie(minimum_vote)

        # If tie, everyone wins
        if tie:
            for name in model.candidates:
                print(name)
            break

        # Eliminate candidates with the minimum vote
        model.eliminate(minimum_vote)


def show_possible_argv_warnings():
    """Checks for invalid commandline usage."""

    if len(sys.argv) < 2:
        exit(show_warning("usage"))

    candidates = sys.argv[1: len(sys.argv)]

    if len(candidates) > MAX_CANDIDATES:
        exit(show_warning("max candidates"))


def is_valid_voter_number(voter_number: str) -> bool:
    """Checks that there is a positive number of voters, and
    that the number entered is numeric"""

    try:
        voters = int(voter_number)
        return 0 <= voters <= MAX_VOTERS
    except ValueError:
        return False


def show_warning(message_type: str) -> str:
    """"Returns a specific warning, depending on the context that has been
    provided."""

    warnings = {
        "usage": "Usage: python runoff.py [candidate ...]",
        "max candidates": f"Maximum number of candidates is {MAX_CANDIDATES}",
        "max voters": f"Maximum number of voters is {MAX_VOTERS}",
        "invalid vote": "Invalid vote.",
    }

    return warnings[message_type]


if __name__ == "__main__":
    main()
