"""
Reads "Birthdays.csv" and stores names and dates of birth in dictionary
'dataset'
"""
import csv

dataset = {}


def dictcreater():
    """
    Reads "Birthdays.csv" and stores names and dates of birth in dictionary
    'dataset'
    """
    with open("Birthdays.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            dataset[row[0]] = row[1]


names = dataset.keys()
dates = dataset.values()


if __name__ == "__main__":
    dictcreater()
    names = dataset.keys()
    dates = dataset.values()
    print(dataset)
    print(names)
    print(dates)
