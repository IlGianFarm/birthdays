import argparse
import sys
import copy
from Python_Package import csv_reader

def argnames():
    parser = argparse.ArgumentParser()
    parser.add_argument("name1", type=str,
                        help = "whose birthday would you like to know")
    parser.add_argument("name2", type=str,
                        help = "whose birthday would you like to know")
    args = parser.parse_args()
    return args

argnames()
args=argnames()

def attempt1():
    count=0
    for key,val in csv_reader.dataset.items():
        if key != "{}".format(args.name1):
            continue
        elif key == "{}".format(args.name1):
            count+=1
            print(key + "\'s birthday is", val + ".")
    if count==0:
        print("Sadly, we don\'t have", "{}".format(args.name1) + "\'s birthday.")

def attempt2():
    count=0
    for key,val in csv_reader.dataset.items():
        if key != "{}".format(args.name2):
            continue
        elif key == "{}".format(args.name2):
            count+=1
            print(key + "\'s birthday is", val + ".")
    if count==0:
        print("Sadly, we don\'t have", "{}".format(args.name2) + "\'s birthday.") 


if __name__=="__main__":
    argname()
    args=argname()
    print("Hello {}".format(args.name1))