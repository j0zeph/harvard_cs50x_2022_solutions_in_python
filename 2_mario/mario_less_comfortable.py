#!/usr/bin/env python3

def main():
    while True:
        height = get_height_of_pyramid()
        proceed_to_print = check_height_is_valid(height)
        if proceed_to_print:
            print_pyramid(height)
            break


def get_height_of_pyramid() -> str:
    """"Gets the height of the pyramid to print."""
    height = input("Height: ")
    return height


def check_height_is_valid(height) -> bool:
    """Checks if the height entered is between 1 and 8 inclusive."""
    try:
        to_check = int(height)
        if (not (to_check > 0)) or (not (to_check <= 8)):
            return False
        else:
            return True
    except ValueError:
        return False


def print_pyramid(height) -> None:
    """Prints a pyramid of stars, depending on the given height."""
    for row in range(1, int(height)+1):
        print("*"*row)


if __name__ == "__main__":
    main()
