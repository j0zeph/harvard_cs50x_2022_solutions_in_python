class Candidate:
    """A candidate has a name, votes, and an `eliminated` status."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.votes = 0
        self.eliminated = False


class Runoff:
    """Represents a runoff voting scenario."""

    def __init__(self, candidates_names: list[str], voter_number: int) -> None:
        self.candidates: dict[str, Candidate] = {}
        self.populate_candidates(candidates_names)
        self.voter_count = voter_number
        self.voter_prefs = [[] for x in range(0, voter_number)]

    def populate_candidates(self, list_of_names: list[str]) -> None:
        """Creates candidates, and populates the candidates list, using the
        provided list of names."""

        for name in list_of_names:
            this_candidate = Candidate(name)
            self.candidates[name] = this_candidate

    def vote(self, voter: int, name: str) -> bool:
        """Records preference if vote is valid."""

        if self.candidate_is_valid(name):
            self.voter_prefs[voter].append(name)
            return True
        return False

    def tabulate(self):
        """Tabulate votes for non-eliminated candidates."""

        # Update the vote count of candidates, based on voter preferences.
        for preference in self.voter_prefs:
            for name in preference:

                # update candidate's vote count, if they have not been
                # eliminated.
                # Move to the next preferred candidate otherwise.
                if not self.candidates[name].eliminated:
                    self.candidates[name].votes += 1
                    break
                else:
                    continue

    def candidate_is_valid(self, candidate_name: str) -> bool:
        """Returns whether this candidate is valid."""

        return candidate_name in self.candidates.keys()

    def is_tie(self, minimum: int) -> bool:
        """Returns whether the election is tied between all candidates."""

        for person in self.candidates.values():
            if (not person.votes == minimum) and (not person.eliminated):
                return False
        return True

    def find_minimum(self) -> int:
        """Returns the minimum number of votes any remaining candidate has."""

        # sort candidates by ascending votes
        sorted_votes = sorted(self.candidates.values(), key=lambda x: x.votes)

        # only keep candidates that are not yet eliminated
        minimum_votes = list(filter(lambda x: not x.eliminated, sorted_votes))

        return minimum_votes[0].votes

    def eliminate(self, minimum: int) -> None:
        """Eliminate the candidate (or candidates) in last place."""

        if not self.is_tie(minimum):
            for person in self.candidates.values():
                if person.votes == minimum:
                    person.eliminated = True

    def print_winner(self) -> bool:
        """Print the winner of the election, if there is one."""

        half_the_vote = self.voter_count / 2

        for person in sorted(self.candidates.values(), key=lambda x: x.votes):
            if (not person.eliminated) and (person.votes > half_the_vote):
                print(person.name)
                return True
        return False

