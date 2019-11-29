import csv

def csv_reader():
    names=[]
    dates=[]
    with open("Birthdays.csv") as csv_file:
        csv_reader = csv.reader(csv_file , delimiter=";")
        for row in csv_reader:
	        names.append(row[0])
            dates.append(row[1])

if __name__==__"main"__:
    csv_reader()