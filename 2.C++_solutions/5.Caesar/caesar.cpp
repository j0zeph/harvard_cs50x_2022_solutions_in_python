#include <cctype>
#include <iostream>
#include <string>

using namespace std;

bool onlyDigits(int argc, char *argv[]);
char rotate (char ch, int n);

const int valueOfUpperA = 65;
const int valueOfLowerA = 97;

int main(int argc, char *argv[])
{
    string plaintext = "";

    if (!(onlyDigits(argc, argv)))
    {
        cout << "Usage: ./caesar key";
        return 1;
    }
    
    int key = stoi(argv[1]);

    cout << "Plaintext: ";
    getline(cin, plaintext);
    
    cout << "Ciphertext: ";

    // Rotate each character in the plaintext by the key
    string::size_type length = plaintext.length();

    for (int i = 0; i < static_cast<int>(length); i++)
        cout << rotate(plaintext[i], key);
    
    cout << endl;

    return 0;
}

// Returns whether the command-line arguments provided
// are valid.
bool onlyDigits(int argc, char *argv[])
{
    if (!(argc == 2))
        return false;
    
    // Check that the key is numeric.
    string key = argv[1];
    string::size_type length = key.length();

    for (int i = 0; i < static_cast<int>(length); i++)
        if (!isdigit(key[i]))
            return false;
    
    return true;
}

/*
Returns a char that is a result of shifting the provided char
n times, while ensuring the shifting wraps around the alphabet
appropriately.
*/
char rotate (char ch, int n)
{
    // Leave non-alphabetical characters unchanged
    if (!isalpha(ch))
        return ch;
    
    int valueOfa = (isupper(ch)) ? valueOfUpperA : valueOfLowerA; 

    return (((ch + n) - valueOfa) % 26) + valueOfa;
}