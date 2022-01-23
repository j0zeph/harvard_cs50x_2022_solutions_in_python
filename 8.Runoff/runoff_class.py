class Runoff:
    """Represents a runoff voting scenario.

    Note: Instead of a candidate being represented by a class,
    candidate properties are represented as a dictionary of dictionaries.
    """

    def __init__(self):
        pass

    def populate_candidates(self, candidates_list: list[str]) -> None:
        """Populates the candidates dictionary, using the provided list of
        names."""

        pass

    def get_preferences_and_cast_votes(self) -> None:
        """Stores each voter's preferences for all candidates."""

        pass

    def vote(self, voter: int, rank: int, name: str) -> None:
        """Records preference if vote is valid."""

        pass

    def tabulate(self):
        """Tabulate votes for non-eliminated candidates."""

        pass

    def candidate_is_valid(self, candidate_name: str) -> bool:
        """Returns whether this candidate is valid."""

        pass

    def is_tie(self, minimum: int) -> bool:
        """Returns whether the election is tied between all candidates."""

        pass

    def find_minimum(self) -> None:
        """Returns the minimum number of votes any remaining candidate has."""

        pass

    def eliminate(self) -> None:
        """Eliminate the candidate (or candidates) in last place"""

        pass

    def print_winner(self):
        """Print the winner of the election, if there is one."""

        pass

    def run_runoff(self) -> None:
        """Initiates the runoff voting process."""

        pass
