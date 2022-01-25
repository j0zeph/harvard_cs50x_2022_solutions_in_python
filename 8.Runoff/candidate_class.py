class Candidate:
    """A candidate has a name, votes, and an `eliminated` status."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.votes: int = 0
        self.eliminated: bool = False
