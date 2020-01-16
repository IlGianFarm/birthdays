#! /usr/bin/env python3
"""
Uses arguments "-credentials" and "-names" from argsmain.py to check whether
the user is registered to the user database and to return the birthdays of 2
individuals that the user would like to know the birthdays of.
"""
import sys
from scripts import log_in
from pypackage import argsmain
from pypackage import csv_reader
from pypackage import birthdays

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
    birthdays.attempts(name1, name2)
