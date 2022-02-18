
#include <cctype>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

const int LETTERS_IN_ALPHABET = 26;
const int valueOfUpperA = 65;
const int valueOfLowerA = 97;

char substitute(char ch, string key[]);

int main(int argc, char *argv[])
{
    // Check for correct number of commandline arguments.
    if (argc != 2)
    {
        cout << "Usage: ./substitution key" << endl;
        return 1;
    }

    string key = argv[1];
    int keyLen = static_cast<int>(key.length());

    // Check the key has 26 characters.
    if (keyLen != LETTERS_IN_ALPHABET)
    {
        cout << "Key must contain 26 characters." << endl;
        return 1;
    }

    // Check that key has only alphabetical characters.
    for (int i = 0; i < keyLen; i++)
    {
        if (!isalpha(key[1]))
        {
            cout << "Key must not contain non-alphabetic characters.";
            return 1;
        }
    }

    // Check that key has no duplicate letters while ignoring case.
    for (int i = 0; i < keyLen - 1; i++)
    {
        for (int j = i + 1; j < keyLen; j++)
        {
            if (tolower(key[i]) == tolower(key[j]))
            {
                cout << "Key must not contain duplicate letters." << endl;
                return 1;
            }
        }
    }

    string plaintext = "";

    // Get the plaintext, and encipher it.
    cout << "plaintext: ";
    getline(cin, plaintext);

    cout << "ciphertext: ";

    int plainLen = static_cast<int>(plaintext.length());

    for (int i = 0; i < plainLen; i++)
    {
        char ch = plaintext[i];

        // Leave non-alphabetical characters unchanged
        if (!isalpha(ch))
        {
            cout << ch;
        }
        else
        {
            bool chIsUpper = isupper(ch);

            // Get the alphabetical index of the provided char, depending
            // on whether or not the char is uppper or lower case.
            int alphaIndex = chIsUpper ? (ch - valueOfUpperA) : (ch - valueOfLowerA);

            // substitute this char with its counterpart in the key,
            // while preserving case.
            char keyString = key[alphaIndex];

            char keyChar = chIsUpper ? (toupper(keyString)) : (tolower(keyString));

            cout << keyChar;
        }
    }

    cout << endl;

    return 0;
}
