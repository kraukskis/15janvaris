import csv
with open('teksts.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])