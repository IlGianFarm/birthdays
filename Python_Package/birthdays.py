from package import csv_reader_test
from package import argname_test

arguments = argname_test.arguments()


def attempt1(name1):
    count = 0
    for key, val in csv_reader_test.dataset.items():
        if key != name1:
            continue
        elif key == name1:
            count += 1
            print(key + "\'s birthday is", val + ".")
    if count == 0:
        print("Sadly, we don\'t have", name1 +
              "\'s birthday.")


def attempt2(name2):
    count = 0
    for key, val in csv_reader_test.dataset.items():
        if key != name2:
            continue
        elif key == name2:
            count += 1
            print(key + "\'s birthday is", val + ".")
    if count == 0:
        print("Sadly, we don\'t have", name2 +
              "\'s birthday.")


if __name__ == "__main__":
    arguments
    name1 = "{}".format(arguments.names[0][0])
    name2 = "{}".format(arguments.names[0][1])
    attempt1()
    attempt2()
