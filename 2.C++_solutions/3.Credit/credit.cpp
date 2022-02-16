#include <iostream>
#include <string>

using namespace std;

bool cardNumHasErrors(string rawCardNum);
int doubleEveryOtherAndSum(const int cardNumber[], int length, int startIndex);
string getCardIssuer(int cardNumber[], int length);
int getStartingDigits(int cardNumber[]);
bool isValid(const int cardNumber[], int length);
void makeIntoIntArray(string rawCardNum, int forPopulation[], int length);
int sumLeftOverNumbers(const int cardNumber[], int length, int startIndex);
int sumTwoHalves(int num);


int main(void)
{
    string rawCardNum;

    do
    {
        cout << "Number: ";
        cin >> rawCardNum;
    }
    while(cardNumHasErrors(rawCardNum));

    int length = static_cast<int>(rawCardNum.length());
    int cardNum[length];

    makeIntoIntArray(rawCardNum, cardNum, length);

    if (!isValid(cardNum, length))
            cout << "INVALID";
    else
        cout << getCardIssuer(cardNum, length);
}


/*
Checks if the number has characters other than 0 through 9.
*/
bool cardNumHasErrors(const string rawCardNum)
{
    for (int i = 0; i < static_cast<int>(rawCardNum.length()); i++)
    {
        bool greaterOrEqual0 = rawCardNum[i] >= '0';
        bool lessOrEqual9 = rawCardNum[i] <= '9';

        if (!(greaterOrEqual0 && lessOrEqual9))
            return true;
    }

    return false;
}

/*
Checks if a credit card number is valid, using Luhn's algorithm.
*/
bool isValid(const int cardNumber[], int length)
{
    if (!(length == 15 || length == 16 || length == 13))
        return false;
    
    bool isEvenLength = length % 2 == 0;
    int i = (isEvenLength) ? 0 : 1;

    int everyOtherSum = doubleEveryOtherAndSum(cardNumber, length, i);

    // reset i
    i = (isEvenLength) ? 1 : 0;

    int leftOverSum = sumLeftOverNumbers(cardNumber, length, i);

    // check that cardNumber is valid.
    if ((everyOtherSum + leftOverSum) % 10 == 0)
        return true;
    
    return false;
}

/* 
Gets each character in the user-entered credit card number,
and copies that character (as its integer value), into an empty
array of the same length.

The char '2' is copied as the integer 2
*/
void makeIntoIntArray(string rawCardNum, int forPopulation[], int length)
{
    for (int i = 0; i < length; i++)
    {
        forPopulation[i] = static_cast<int>(rawCardNum[i]) - '0';
    }
}


/*
Returns the sum of the two halves of a double-digit number.
*/
int sumTwoHalves(int num)
{
    return (num / 10) + (num % 10);
}


/*
Returns a sum resulting from doubling everyother integer (starting
from "startIndex", up to the end of the provided array),
and summing up those doublings as per Luhn's algorithm.
*/
int doubleEveryOtherAndSum(const int cardNumber[], int length, int startIndex)
{
    int i = startIndex;
    int everyOtherSum = 0;

    while(i < length)
    {
        int byTwo = cardNumber[i] * 2;

        // If multiplication gave a double-digit.
        if (byTwo > 9)
            everyOtherSum += sumTwoHalves(byTwo);
        else
            everyOtherSum += byTwo;
        
        i += 2;
    }

    return everyOtherSum;
}


/*
Returns a sum, resulting from adding up every-other integer,
starting from "startIndex", up to the end of the provided array. 
*/
int sumLeftOverNumbers(const int cardNumber[], int length, int startIndex)
{
    int i = startIndex;
    int leftOverSum = 0;

    while(i < length)
    {
        leftOverSum += cardNumber[i];
        i += 2;
    }

    return leftOverSum;
}


/*
Returns the issuer, if any, of this card.
*/
string getCardIssuer(int cardNumber[], int length)
{
    int cardLength = length;
    int amexStartingDigits[] = {34, 37};
    int masterCardStartingDigits[] = {51, 52, 53, 54, 55};
    int visaStartingDigits[] = {4};

    int startingDigit = getStartingDigits(cardNumber);

    switch(cardLength)
    {
        case 16:
            for(int num: masterCardStartingDigits)
            {
                if (num == startingDigit)
                    return "MASTERCARD\n";
            }

            for(int num: visaStartingDigits)
            {
                if (num == startingDigit)
                    return "VISA\n";
            }   
        case 15:
            for(int num: amexStartingDigits)
            {
                if (num == startingDigit)
                    return "AMEX\n";
            }
        case 13:
            for(int num: visaStartingDigits)
            {
                if (num == startingDigit)
                    return "VISA\n";
            }
        default:
            return "INVALID";
    }
}


/*
Returns the starting digit of the "cardNumber",
which is a result of combining the first two starting digits in "cardNumber".
Returns 4, if the first digit of "cardNumber" is 4.
*/
int getStartingDigits(int cardNumber[])
{
    // special case for VISA cards.
    if (cardNumber[0] == 4)
        return 4;
    
    return (cardNumber[0] * 10) + cardNumber[1];
}
