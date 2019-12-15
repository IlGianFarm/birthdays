#! /usr/bin/env python3

import sys
from scripts import log_in
from Python_Package import argsmain
from Python_Package import csv_reader
from Python_Package import birthdays

argsmain.argsmain()  # Runs argsmain's argsmain() function.
argsmain = argsmain.argsmain()

log_in.open_and_create()  # Opens the database containing users' credentials.

# Stores user inputted username and password as variables.
username = '{}'.format(argsmain.credentials[0][0])
password = '{}'.format(argsmain.credentials[0][1])

if log_in.check_user(username, password):  # Runs the "check_user()" function.
    # If user is verified:
    csv_reader.dictcreater()  # Read "Birthdays.csv" and create dictionary.

    # Save names as variables of 2 people user is interested in birthday.
    name1 = "{}".format(argsmain.names[0][0])
    name2 = "{}".format(argsmain.names[0][1])

    # Return birthday of both people if known.
    birthdays.attempt1(name1)
    birthdays.attempt2(name2)
