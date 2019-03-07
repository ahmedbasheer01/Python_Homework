import csv

#file path
csvpath = ('budget_data.csv')

#Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first  
    csv_header = next(csvreader)

    max = 0
    min = 0
    
    row_count = 0
    total_amount = 0

    for row in csvreader:
        row_count = row_count + 1
        profit_loss = int(row[1])
        total_amount = total_amount + profit_loss

        if profit_loss >= max: 
            max = profit_loss
            maxdate = row[0]
    
        if profit_loss <= min:
            min = profit_loss
            mindate = row[0]
    

    avg_chg = int(total_amount / row_count)
    print(f'Total Number of Months: {row_count}')
    print(f'Total Amount: ${total_amount}')
    print(f'Avg change: $', avg_chg)
    print('Max Profits: ',maxdate, '$', max)
    print('Min Profits: ',mindate, '$', min)

file = open('datafile.txt','w') 
 
file.write(f'Total Number of Months: {row_count}')
file.write(f'Total Amount: ${total_amount}')
file.write(f'Avg change: ${avg_chg}')
file.write(f'Max Profits: {maxdate} $ {max}')
file.write(f'Min Profits: {mindate}  $ {min}')

file.close() 