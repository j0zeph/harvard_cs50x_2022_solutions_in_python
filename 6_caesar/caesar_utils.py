def get_ascii_value(self, character):
    """Returns the ASCII value of the character provided."""
    return ord(character)


def argv_is_valid(argv):
    """Returns whether or not the commandline arguments provided are valid."""
    try:
        correct_length = len(argv) == 2
        second_arg_is_numeric = argv[1].isnumeric()
        return correct_length and second_arg_is_numeric
    except IndexError:
        return False


def remind_user_of_usage():
    """Prints a reminder of the correct usage of the script"""
    print("Usage: python caesar.py key")
