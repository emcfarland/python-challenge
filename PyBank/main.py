import os
import csv

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')


with open(csvpath) as csvFileStream:
    csvreader = csv.reader(csvFileStream,delimiter=',')

    csv_header = next(csvreader)

    num_months = 0
    total = 0
    prev_profit = 0
    change = []
    tot = 0

    for row in csvreader:
        num_months += 1
        curr_profit = int(row[1])
        total += curr_profit
        if prev_profit != 0:
            change.append(curr_profit - prev_profit)
        prev_profit = curr_profit
    for val in change:
        tot += val

    print(f'Financial Analysis')
    print(f'--------------------------------')
    print(f'Total Months: {num_months}')
    print('Total: '+'${:,}'.format(total))
    print('${:,.2f}'.format(tot/(num_months-1)))
    print('${:,}'.format(max(change)))
    print('${:,}'.format(min(change)))