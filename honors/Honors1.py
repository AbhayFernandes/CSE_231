import csv
import datetime

fp = open('TEW_2021_Observations.csv', 'r')
reader = csv.reader(fp, delimiter=',', quotechar='"')
count = 0
new_list = []
for row in reader:
    date = row[0] + " " + row[1]
    try:
        date = datetime.datetime.strptime(date, '%m/%d/%Y %H:%M')
    except ValueError:
        continue
    count += 1
    if date.month >= 3 and date.month <= 11:
        # replace first two columns with date
        row[:2] = [date]
        new_list.append(row)
        print(row)