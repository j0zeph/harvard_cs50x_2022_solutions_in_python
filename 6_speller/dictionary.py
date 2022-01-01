#!/usr/bin/env python3

loaded_words = set()


def load(dictionary) -> bool:
    """Loads all the words from a dictionary file into word_dictionary.
    Returns True if loading was successful, False otherwise."""
    try:
        with open(dictionary, encoding="utf-8") as word_dict:
            for word in word_dict:
                loaded_words.add(word)
        return True
    except FileNotFoundError:
        return False


def hash_function():
    """Was supposed to be `hash()`, but that method name shadowed an in-built
    Python name.

    Function unimplemented because Python's set provides hashing under the
    hood."""
    pass


def size() -> int:
    """Returns how many words are in the dictionary."""
    
    return len(loaded_words)


def check(word):
    """Checks if a word is in the dictionary."""

    return word in loaded_words


def unload():
    """Method unimplemented because python unloads automatically"""
    pass
