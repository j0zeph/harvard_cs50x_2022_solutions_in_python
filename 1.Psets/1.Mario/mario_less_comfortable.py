#!/usr/bin/env python3

def main():
    while True:
        height = input("Height: ")
        if is_valid(height):
            print_pyramid(int(height))
            break


def is_valid(height) -> bool:
    """Checks if the height entered is between 1 and 8 inclusive."""
    try:
        h = int(height)
    except ValueError:
        return False
    else:
        return 1 <= h <= 8


def print_pyramid(height: int) -> None:
    """Prints a pyramid of stars, depending on the given height."""
    for row in range(1, height+1):
        print("{}{}".format(" " * (height - row), "#" * row))


if __name__ == "__main__":
    main()
