import os

import csv

# cvs path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Specify the file to write to
output_path = os.path.join("..", "analysis", "financial_analysis.txt")

# Initialize variables
total_votes = 0
# Create dictionary for Candidate
candidates = {}
winner = ''

# Open and read the CSV file
with open(csvpath) as budgetcsv:
    cvsreader = csv.reader(budgetcsv)
    cvs_header = next(cvsreader)  # Skip the header row

    # Go over each row in the CSV
    for row in cvsreader:
        candidate = row[2]

        total_votes += 1

        # If the candidate is not in the candidates dictionary, add them
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            # If they are, increment their vote count
            candidates[candidate] += 1

# Create the results as a string
results = f'Election Results\nTotal Votes: {total_votes}\n'

# Iterate over each candidate
for candidate, votes in candidates.items():
    # Calculate the percentage of votes the candidate won
    vote_percentage = (votes / total_votes) * 100

    # Add to the results string
    results += f'{candidate}: {vote_percentage:.3f}% ({votes})\n'

    # If this candidate has more votes than the current winner, update the winner
    if winner == '' or votes > candidates[winner]:
        winner = candidate

# Add the winner to the results string
results += f'Winner: {winner}\n'

# Print the results to the terminal
print(results)

# Write the results to a text file
with open(output_path, 'w') as financial_analysis:
    financial_analysis.write(results)
