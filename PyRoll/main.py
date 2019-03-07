import csv

#file path
csvpath = ('election_data.csv')

#Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first  
    csv_header = next(csvreader)

    candidates=[]
    vote_count=[]
    percentages=[]
    
    tot_count = 0

    for row in csvreader:
        tot_count = tot_count + 1
        candidate = row[2]

        #if candidate has other votes then add to vote tally
        if candidate not in candidates:
            candidates.append(candidate)
            vote_count.append(1)            
        else:
            marker = candidates.index(candidate)
            vote_count[marker]= vote_count[marker]+1

    #calculations:
    #tot_candidates = len(candidates)

    for x in range(len(candidates)):
        percent=round(((vote_count[x] / tot_count)*100),2)
        percentages.append(percent)
    
    print('Election Results')
    print('-------------------------')
    print('')
    print(f'Total Votes: {tot_count}')
    
    for y in range(len(candidates)):
        print(f'{candidates[y]}: {percentages[y]}% ({vote_count[y]}) ')

    print('')
    winner = candidates[percentages.index(max(percentages))]
    print(f'Winner: {winner}')

#open write file
write_file = f'pypoll_summary.txt'
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write('Election Results\n')
filewriter.write('-----------------------\n')
filewriter.write(f'Total Votes: {tot_count}\n')
for z in range(len(candidates)):
    filewriter.write(f'{candidates[z]}: {percentages[z]}% ({vote_count[z]})\n')

filewriter.write(f"Winner: {winner}\n")

#close file
filewriter.close()