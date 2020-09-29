import os
import csv

# Get File Path of election_data.csv dataset
csvpath = os.path.join('Resources','election_data.csv')
txtpath = os.path.join('Analysis','elec_analysis.txt')

# Open CSV
with open(csvpath) as csvFileStream:
    csvreader = csv.reader(csvFileStream,delimiter=',')

    csv_header = next(csvreader)
    
    # Set Total Votes number to zero for incrementing and set blank dictionary for individual candidate totals
    num_votes = 0
    candidates = {}

    # Iterate through rows of CSV
    for row in csvreader:

        # Increment total votes
        num_votes += 1

        # Add unique candidate names as dictionary keys and set vote counts to 0
        if row[2] not in candidates:
            candidates[row[2]] = 0
        
        # Increment vote count for this row's candidate
        candidates[row[2]] += 1

    # Sort candidates by decreasing vote count
    sorted_cand = sorted(candidates.items(), key=lambda x:x[1], reverse=True)        
    
    # Print total votes and line break
    print('Election Results')
    print('--------------------------------')    
    print(f'Total Votes: {num_votes:,}')
    print('--------------------------------')
    
    # Print name, percent of total votes, and number of votes for each candidate
    for x in sorted_cand:
        print(f'{x[0]}: {x[1]/num_votes:.3%} ({x[1]:,} votes)')

    # Print line break, and winner by position in sorted list
    print('--------------------------------')
    print(f'Winner: {sorted_cand[0][0]}')

# Open TXT and write results
with open(txtpath, "w") as text_file:

    # Write results to text file
    text_file.writelines([
        'Election Results\n',
        '--------------------------------\n',
        f'Total Votes: {num_votes:,}\n',
        '--------------------------------\n',
    ])

    for x in sorted_cand:
        text_file.write(f'{x[0]}: {x[1]/num_votes:.3%} ({x[1]:,} votes)\n')

    text_file.writelines([
        '--------------------------------\n',
        f'Winner: {sorted_cand[0][0]}'
    ])
