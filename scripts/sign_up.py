import sqlite3
import hashlib
import argparse
import random

conn = None
cursor = None


def open_and_create():
    # Opens a database.
    # If the database already exists, it selects all data from table user.
    # If it does not already exist, it creates table user with 3 columns.
    global conn
    global cursor

    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM user")
    except Exception:
        cursor.execute('''CREATE TABLE user
        (username CHAR(256) NOT NULL,
        password CHAR(256) NOT NULL,
        salt CHAR(256) NOT NULL,
        PRIMARY KEY(username))''')


def signup_args():
    # Saves username and password to be used in the 'save_new_user' function.
    parser = argparse.ArgumentParser()
    parser.add_argument('user',
                        help="Please insert your username (requires pwd).")
    parser.add_argument('pwd',
                        help="Please insert your password (requires user).")
    signup_args = parser.parse_args()
    return signup_args


def save_new_user(username, password):
    # Saves username, random salt and hashed password of a new user.
    # If the username and password are already saved it asks for new ones.
    global conn
    global cursor

    rows = cursor.execute("SELECT * FROM user WHERE username=?", [username])
    conn.commit()

    if rows.fetchall():
        conn.close()
        print("User already exists, please provide different credentials.")
        return
    else:
        salt = str(random.random())
        digest = salt + password
        for i in range(1000000):
            digest = hashlib.sha256(digest.encode("utf-8")).hexdigest()

        try:
            cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                           (username, digest, salt))
            conn.commit()
        except Exception:
            print("An error occured trying to add the new user.")
            conn.close()
            return
        conn.close()
        print('''A new user has been added to the database. Try logging-in
with your credentials via main.py.''')
        return


if __name__ == "__main__":
    open_and_create()
    signup_args()
    signup_args = signup_args()
    username = '{}'.format(signup_args.user)
    password = '{}'.format(signup_args.pwd)
    save_new_user(username, password)
