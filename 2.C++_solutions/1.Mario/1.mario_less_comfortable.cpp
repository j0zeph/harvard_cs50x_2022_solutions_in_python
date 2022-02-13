#include <iostream>
#include <limits>

using namespace std;

int main(void)
{
    int height;

    do
    {
        cout << "Height: ";
        cin >> height;
        
        // ignore faulty input
        if(!cin)
        {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }
    while (!(height >= 1 && height <= 8));

    int spaces;
    int hashes;


    for (int row = 0; row < height; row++)
    {
        spaces = height - (row + 1);

        while (spaces > 0)
        {
            cout << " ";
            spaces--;
        }

        hashes = (row + 1);

        while (hashes > 0)
        {
            cout << "#";
            hashes--;
        }

        cout << endl;
    }
    return 0;
}