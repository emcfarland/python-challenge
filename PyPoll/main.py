import os
import csv

csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
# txtpath = os.path.join('..','PyPoll','Analysis','election_results.txt')


with open(csvpath) as csvFileStream:
    csvreader = csv.reader(csvFileStream,delimiter=',')

    csv_header = next(csvreader)

    num_votes = 0
    candidates = {}

    for row in csvreader:

        num_votes += 1

        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] += 1

    sorted_cand = sorted(candidates.items(), key=lambda x:x[1], reverse=True)        
    
    print(f'Total Votes: {num_votes:,}')
    print('--------------------------------')
    
    for x in sorted_cand:
        print(f'{x[0]}: {x[1]/num_votes:.3%} ({x[1]:,} votes)')

    print('--------------------------------')
    print(f'Winner: {sorted_cand[0][0]}')

    