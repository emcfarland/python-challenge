import os
import csv

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')


with open(csvpath) as csvFileStream:
    csvreader = csv.reader(csvFileStream,delimiter=',')

    csv_header = next(csvreader)

    num_months = 0
    total = 0
    prev_profit = 0
    change = 0
    tot = 0
    gains = 0
    losses = 0

    for row in csvreader:
        
        num_months += 1
        curr_profit = int(row[1])
        total += curr_profit
        
        if prev_profit != 0:
            change += (curr_profit - prev_profit)
        
        if (prev_profit < curr_profit) and ((curr_profit - prev_profit) > gains):
            gains = curr_profit - prev_profit

        elif (prev_profit > curr_profit) and ((curr_profit - prev_profit) < losses):
            losses = curr_profit - prev_profit
        
        prev_profit = curr_profit
    
    # for val in change:
    #     tot += val


    print(f'Financial Analysis')
    print(f'--------------------------------')
    print(f'Total Months: {num_months}')
    print('Total: '+'${:,}'.format(total))
    print('${:,.2f}'.format(change/(num_months-1)))
    print('${:,}'.format(gains))
    print('${:,}'.format(losses))
    # print('${:,}'.format(max(change)))
    # print('${:,}'.format(min(change)))