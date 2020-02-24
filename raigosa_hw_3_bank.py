import os
import csv

# function to build summary string
def build_summary_string( num_months, sum, average_change, max_increase_date, max_increase, max_decrease_date, max_decrease ):
    summary_string = f"Financial Analysis\n----------------------------\nTotal Months: {num_months}\n"
    summary_string += f"Total: {sum}\nAverage Change: ${round(average_change,2)}\n"
    summary_string += f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
    summary_string += f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n"
    return summary_string

bank_csv = os.path.join("Pybank","Resources", "budget_data.csv")

# Read in the CSV file
with open(bank_csv, 'r') as bankfile:

    # Split the data on commas
    csvreader = csv.reader(bankfile, delimiter=',')

    # variables
    sum = 0
    num_months = 0
    max_increase = 0
    max_decrease = 0
    max_increase_date = ""
    max_decrease_date = ""
    last_change = None
    diff_sum = 0

    # skip header
    next(csvreader)

    # Loop through the data, populate variables
    for row in csvreader:
        change = int(row[1])
        sum += change
        num_months += 1
        if change > max_increase:
            max_increase = change
            max_increase_date = row[0]
        elif change < max_decrease:
            max_decrease = change
            max_decrease_date = row[0]
        if last_change is not None: 
            diff_sum += ( change - last_change ) 
        last_change = change
    
    # calculate avg change
    average_change = diff_sum / (num_months-1)

    # build summary string, print to terminal
    summary_string = build_summary_string(num_months, sum, average_change, max_increase_date, max_increase, max_decrease_date, max_decrease)
    print(summary_string)

    # output summary string to text file
    output_file = open("financial_summary.txt", "w")
    output_file.write(summary_string)
    output_file.close()
  

