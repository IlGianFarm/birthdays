import argparse
import sys


def argsmain():
    parser = argparse.ArgumentParser()
    parser.add_argument('-credentials', action='append', nargs=2,
                        metavar=('username', 'password'),
                        help='Please insert your username and your password.')
    parser.add_argument('-names', action='append', nargs=2,
                        metavar=('name1', 'name2'),
                        help=('''Whose birthday would you like to know? You
                         may choose 2 names from this list: Albert Einstein,
                         Benjamin Franklin, Ada Lovelace, Donald Trump,
                         Rowan Atkinson.'''))
    argsmain = parser.parse_args()
    return argsmain


if __name__ == "__main__":
    argsmain()
    argsmain = argsmain()
    print(argsmain)
