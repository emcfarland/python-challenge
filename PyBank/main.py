import os
import csv

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')


with open(csvpath) as csvFileStream:
    csvreader = csv.reader(csvFileStream,delimiter=',')

    csv_header = next(csvreader)

    num_months = 0
    total = 0
    curr_profit = 0

    for row in csvreader:
        num_months += 1
        total += int(row[1])
        curr_profit = int(row[1])
        if curr_profit > 0:

    print(num_months)
    print(total)
    print(total/num_months)