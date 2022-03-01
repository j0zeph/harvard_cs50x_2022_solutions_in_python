#include <iostream>
#include <string>

using namespace std;

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each candidate_pair has a winner, loser
struct candidate_pair
{
    int winner;
    int loser;
};

// Array of candidates
string candidates[MAX];

// changed to `candidate_pair` because the gcc compiler
// insisted that `pair` was too ambiguous.
candidate_pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        cout << "Usage: tideman [candidate ...]\n";
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        cout << "Maximum number of candidates is " << MAX << "\n";
        return 2;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = 0;
    cout << "Number of voters: ";
    cin >> voter_count;

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name;
            cout << "Rank " << j + 1 << ": ";
            cin >> name;

            if (!vote(j, name, ranks))
            {
                cout << "Invalid vote.\n";
                return 3;
            }
        }

        record_preferences(ranks);

        cout << "\n";
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // make sure name is valid
    for (int i = 0; i < candidate_count; i++)
    {
        if (name == candidates[i])
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i; j < candidate_count; j++)
        {
            // A candidate cannot be preferred over themselves
            if (i == j)
                preferences[i][j] = 0;
            else
            {
                // Add one more person who prefers candidate i over j
                preferences[ranks[i]][ranks[j]] += 1;
            }
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // The useful part of the preferences array is always
    // (candidate_count * candidate_count).
    for (int i = 0; i < candidate_count; i++)
    {
        candidate_pair this_pair;

        // Avoid repeating pairs, and the i == j case
        for (int j = i + 1; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                // winner is candidate i
                this_pair.winner = i;
                this_pair.loser = j;

                pairs[pair_count] = this_pair;
                pair_count++;
            }

            else if (preferences[i][j] < preferences[j][i])
            {
                // winner is candidate j
                this_pair.winner = j;
                this_pair.loser = i;

                pairs[pair_count] = this_pair;
                pair_count++;
            }

            else
                // Do nothing for a tie between pairs
                continue;
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    return;
}
