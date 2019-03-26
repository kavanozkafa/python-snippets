import csv


with open('myfile.csv') as csvfile:
	readCSV = csv.reader(csvfile,delimiter=',')
	
	for row in readCSV:
		print(row)