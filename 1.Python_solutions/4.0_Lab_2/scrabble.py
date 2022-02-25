#!/usr/bin/env python3

# Points assigned to each letter of the alphabet
points = [
    1, 3, 3, 2, 1, 4, 
    2, 4, 1, 8, 5, 1, 
    3, 1, 1, 3, 10, 1, 
    1, 1, 1, 4, 4, 8, 
    4, 10,
    ]


def main() -> None:
    # Get input words from both players
    word1 = input("Player 1: ")
    word2 = input("Player 2: ")

    # Score both words
    score1 = compute_score(word1)
    score2 = compute_score(word2)

    if score1 == score2:
        print("Tie")
    elif score1 > score2:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


def compute_score(word: str) -> int:
    """Returns a score, which is a result of adding up the
       scrabble points of each alphabetical letter in the provided word."""

    score = 0

    for letter in word:
        if not (letter.isalpha()):
            continue
        else:
            score += ord(letter.lower())
    
    return score


if __name__ == "__main__":
    main()
