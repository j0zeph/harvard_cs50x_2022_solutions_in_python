#include <cctype>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

const int EXPECTED_ARGS = 2;
const int ALPHABET_LEN = 26;

bool keyIsValid(string key, int keyLen);
char substitute(char ch, string key);

int main(int argc, char *argv[])
{
    // Check for correct number of commandline arguments.
    if (argc != EXPECTED_ARGS)
    {
        cout << "Usage: ./substitution key" << endl;
        return 1;
    }

    string key = argv[1];
    int keyLen = static_cast<int>(key.length());

    if (!keyIsValid(key, keyLen))
       return 1; 

    string plaintext = "";
    cout << "plaintext: ";
    getline(cin, plaintext);

    int plainLen = static_cast<int>(plaintext.length());

    cout << "ciphertext: ";

    for (int i = 0; i < plainLen; i++)
        cout << substitute(plaintext[i], key);

    cout << endl;

    return 0;
}


// Returns whether the key is valid.
bool keyIsValid(string key, int keyLen)
{
    if (keyLen != ALPHABET_LEN)
    {
        cout << "Key must contain 26 characters." << endl;
        return false;
    }

    // Check that key has only alphabetical characters.
    for (int i = 0; i < keyLen; i++)
    {
        if (!isalpha(key[1]))
        {
            cout << "Key must contain only alphabetic characters.";
            return false;
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
                return false;
            }
        }
    }

    return true;
}


char substitute(char ch, string key)
{
    // Leave non-alphabetical characters unchanged
    if (!isalpha(ch))
        return ch;
    else
    {
        bool chIsUpper = isupper(ch);

        // Get the alphabetical index of the provided char.
        int alphaIndex = chIsUpper ? (ch - 'A') : (ch - 'a');

        // substitute this char with its counterpart in the key,
        // while preserving case.
        char keyString = key[alphaIndex];

        char keyChar = chIsUpper ? (toupper(keyString)) : (tolower(keyString));

        return keyChar;
    }
}
