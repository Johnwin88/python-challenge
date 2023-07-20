import os

import csv

# cvs path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Specify the file to write to
output_path = os.path.join("..", "analysis", "financial_analysis.txt")

# Initialize variables
total_months = 0
total_profit_loss = 0
changes = []
prev_profit_loss = 0
greatest_increase = {'date': '', 'amount': 0}
greatest_decrease = {'date': '', 'amount': 0}

# Open and read the CSV file
with open(csvpath) as cvsfile:
    cvsreader = csv.reader(cvsfile)
    cvs_header = next(cvsreader)  # Skip the header row

    # Go over each row in the CSV
    for row in cvsreader:
        date = row[0]
        profit_loss = int(row[1])

        # Increment the total months and add the profit/loss to the total
        total_months += 1
        total_profit_loss += profit_loss

        # If this is not the first row, calculate the change from the previous month
        if total_months > 1:
            change = profit_loss - prev_profit_loss
            changes.append(change)

            # Update the greatest increase or decrease if necessary
            if change > greatest_increase['amount']:
                greatest_increase = {'date': date, 'amount': change}
            elif change < greatest_decrease['amount']:
                greatest_decrease = {'date': date, 'amount': change}

        # Update the previous month's profit/loss for the next iteration
        prev_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Define results for export text file 
results = (
    f'Financial Analysis\n'
    f'Total Months: {total_months}\n'
    f'Total: ${total_profit_loss}\n'
    f'Average Change: {average_change:.2f}\n'
    f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})\n'
    f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})'
    )

# Print the results to the terminal
print(results)

# Write the results to a text file
with open(output_path, 'w') as textfile:
    textfile.write(results)
