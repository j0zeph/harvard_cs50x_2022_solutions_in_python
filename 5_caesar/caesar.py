#!/usr/bin/env python3

import caesar_utils as cu
from sys import argv
from caesar_logic import Caesar


def main():
    check_argv()
    key = argv[1]
    caesar = Caesar(int(key))
    plain_text = input("plaintext: ")
    print("ciphertext: ", end="")

    for char in plain_text:
        print(caesar.shift_by_key(char), end="")
    print()

def check_argv() -> None:
    if not cu.argv_is_valid(argv):
        cu.remind_user_of_usage()
        exit(1)


if __name__ == "__main__":
    main()
