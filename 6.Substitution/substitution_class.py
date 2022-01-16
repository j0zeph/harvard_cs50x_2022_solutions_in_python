import substitution_utils


class Substitution:

    def __init__(self):
        self.key = ""
        self.plaintext = ""
        self.ciphertext = ""
        self.alphabet = substitution_utils.ALPHABET

    def encipher(self) -> None:
        """Enciphers the given plaintext using the given key, by way of
        substitution, and returns the ciphertext"""

        for char in self.plaintext:

            # Do not encipher a non-alphabetic character.
            if char.lower() not in self.alphabet:
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
        return self.ciphertext

    def set_plaintext(self, plaintext: str) -> None:
        self.plaintext = plaintext

    def set_key(self, key: str) -> None:
        self.key = key

    def clear_ciphertext(self) -> None:
        """Empties stored ciphertext"""
        self.ciphertext = ""
