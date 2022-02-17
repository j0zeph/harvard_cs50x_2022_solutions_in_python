#include <cctype>
#include <iostream>
#include <string>

using namespace std;

bool onlyDigits(int argc, char *argv[]);

int main(int argc, char *argv[])
{
    if (!(onlyDigits(argc, argv)))
    {
        cout << "Usage: ./caesar key";
        return 1;
    }
    
    return 0;

}

// Returns whether the command-line arguments provided
// are valid.
bool onlyDigits(int argc, char *argv[])
{
    if (!(argc == 2))
        return false;
    
    // Check that the key supplied is numeric, by checking every character of the key.
    string key = argv[1];
    string::size_type length = key.length();

    for (int i = 0; i < static_cast<int>(length); i++)
        if (!isdigit(key[i]))
            return false;
    
    return true;
}