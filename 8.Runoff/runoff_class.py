import candidate_class as candidate


class Runoff:
    """Represents a runoff voting scenario."""

    def __init__(self, candidates_names: list[str], voter_number: int) -> None:
        self.candidates: dict[str] = {}
        self.populate_candidates(candidates_names)
        self.candidate_count = len(self.candidates)
        self.voter_count = voter_number
        self.voter_prefs = [[] for x in range(0, voter_number)]

    def populate_candidates(self, list_of_names: list[str]) -> None:
        """Creates candidates, and populates the candidates list, using the
        provided list of names."""

        for name in list_of_names:
            this_candidate = candidate.Candidate(name)
            self.candidates[name] = this_candidate

    def get_preferences_and_cast_votes(self) -> None:
        """Stores each voter's preferences for all candidates."""

        voters = list(range(0, self.voter_count))
        rank_numbers = list(range(0, self.candidate_count))

        for voter in voters:
            for rank in rank_numbers:
                name = input(f"Rank {rank + 1}: ")
                if self.candidate_is_valid(name):
                    self.vote(voter, name)

    def vote(self, voter: int, name: str) -> None:
        """Records preference if vote is valid."""

        self.voter_prefs[voter].append(name)

    def tabulate(self):
        """Tabulate votes for non-eliminated candidates."""

        pass

    def candidate_is_valid(self, candidate_name: str) -> bool:
        """Returns whether this candidate is valid."""

        return candidate_name in self.candidates.keys()

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
