import os
import csv

poll_csv = os.path.join("..", "PyPoll", "election_data.csv")

total_votes = 0
candidates = {}

with open(poll_csv) as poll_file:

    csvreader = csv.reader(poll_file, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    print(f"{candidate}: {(votes/total_votes)*100}% ({votes})")

print("-------------------------")
print(f"Winner: {max(candidates, key=candidates.get)}")
print("-------------------------")
