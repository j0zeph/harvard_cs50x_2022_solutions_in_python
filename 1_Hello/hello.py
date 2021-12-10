#!/usr/bin/env python3

def main():
    greet(get_name())


def get_name():
    name = input("What is your name? ")
    return name


def greet(name):
    print("\nHello {}\n".format(name))


if __name__ == "__main__":
    main()
