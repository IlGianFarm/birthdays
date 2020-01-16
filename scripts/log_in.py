"""
Checks whether users' credentials are present in the user database"""

import sqlite3
import hashlib
import argparse
import random

conn = None
cursor = None


def open_and_create():
    """
    Opens a database.
    If the database already exists it selects all data from table user.
    If it does not already exist it creates table user with 3 columns.
    """ 
    global conn
    global cursor

    conn = sqlite3.connect("scripts/user_database.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM user")
    except Exception:
        cursor.execute('''CREATE TABLE user
        (username CHAR(256) NOT NULL,
        password CHAR(256) NOT NULL,
        salt CHAR(256) NOT NULL,
        PRIMARY KEY(username))''')


def login_args():
    """Saves username and password to be used in the 'check_user' function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('user',
                        help="Please insert your username (requires pwd).")
    parser.add_argument('pwd',
                        help="Please insert your password (requires user).")
    loginargs = parser.parse_args()
    return loginargs


def check_user(username, password):
    """
    Checks whether the users' credentials are registered in the database.

    :param username: the username inputted by the user to be checked for
     presence in the user database.
    :param password: the password inputted by the user to be checked for
     presence in the user database.
    """
    global conn
    global cursor

    try:
        salt = cursor.execute("SELECT salt FROM user WHERE username=?",
                              [username]).fetchall()[0][0]
        conn.commit()
    except Exception:
        print("Username and/or password are invalid, please retry.")
        conn.close()
        return

    if salt:
        digest = salt + password
        for i in range(1000000):
            digest = hashlib.sha256(digest.encode("utf-8")).hexdigest()

        query = cursor.execute('''SELECT * FROM user WHERE username=? AND
                                   password=?''', (username, digest))
        results = query.fetchall()
        if results:
            print('''User is present, password is valid, you may now
 proceed with main.py.''')
            conn.close()
            return results
        else:
            print("Username and/or password are invalid, please retry.")
            conn.close()
            return


if __name__ == "__main__":
    open_and_create()
    login_args()
    login_args = login_args()
    username = '{}'.format(login_args.user)
    password = '{}'.format(login_args.pwd)
    check_user(username, password)
