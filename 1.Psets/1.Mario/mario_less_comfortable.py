#!/usr/bin/env python3

def main():
    while True:
        height = input("Height: ")
        proceed_to_print = check_height_is_valid(height)
        if proceed_to_print:
            print_pyramid(int(height))
            break


def check_height_is_valid(height) -> bool:
    """Checks if the height entered is between 1 and 8 inclusive."""
    try:
        h = int(height)
        return h >= 1 and h <= 8
    except ValueError:
        return False


def print_pyramid(height: int) -> None:
    """Prints a pyramid of stars, depending on the given height."""
    for row in range(1, height+1):
        print("{}{}".format(" " * (height - row), "#" * row))


if __name__ == "__main__":
    main()
