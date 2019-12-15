#! /usr/bin/env python3

import sys
from scripts import log_in
from Python_Package import argsmain
from Python_Package import csv_reader
from Python_Package import birthdays

argsmain.argsmain()
argsmain = argsmain.argsmain()

log_in.open_and_create()

username = '{}'.format(arguments.credentials[0][0])
password = '{}'.format(arguments.credentials[0][1])

if log_in.check_user(username, password):
    csv_reader_test.dictcreater()

    name1 = "{}".format(arguments.names[0][0])
    name2 = "{}".format(arguments.names[0][1])

    birthdays.attempt1(name1)
    birthdays.attempt2(name2)
