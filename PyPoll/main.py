import os
import csv

csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
# txtpath = os.path.join('..','PyPoll','Analysis','election_results.txt')


with open(csvpath) as csvFileStream:
    csvreader = csv.reader(csvFileStream,delimiter=',')

    csv_header = next(csvreader)

    num_votes = 0
    candidates = {}
    # p1 = p2 = p3 = p4 = 0

    for row in csvreader:

        num_votes += 1

        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] += 1
    #         candidates.append(row[2])
    
    #     if row[2] == candidates[0]:
    #         p1 += 1
    #     elif row[2] == candidates[1]:
    #         p2 += 1
    #     elif row[2] == candidates[2]:
    #         p3 += 1
    #     elif row[2] == candidates[3]:
    #         p4 += 1


    sorted_cand = sorted(candidates.items(), key=lambda x:x[1], reverse=True)        
    for x in sorted_cand:
        print(f'{x[0]}: '+'{:.3%}'.format(x[1]/num_votes))
    print(f'Total Votes: {num_votes}')
    # print(candidates[0] + ': {:.3%}'.format(p1/num_votes) + ' (' + str(p1) + ')')
    # print(candidates[1] + ': {:.3%}'.format(p2/num_votes) + ' (' + str(p2) + ')')
    # print(candidates[2] + ': {:.3%}'.format(p3/num_votes) + ' (' + str(p3) + ')')
    # print(candidates[3] + ': {:.3%}'.format(p4/num_votes) + ' (' + str(p4) + ')')

    # print(f'Winner: {winner}')
    