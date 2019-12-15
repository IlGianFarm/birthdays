#! /usr/bin/env python3

import sys
from scripts import log_in
from Python_Package import argsmain
from Python_Package import csv_reader
from Python_Package import birthdays

argsmain.argsmain()
argsmain = argsmain.argsmain()

log_in.open_and_create()

<<<<<<< HEAD
username = '{}'.format(argsmain.credentials[0][0])
password = '{}'.format(argsmain.credentials[0][1])

if log_in.check_user(username, password):
    csv_reader.dictcreater()

    name1 = "{}".format(argsmain.names[0][0])
    name2 = "{}".format(argsmain.names[0][1])
=======
username = '{}'.format(argsmain.credentials[0][0])
password = '{}'.format(argsmain.credentials[0][1])

if log_in.check_user(username, password):
    csv_reader.dictcreater()

    name1 = "{}".format(argsmain.names[0][0])
    name2 = "{}".format(argsmain.names[0][1])
>>>>>>> database

    birthdays.attempt1(name1)
    birthdays.attempt2(name2)
