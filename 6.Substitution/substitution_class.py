import substitution_utils


class Substitution:

    def __init__(self):
        self.key: str = ""
        self.plaintext: str = ""
        self.ciphertext: str = ""
        self.alphabet = substitution_utils.ALPHABET

    def get_substitution(self, key: str, plaintext: str) -> None:
        """Enciphers the given plaintext using the given key, by way of
        substitution, and returns the ciphertext"""

        for char in plaintext:

            # Do not encipher a non-alphabetic character.
            if char not in self.alphabet:
                self.ciphertext += char
            else:
                # Find the char's location in the alphabet
                index = self.alphabet.index(char.lower())

                # Find the corresponding char in that same location within the
                # key, while preserving case.
                if char.isupper():
                    self.ciphertext += self.key[index].upper()
                else:
                    self.ciphertext += self.key[index].lower()

    def get_ciphertext(self) -> str:
        """Returns the ciphertext."""
        return self.ciphertext

    def set_plaintext(self, plaintext: str) -> None:
        self.plaintext = plaintext
