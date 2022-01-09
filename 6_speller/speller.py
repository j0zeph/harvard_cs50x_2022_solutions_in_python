"""
The python code here tries to match the C implementation (given as distribution
code) as closely as possible.
"""

import time
import re
from sys import argv, exit
from dictionary import load, size, check, unload
MAX_LENGTH_OF_WORD = 45

# Default dictionary
DICTIONARY = "dictionaries/large"

# Check for correct number of args
if (not len(argv) == 2) and (not len(argv) == 3):
    print("Usage: python3 speller.py [DICTIONARY] text")
    exit(1)

time_to_load, time_to_check_word, time_to_check_length = 0.0, 0.0, 0.0

# Determine what dictionary to use
dictionary = DICTIONARY if len(argv) == 2 else argv[1]

# Load dictionary
time_before_load = time.process_time()
loaded = load(dictionary)
time_after_load = time.process_time()

if not loaded:
    print("Could not load dictionary.")
    exit(1)

time_to_load = time_after_load - time_before_load

# Try to open the text
text = argv[2] if len(argv) == 3 else argv[1]
try:
    text_to_check = open(text, "r", encoding="utf-8")
    text_to_check.close()
except FileNotFoundError:
    print("Could not open {}".format(text))
    exit(1)

# Prepare to report misspellings.
print("\nMISSPELLED WORDS\n")

# Prepare to spell-check
index, misspellings, words = 0, 0, 0
word = ""


with open(text, "r", encoding="utf-8") as text:
    # Spell check each word in the text
    # Allow only alphabetical characters and apostrophes
    while True:

        char = text.read(1)
        if not char:
            # We are at the end of the file
            break

        if re.match(r"[A-Za-z']", char):
            # Append character to word
            word += char
            index += 1

            # Ignore alphabetical strings that are too long to be words
            # by consuming the rest of this string.
            if index > MAX_LENGTH_OF_WORD:

                while True:
                    # Read one more character
                    char = text.read(1)
                    if not (char or (re.match(r"[A-Za-z]", char))):
                        break

                index, word = 0, ""

        # Ignore words with numbers (like MS Word can)
        # by consuming the rest of this string
        elif char.isdigit():
            while True:
                # Read one more character
                char = text.read(1)
                if not char or (not char.isalpha() and not char.isdigit()):
                    break

                index, word = 0, ""

        # We have fond the whole word
        elif index > 0:

            words += 1

            # time how long it takes to check if a word is misspelled
            before_word_check = time.process_time()
            misspelled = not check(word)
            after_word_check = time.process_time()

            # Update benchmark
            time_to_check_word += (after_word_check - before_word_check)

            # Print the misspelled word
            if misspelled:
                print(word)
                misspellings += 1

            index, word = 0, ""

# time how long it takes to check the length of the loaded dictionary
before_length_check = time.process_time()
length = size()
after_length_check = time.process_time()
time_to_check_length = after_length_check - before_length_check

# time how long it takes to unload the dictionary (no implementation needed)
before_unload = time.process_time()
unloaded = unload()
after_unload = time.process_time()
time_to_unload = after_unload - before_unload

# calculate the total time for all benchmarks
total_time = time_to_load + time_to_check_word + time_to_check_length + \
             time_to_unload


# Report benchmarks
print(f"\nWORDS MISSPELLED:    {misspellings}")
print(f"\nWORDS IN DICTIONARY: {length}")
print(f"\nWORDS IN TEXT:       {words}")
print(f"\nTIME IN load:        {time_to_load:.2f}")
print(f"\nTIME IN check:       {time_to_check_word:.2f}")
print(f"\nTIME IN size:        {time_to_check_length:.2f}")
print(f"\nTIME IN unload:      {time_to_unload:.2f}")
print(f"\nTIME IN TOTAL:       {total_time:.2f}")
