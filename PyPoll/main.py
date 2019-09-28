# import csv, os

import csv
import os

# read in data

file_path = os.path.join('..','Resources','election_data.csv')

with open(file_path, newline='') as csv_file:

    csv_data = csv.reader(csv_file, delimiter=',')
    next(csv_data)
    data = list(csv_data)

csv_file.close()

total_votes = len(data)

# get unique set of candidates
candidates = []
candidate_tally = []

for vote in data:
    if vote[2] not in candidates:
        candidates.append(vote[2])

# get number of candidates
no_candidates = len(candidates)

count = 0

# print & write concurrently
file_output = open('PyPoll Output.txt', 'w')

print('\n')
print('Election Results')
file_output.write('Election Results\n')
print('--------------------------------------')
file_output.write('--------------------------------------\n')
print(f'Total Votes: {total_votes:,}')
file_output.write(f'Total Votes: {total_votes:,}\n')
print('--------------------------------------')
file_output.write('--------------------------------------\n')

# get number of votes per candidate
while count < no_candidates:
    tally = 0  
    for vote in data:
        if vote[2] == candidates[count]:
            tally += 1

    candidate_tally.append(tally)
    print(f'{candidates[count]}: {(candidate_tally[count]/total_votes)*100:.2f}% ({candidate_tally[count]:,})')
    file_output.write(f'{candidates[count]}: {(candidate_tally[count]/total_votes)*100:.2f}% ({candidate_tally[count]:,})\n')    
    count += 1 

# get max votes
count = 0

max_votes = max(candidate_tally)
max_index = candidate_tally.index(max_votes)

print('--------------------------------------')
file_output.write('--------------------------------------\n')
print(f'Winner: {candidates[max_index]}')
file_output.write(f'Winner: {candidates[max_index]}\n')
print('--------------------------------------')
file_output.write('--------------------------------------\n')

file_output.close()
print('File: PyPoll Output.txt created')