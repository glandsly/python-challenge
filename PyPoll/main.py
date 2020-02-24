# import dependencies
import os
import csv

# define a function that allows the program to print to both stdout and a text file
def print_output(output, outfile):

    print(output)
    print(output, file=outfile)

## main code block

# set path for polling data
poll_csv = os.path.join("..", "PyPoll", "election_data.csv")

# initialize variables used in loops and conditionals
total_votes = 0
candidates = {}

# open polling data csv file
with open(poll_csv) as poll_file:

    csvreader = csv.reader(poll_file, delimiter=',')

    header = next(csvreader, None) # store header and skip it so it is not counted as data

    # iterate through each row in the csv file, incrementing the total number of votes by one
    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates: # adds a new candidate and sets their votes at 1 (important to count the initializing row as a vote too)
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1 # if a candidate has already been added, just increments their vote count by 1

# set output file and print output using custom print_output function
with open('output.txt', 'w') as outfile:

    print_output("Election Results", outfile)
    print_output("-------------------------", outfile)
    print_output(f"Total Votes: {total_votes}", outfile)
    print_output("-------------------------", outfile)

    # iterates through dictionary, using key (candidate), value (votes), and total votes to provide snapshot of each candidate's performance 
    for candidate, votes in candidates.items():
        print_output(f"{candidate}: {(votes/total_votes)*100:.3f}% ({votes})", outfile)

    print_output("-------------------------", outfile)
    print_output(f"Winner: {max(candidates, key=candidates.get)}", outfile) # finds the max value by comparing dictionary values and returning the key
    print_output("-------------------------", outfile)
