import unittest
import substitution_class as substitution


class SubstitutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.key_lower = "gtkylxjuzicpmnaqvowsehfrdb"
        self.sub = substitution.Substitution()

    def test_that_case_is_preserved_when_enciphering(self):

        plain_and_cipher = {
            "This is almost CS50.": "Suzw zw gpmaws KW50."
        }

        for plain, enciphered in plain_and_cipher.items():
            self.sub.set_plaintext(plain)
            self.sub.set_key(self.key_lower)
            self.sub.encipher()
            self.assertEqual(self.sub.get_ciphertext(), enciphered)

    def test_that_upper_lower_and_mixed_case_keys_encipher_the_same(self):
        pass

    def test_that_symbols_are_not_enciphered(self):
        pass


