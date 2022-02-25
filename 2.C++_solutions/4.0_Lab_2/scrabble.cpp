#include <ctype.h>
#include <iostream>
#include <string>

using namespace std;

// Points assigned to each letter of the alphabet
int POINTS[] = {
    1, 3, 3, 2, 1, 4,
    2, 4, 1, 8, 5, 1, 
    3, 1, 1, 3, 10, 1, 
    1, 1, 1, 4, 4, 8, 
    4, 10
    };

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1, word2;

    cout << "Player 1: ";
    cin >> word1;

    cout << "Player 2: ";
    cin >> word2;

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    if (score1 == score2)
        cout << "Tie!";
    else if (score1 > score2)
        cout << "Player 1 wins!";
    else
        cout << "Player 2 wins!";

}

int compute_score(string word)
{
    int score = 0;
    int len = word.length();

    for (char ch: word)
    {
        if (!isalpha(ch))
            continue;
        else
            score += POINTS[(tolower(ch) - 'a')];
    }

    return score;
}
