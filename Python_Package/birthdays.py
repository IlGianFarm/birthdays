from Python_Package import csv_reader
from Python_Package import argsmain

argsmain = argsmain.argsmain()


def attempt1(name1):
    count = 0
    for key, val in csv_reader.dataset.items():
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
    for key, val in csv_reader.dataset.items():
        if key != name2:
            continue
        elif key == name2:
            count += 1
            print(key + "\'s birthday is", val + ".")
    if count == 0:
        print("Sadly, we don\'t have", name2 +
              "\'s birthday.")


if __name__ == "__main__":
    argsmain()
    argsmain = argsmain.argsmain()
    name1 = "{}".format(argsmain.names[0][0])
    name2 = "{}".format(argsmain.names[0][1])
    attempt1(name1)
    attempt2(name2)
