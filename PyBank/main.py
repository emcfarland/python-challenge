import os
import csv

# Get File Path of budget_data.csv dataset
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')
txtpath = os.path.join('..','PyBank','Analysis','fin_analysis.txt')

# Open CSV
with open(csvpath) as csvFileStream:
    csvreader = csv.reader(csvFileStream,delimiter=',')

    csv_header = next(csvreader)

    # Set variables for number of months and total of profit/loss
    num_months = 0
    total = 0

    # Set variables for profit/loss of previous row,
    # change in profit from previous rows to current row,
    # and gains and losses, which hold max and min change values
    prev_profit = change = 0
    gains = losses = 0

    # Loop through rows of CSV
    for row in csvreader:
        
        # Increment number of months, set current profit, and add current to total
        num_months += 1
        curr_profit = int(row[1])
        total += curr_profit
        
        # Find change in profit, after the first row
        if prev_profit != 0:
            change += (curr_profit - prev_profit)
        
        # Store current increase and month if value is higher than previous
        if (curr_profit - prev_profit) > gains:
            gains = curr_profit - prev_profit
            best_month = row[0]

        # Store current decrease and month if value is lower than previous
        elif (curr_profit - prev_profit) < losses:
            losses = curr_profit - prev_profit
            worst_month = row[0]
        
        # Set previous profit for next iteration
        prev_profit = curr_profit
    
    # Calculate average change
    avg = change/(num_months-1)
    
    print(f'Financial Analysis')
    print(f'--------------------------------')
    print(f'Total Months: {num_months}')
    print(f'Total: ${total:,}')
    print(f'Average Change: ${avg:,.2f}')
    print(f'Greatest Increase in Profits: {best_month} (${gains:,})')
    print(f'Greatest Decrease in Profits: {worst_month} (${losses:,})')


# Open TXT and write results
with open(txtpath, "w") as text_file:

    text_file.writelines([
        f'Financial Analysis'+'\n',
        f'--------------------------------'+'\n',
        f'Total Months: {num_months}'+'\n',
        f'Total: ${total:,}'+'\n',
        f'Average Change: ${avg:,.2f}'+'\n',
        f'Greatest Increase in Profits: {best_month} (${gains:,})'+'\n',
        f'Greatest Decrease in Profits: {worst_month} (${losses:,})'
    ])