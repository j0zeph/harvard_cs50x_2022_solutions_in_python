import sys

CORRECT_ARGV_LENGTH = 2
CORRECT_KEY_LENGTH = 26


def main():
    if not(len(sys.argv) == CORRECT_ARGV_LENGTH):
        exit(show_error("usage"))
    elif not(len(sys.argv[1]) == CORRECT_KEY_LENGTH):
        exit(show_error("key length"))


def show_error(message_type: str) -> str:
    """Returns the error message that is associated with the
    provided message type."""

    messages = {
        "usage": "Usage: python substitution.py key",
        "key length": f"Key must contain {CORRECT_KEY_LENGTH} characters.",
    }

    return messages[message_type]


if __name__ == "__main__":
    main()
