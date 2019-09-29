# import csv, os

import csv
import os

# read in data

file_path = os.path.join('..','Resources','budget_data.csv')

with open(file_path, newline='') as csv_file:

    csv_data = csv.reader(csv_file, delimiter=',')
    next(csv_data)
    data = list(csv_data)

csv_file.close()

PL_agg = 0
PL_Max = 0
PL_Min = 0
PL_PrevRowVal = 0
Annual_Change = []
Agg_Change = 0
# determine total value of profit / loss
for row in data:

    PL_agg = PL_agg + int(row[1])
    if int(row[1]) > int(PL_Max):
        PL_Max = int(row[1])
        PL_Max_Month = row[0]

    if int(row[1]) < int(PL_Min):
        PL_Min = int(row[1])
        PL_Min_Month = row[0]

    Annual_Change.append(int(row[1]) - PL_PrevRowVal)
    PL_PrevRowVal = int(row[1])

del Annual_Change[0]
Avg_PL = sum(Annual_Change) / len(Annual_Change)

print('Financial Analysis \n')
print('---------------------------------\n')
print(f"Total Months: {len(data)}")
print(f"Total: ${PL_agg:,.2f}")
print(f"Average Change: ${Avg_PL:,.2f}")
print(f"Greatest Increase in Profits: {PL_Max_Month} (${PL_Max:,.2f})")
print(f"Greatest Decrease in Profits: {PL_Min_Month} (${PL_Min:,.2f})")

file_output = open('PyBank_output.txt' , 'w')

file_output.write('Financial Analysis \n\n')
file_output.write('---------------------------------\n\n')
file_output.write(f"Total Months: {len(data)}\n")
file_output.write(f"Total: ${PL_agg:,.2f}\n")
file_output.write(f"Average Change: ${Avg_PL:,.2f}\n")
file_output.write(f"Greatest Increase in Profits: {PL_Max_Month} (${PL_Max:,.2f})\n")
file_output.write(f"Greatest Decrease in Profits: {PL_Min_Month} (${PL_Min:,.2f})\n")           

print(f"File: PyBank_output.txt created")