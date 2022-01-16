import sys
import string

CORRECT_ARGV_LENGTH = 2
CORRECT_KEY_LENGTH = 26
ALPHABET = string.ascii_lowercase


def print_any_argv_warnings() -> None:
    """Prints an error message if the commandline argument(s):
        -- Is not the correct length
        -- Has a key whose length is not correct
        -- Has a key containing non_alphabetic characters
    """

    if not(len(sys.argv) == CORRECT_ARGV_LENGTH):
        exit(show_error("usage"))
    if not(len(sys.argv[1]) == CORRECT_KEY_LENGTH):
        exit(show_error("key"))

    key_provided = sys.argv[1]

    for char in key_provided:
        if char not in ALPHABET:
            exit(show_error("alphabet"))


def show_error(message_type: str) -> str:
    """Returns the error message that is associated with the
    provided message type."""

    messages = {
        "usage": "Usage: python substitution.py key",
        "key": f"Key must contain {CORRECT_KEY_LENGTH} characters.",
        "alphabet": "Key must only contain alphabetic characters."
    }

    return messages[message_type]


def get_key() -> str:
    return sys.argv[1]
