import unittest


class DictionaryTester(unittest.TestCase):

    def setUp(self):
        self.dictionary_paths = ["dictionaries/small_modified",
                                 "dictionaries/small",
                                 "dictionaries/small"]
        self.loaded_words = set()

    def test_that_dictionary_files_exist_in_expected_path(self):
        """Checks that the dictionary files can be found in their paths."""

        for path in self.dictionary_paths:
            try:
                with open(path):
                    file_exists = True
            except FileNotFoundError:
                file_exists = False

            self.assertTrue(file_exists)

    def test_that_a_loaded_dictionary_returns_the_correct_size(self):
        """Checks that the loaded dictionary file returns the correct word
        count.
        Assumption: The dictionary contains only one word per line."""

        with open(self.dictionary_paths[0]) as word_dict:
            for line in word_dict:
                self.loaded_words.add(line)

        self.assertEqual(501, len(self.loaded_words))
