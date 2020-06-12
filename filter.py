import csv

with open('numbers/cummalative_morning_evening.csv') as cfile:
	reader = csv.reader(cfile, delimiter=',')
	cumma = [row[0] for row in reader]	


print(len(cumma))
