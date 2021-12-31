import unittest


class DictionaryTester(unittest.TestCase):

    def test_that_dictionary_files_exist_in_expected_path(self):
        """Checks that the dictionary files can be found in their paths."""

        paths_of_dictionaries = ["dictionaries/large", "dictionaries/small"]

        for path in paths_of_dictionaries:
            try:
                with open(path):
                    file_exists = True
            except FileNotFoundError:
                file_exists = False

            self.assertTrue(file_exists)
