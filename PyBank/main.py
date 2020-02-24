# import dependencies
import os
import csv

# define a function that allows the program to print to both stdout and a text file
def print_output(output, outfile):

    print(output)
    print(output, file=outfile)

## main code block

# set path for budget data
budget_csv = os.path.join("..", "PyBank", "budget_data.csv")

# initialize variables used in loops and conditionals
total_months = 0
net_revenue = 0
monthly_change = []
greatest_increase = 0
greatest_decrease = 0

# open budget data csv file 
with open(budget_csv) as budget_file:

    csvreader = csv.reader(budget_file, delimiter=',')

    header = next(csvreader, None) # store header and skip it so it is not counted as data

    # iterate through each row in the csv file, counting the row as a month and adding together the net revenue 
    for row in csvreader:
        total_months += 1
        net_revenue += int(row[1])

        if total_months > 1: # skip the first month since change needs at least two months of data to be calculated
            change = int(row[1]) - last_month
            monthly_change.append(change)

            # as the csv is being iterated, find and store values of greatest change
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        last_month = int(row[1]) # just before the loop restarts, temp store revenue data so it can be used to calculate change 

    average_change = sum(monthly_change)/len(monthly_change) # once the loop is complete, find the average change using the list of monthly change

# set output file and print output using custom print_output function
with open('output.txt', 'w') as outfile:

    print_output("Financial Analysis", outfile)
    print_output("----------------------------", outfile)
    print_output(f"Total Months: {total_months}", outfile)
    print_output(f"Total: {net_revenue}", outfile)
    print_output(f"Average  Change: {average_change:.2f}", outfile)
    print_output(f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase})", outfile)
    print_output(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})", outfile)


