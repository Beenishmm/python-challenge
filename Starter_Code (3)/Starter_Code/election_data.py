import csv
import os

csvpath = os.path.join("PyPoll\Resources", "election_data.csv")
total_votes = 0
print (csvpath)

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    header = next(csvreader)
    # Initialize variables
    total_votes = 0
    candidates = {}
    # Loop through each row in the CSV file
    for row in csvreader:
        # Add to the total vote count
        total_votes += 1
        # If the candidate is not in the dictionary, add them
        if row[2] not in candidates:
            candidates[row[2]] = 1
        # Otherwise, increment their vote count
        else:
            candidates[row[2]] += 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Loop through the candidates dictionary and calculate their vote percentage
for candidate, vote_count in candidates.items():
    vote_percentage = round(vote_count / total_votes * 100, 3)
    print(f"{candidate}: {vote_percentage}% ({vote_count})")
print("-------------------------")
# Find the winner of the election based on popular vote
winner = max(candidates, key=candidates.get)
print(f"Winner: {winner}")
