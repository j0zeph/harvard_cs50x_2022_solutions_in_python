#!/usr/bin/env python3

def main():
    greet(input("What is your name? "))


def greet(name: str) -> None:
    """"Says hello to user, using their name in the greeting"""

    print("\nHello {}\n".format(name))


if __name__ == "__main__":
    main()
