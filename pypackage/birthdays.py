from pypackage import csv_reader
from pypackage import argsmain

argsmain = argsmain.argsmain()


def attempts(name1, name2):
    # Checks whether namel's birthday is saved in the dictionary 'dataset'.
    # If it is, it returns name1's birthday.
    # Otherwise it prints that it doesn't know it.
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

    # Checks whether name2's birthday is saved in the dictionary 'dataset'.
    # If it is, it returns name2's birthday.
    # Otherwise it prints that it doesn't know it.
    counting = 0
    for key, val in csv_reader.dataset.items():
        if key != name2:
            continue
        elif key == name2:
            count += 1
            print(key + "\'s birthday is", val + ".")
    if counting == 0:
        print("Sadly, we don\'t have", name2 +
              "\'s birthday.")


if __name__ == "__main__":
    argsmain()
    argsmain = argsmain.argsmain()
    name1 = "{}".format(argsmain.names[0][0])
    name2 = "{}".format(argsmain.names[0][1])
    attempts(name1, name2)
