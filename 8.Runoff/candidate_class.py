class Candidate:
    """A candidate has a name, votes, and an `eliminated` status."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.votes = 0
        self.eliminated = False
