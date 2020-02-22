import os
import csv

budget_csv = os.path.join("..", "PyBank", "budget_data.csv")

total_months = 0
net_revenue = 0
last_month = 0
monthly_change = []
average_change = 0
greatest_increase_date = "None"
greatest_increase = 0
greatest_decrease_date = "None"
greatest_decrease = 0

with open(budget_csv) as budget_file:

    csvreader = csv.reader(budget_file, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        total_months += 1
        net_revenue += int(row[1])

        if total_months > 1:
            change = int(row[1]) - last_month
            monthly_change.append(change)

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        last_month = int(row[1])

        # if greatest_increase < int(row[1]):
        #    greatest_increase = int(row[1])
        #    greatest_increase_date = row[0]

        # if greatest_decrease > int(row[1]):
        #    greatest_decrease = int(row[1])
        #    greatest_decrease_date = row[0]

    # print(monthly_change)
    average_change = sum(monthly_change)/(total_months - 1)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {net_revenue}")
    print(f"Average  Change: {average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})")
