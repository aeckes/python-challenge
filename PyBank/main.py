# import csv, os

import csv
import os

# read in data

file_path = os.path.join('..','Resources','budget_data.csv')

print(file_path)

with open(file_path, newline='') as csv_file:

    csv_data = csv.reader(csv_file, delimiter=',')
    next(csv_data)
    data = list(csv_data)

   # print(len(months)-1)

PL_agg = 0
PL_Max = 0

PL_Min = 0

# determine total value of profit / loss
for row in data:

    PL_agg = PL_agg + int(row[1])
    if int(row[1]) > int(PL_Max):
        PL_Max = int(row[1])
        PL_Max_Month = row[0]

    if int(row[1]) < int(PL_Min):
        PL_Min = int(row[1])
        PL_Min_Month = row[0]


#print(f"{row[0]} {row[1]}")

Avg_PL = PL_agg / len(data)

print('Financial Analysis \n')
print('---------------------------------\n')
print(f"Total Months: {len(data)}")
print(f"Total: ${PL_agg:,.2f}")
print(f"Average Change: ${Avg_PL:,.2f}")
print(f"Greatest Increase in Profits: {PL_Max_Month} (${PL_Max:,.2f})")
print(f"Greatest Decrease in Profits: {PL_Min_Month} (${PL_Min:,.2f})")

# Write to file

output_data = [['Financial Analysis',''],
               ['----------------------- ',''],
               ['Total Months:', len(data)],
               ['Total:', f'${PL_agg:,.2f}'],
               ['Average Change:', f'${Avg_PL:,.2f}'],
               [f'Greatest Increase in Profits ({PL_Max_Month}):', f'${PL_Max:,.2f}'],
               [f'Greatest Decrease in Profits ({PL_Min_Month}):', f'${PL_Min:,.2f}']]

output_file = open('output.csv', 'w')
with output_file:
    writer = csv.writer(output_file)
    writer.writerows(output_data)
            
