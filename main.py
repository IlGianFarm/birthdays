#! /usr/bin/env python3

from birthdays import return_birthday

return_birthday('Albert Einstein')
return_birthday('Alan Turing')

import argparse
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", 
                         help = "whose birthday would you like to know",
                         choices=)
    parser.add_argument("date"