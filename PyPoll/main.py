import os
import csv

def print_output(output):

    with open('output.txt', 'a') as outfile:
        print(output)
        print(output, file=outfile)

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

print_output("Election Results")
print_output("-------------------------")
print_output(f"Total Votes: {total_votes}")
print_output("-------------------------")

for candidate, votes in candidates.items():
    print_output(f"{candidate}: {(votes/total_votes)*100}% ({votes})")

print_output("-------------------------")
print_output(f"Winner: {max(candidates, key=candidates.get)}")
print_output("-------------------------")
