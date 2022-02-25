#include <cctype>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int count_letters(const string text);
int count_words(const string text);
int count_sentences(const string text);
int getColemanLiau(int letters, int words, int sentences);

const double lMultiplier = 0.0588;
const double sMultiplier = 0.296;
const double constRemoved = 15.8;

int main()
{
    string text;

    cout << "Text: ";
    getline(cin, text);

    int letters = count_letters(text);
    int words = count_words(text);
    int sentences =  count_sentences(text);
    int readingIndex = getColemanLiau(letters, words, sentences);

    if (readingIndex < 1)
        cout << "Before Grade 1" << endl;
    else if (readingIndex >= 1 && readingIndex <= 15)
        cout << "Grade " << readingIndex << endl;
    else
        cout << "Grade 16+" << endl;

    return 0;
}

/*
Returns the number of letters in the given string.
*/
int count_letters(const string text)
{
    int letterCount = 0;

    for (char ch: text)
        if (isalpha(ch))
            letterCount++;

    return letterCount;
}

/*
Returns how many words (sequence of characters separated by a space)
there are in the given string.
*/
int count_words(const string text)
{
    int spacesFound = 0;

    for(char ch: text)
        if (ch == ' ')
            spacesFound++;
    
    return spacesFound + 1;
}

/*
Returns how many sentences there are in the provided text.
A period, exclamation point, or a question mark, denote the 
end of a sentence.
*/
int count_sentences(const string text)
{
    int punctsFound = 0;

    for (char ch: text)
        if (ch == '.' || ch == '!' || ch == '?')
            punctsFound++;
    
    return punctsFound;
}

/*
Returns the approximate reading level of the text, (given how many
letters, words, and sentences there are in said text),
using the Coleman-Liau index:

index = 0.0588 * L - 0.296 * S - 15.8
where L is the average number of letters per 100 words in the text,
and S is the average number of sentences per 100 words in the text.
*/
int getColemanLiau(int letters, int words, int sentences)
{
    double L = static_cast<double>(letters) / (static_cast<double>(words)/100);
    double S = static_cast<double>(sentences) / (static_cast<double>(words)/100);

    int index = round((lMultiplier * L) - (sMultiplier * S) - constRemoved);

    return index;
}
