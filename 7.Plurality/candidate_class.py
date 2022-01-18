
class Candidate:
    """Represents a candidate in a voting scenario.

    A candidate has a name and a vote count.
    """

    def __init__(self, name: str, votes: int = 0):
        self.name = ""
        self.votes = votes

    def vote(self) -> None:
        self.votes += 1
