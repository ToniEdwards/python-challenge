import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    print("Header: "+str(csv_header))
    rows = []
    for row in csv_reader:
        rows.append(row)
    print(rows)
print("Financial Analysis")


