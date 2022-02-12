class Caesar:

    def __init__(self, key_to_shift_by):
        self.key = key_to_shift_by
        self.ascii_of_a = 97
        self.ascii_of_A = 65

    def shift_by_key(self, char) -> str:
        """Returns a string that represents a character, which is a result of
        shifting the provided char by `key` times, using the equation:
        Ci = (Pi + key) % 26 where;
        Ci is the `alphabetical index` of enciphered character,
        Pi is the `alphabetical index` of the plain-text character.

        Here, the `alphabetical index` is a mapping where a=0, b=1, ..., z=25

        The equation has been modified to first convert the plain-text
        character to its ASCII value, then shift by the key provided,
        then convert that to its `alphabetical index` then convert that back
        to the ASCII value, and return the character that is represented by
        this ASCII value.

        Case is preserved throughout this conversion."""

        if not char.isalpha():
            return char

        key = self.key
        ascii_of_char = ord(char)
        value_of_a = self.ascii_of_A if char.isupper() else self.ascii_of_a

        shifted_char = (((ascii_of_char + key) - value_of_a) % 26) + value_of_a

        return chr(shifted_char)
