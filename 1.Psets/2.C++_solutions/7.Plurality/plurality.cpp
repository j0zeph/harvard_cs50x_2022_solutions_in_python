#include <iostream>
#include <string>
#include <limits>

using namespace std;

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
struct candidate
{
    string name;
    int votes;
};

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        cout << "Usage: plurality [candidate ...]\n";
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        cout << "Maximum number of candidates is " << MAX << endl;
        return 2;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count;
    cout << "Number of voters: ";
    cin >> voter_count;

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name;
        cout << "Vote: ";
        cin >> name;

        // Check for invalid vote
        if (!vote(name))
        {
            cout << "Invalid vote.\n";
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].name == name)
        {
            candidates[i].votes += 1;
            return true;
        }
    }

    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int maxVote = numeric_limits<int>::min();
    int currentVote;

    // Find the highest vote
    for (int i = 0; i < candidate_count; i++)
    {
        currentVote = candidates[i].votes;

        if (currentVote > maxVote)
            maxVote = currentVote;
    }

    // Print winners
    for (int i = 0; i < candidate_count; i++)
    {
        currentVote = candidates[i].votes;

        if (currentVote == maxVote)
            cout << candidates[i].name << endl;
    }
}