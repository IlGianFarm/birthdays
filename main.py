#! /usr/bin/env python3

import argparse
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", required = True,
                         help = "whose birthday would you like to know",
                         choices=)
    parser.add_argument("date", 
                        help = "provide a date to check if it is anyone's 
                        birthday")
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_arguments()
    print('user has requested "{}" birthday'.format(args.name, args.date))