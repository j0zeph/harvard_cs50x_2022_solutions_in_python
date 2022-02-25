import unittest
import substitution_class as substitution


class SubstitutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.keys = {
            "key_upper": "GTKYLXJUZICPMNAQVOWSEHFRDB",
            "key_lower": "gtkylxjuzicpmnaqvowsehfrdb",
            "key_mixed": "gTkYLxjuZIcPmNaQvOwSeHfRdB",
        }
        self.sub = substitution.Substitution()

    def test_that_case_is_preserved_when_enciphering(self):
        plain_and_cipher = {
            "This is almost CS50.": "Suzw zw gpmaws KW50.",
            "Almost, bUt not ReaLLy!": "Gpmaws, tEs nas OlgPPd!",
            "ABcdEFghIJklMNopQRstUVwxYZ": "GTkyLXjuZIcpMNaqVOwsEHfrDB",
        }

        for plain, enciphered in plain_and_cipher.items():
            self.sub.clear_ciphertext()
            self.sub.set_plaintext(plain)
            self.sub.set_key(self.keys["key_lower"])
            self.sub.encipher()
            self.assertEqual(self.sub.get_ciphertext(), enciphered)

    def test_that_upper_lower_and_mixed_case_keys_encipher_the_same(self):
        plaintext = "Click inside the Terminal window."
        enciphered = "Kpzkc znwzyl sul Slomzngp fznyaf."

        for value in self.keys.values():
            self.sub.clear_ciphertext()
            self.sub.set_plaintext(plaintext)
            self.sub.set_key(self.keys["key_lower"])
            self.sub.encipher()
            self.assertEqual(self.sub.get_ciphertext(), enciphered)

