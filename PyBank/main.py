import os
import csv

# Get File Path of budget_data.csv dataset
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

# Open CSV
with open(csvpath) as csvFileStream:
    csvreader = csv.reader(csvFileStream,delimiter=',')

    csv_header = next(csvreader)

    # Set variables for number of months and total of profit/loss
    num_months = 0
    total = 0

    # Set variables for profit/loss of previous row,
    # change in profit from previous row to current row,
    # and gains and losses, which hold max and min change values
    prev_profit = change = 0
    gains = losses = 0

    for row in csvreader:
        
        num_months += 1
        curr_profit = int(row[1])
        total += curr_profit
        
        if prev_profit != 0:
            change += (curr_profit - prev_profit)
        
        if (prev_profit < curr_profit) and ((curr_profit - prev_profit) > gains):
            gains = curr_profit - prev_profit
            best_month = row[0]

        elif (prev_profit > curr_profit) and ((curr_profit - prev_profit) < losses):
            losses = curr_profit - prev_profit
            worst_month = row[0]
        
        prev_profit = curr_profit
    
    avg = change/(num_months-1)
    
    print(f'Financial Analysis')
    print(f'--------------------------------')
    print(f'Total Months: {num_months}')
    print(f'Total: ${total:,}')
    print(f'Average Change: ${avg:,.2f}')
    print(f'Greatest Increase in Profits: {best_month} (${gains:,})')
    print(f'Greatest Decrease in Profits: {worst_month} (${losses:,})')


    # with open("Output.txt", "w") as text_file:
    #     text_file.write()