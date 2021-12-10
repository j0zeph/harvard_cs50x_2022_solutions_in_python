#!/usr/bin/env python3

def main():
    greet(get_name())


def get_name() -> str:
    """"Returns the name that the user entered"""
    name = input("What is your name? ")
    return name


def greet(name) -> None:
    """"Says hello to user, using their name in the greeting"""
    print("\nHello {}\n".format(name))


if __name__ == "__main__":
    main()
