#include <iostream>
#include <limits>
#include <string>

using namespace std;

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        cout << "Usage: runoff [candidate ...]\n";
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        cout << "Maximum number of candidates is " << MAX_CANDIDATES << "\n";
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    cout << "Number of voters: ";
    cin >> voter_count;

    if (voter_count > MAX_VOTERS)
    {
        cout << "Maximum number of voters is " << MAX_VOTERS << "\n";
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {
        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name;
            cout << "Rank " << j + 1 << ": ";
            cin >> name;

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                cout << "Invalid vote.\n";
                return 4;
            }
        }

        cout << "\n";
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    cout << candidates[i].name << "\n";
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // check that the name is of a candidate
    for (int i = 0; i < candidate_count; i++)
    {
        if (name.compare(candidates[i].name) == 0)
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    for (int row = 0; row < voter_count; row++)
    {
        for (int col = 0; col < candidate_count; col++)
        {
            // Index of the candidate in the preferences array
            int candidate = preferences[row][col];

            if (!candidates[candidate].eliminated)
            {
                candidates[candidate].votes += 1;
                break;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    bool winner_found = false;
    int half_the_votes = voter_count / 2;
    for (int i = 0; i < candidate_count; i++)
    {
        // make a pointer to work directly on the actual candidate
        // (and not a copy)
        candidate *thisCandidate = &candidates[i];
        bool not_eliminated = !thisCandidate->eliminated;
        bool has_more_than_half_votes = thisCandidate->votes > half_the_votes;

        if (not_eliminated && has_more_than_half_votes)
        {
            cout << thisCandidate->name << endl;

            if (!winner_found)
                winner_found = true;
        }
    }
    
    return winner_found;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    int min_vote = numeric_limits<int>::max();

    for (int i = 0; i < candidate_count; i++)
    {
        // make a pointer to work directly on the actual candidate
        // (and not a copy)
        candidate *thisCandidate = &candidates[i];
        bool not_eliminated = !thisCandidate->eliminated;
        bool votes_less_than_min = thisCandidate->votes < min_vote;

        if (not_eliminated && votes_less_than_min)
            min_vote = thisCandidate->votes;
    }
    return min_vote;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        // make a pointer to work directly on the actual candidate
        // (and not a copy)
        candidate *thisCandidate = &candidates[i];
        bool not_eliminated = !thisCandidate->eliminated;

        // Any other vote than the minimum means no tie
        if (not_eliminated && (thisCandidate->votes != min))
            return false;
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        // make a pointer to work directly on the actual candidate
        // (and not a copy)
        candidate *thisCandidate = &candidates[i];

        bool not_eliminated = !thisCandidate->eliminated;

        if (not_eliminated && thisCandidate->votes == min)
        {
            (*thisCandidate).eliminated = true;
        }
    }
    return;
}