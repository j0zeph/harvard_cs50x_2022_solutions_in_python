class Plurality:
    """Represents a voting scenario."""

    def __init__(self):
        self.MAX_CANDIDATES = 9
        self.candidates_list: dict[str, int] = {}
        self.voter_number = 0

    def vote(self, name: str) -> None:
        """Adds one vote for this candidate"""

        self.candidates_list[name] += 1

    def populate_candidates(self, candidates_list: list[str]) -> None:
        """Takes a list, and creates a model of candidates with votes from
        it."""

        for name in candidates_list:
            self.candidates_list.setdefault(name, 0)

    def run_plurality(self):
        """Initiates the voting process by asking for what candidate
        to vote for."""

        for voter in range(0, self.voter_number):
            candidate_to_vote = input("Vote: ")
            if candidate_to_vote not in self.candidates_list.keys():
                print("Invalid vote.")
            else:
                self.vote(candidate_to_vote)

    def print_winner(self) -> None:
        """Print winners"""

        for winner in self.get_winner():
            print(winner)

    def get_winner(self) -> list:
        """Gets the winner/winners of the plurality voting process.
        Should multiple winners exist, they are all returned."""

        winners = set()

        # Sort votes from large to small.
        sorted_votes = sorted(self.candidates_list.items(), key=lambda x: x[1],
                              reverse=True)

        # add everyone with the highest vote to the set of winners.
        highest_vote = sorted_votes[0][1]
        for person in sorted_votes:
            if person[1] == highest_vote:
                winners.add(person[0])

        return sorted(winners)

