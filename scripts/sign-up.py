import sqlite3
import hashlib
import argparse
import random

conn = None
cursor = None



def open_and_create():
    global conn
    global cursor
    
    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM user")
    except:
        cursor.execute('''CREATE TABLE user
        (username CHAR(256) NOT NULL,
        password CHAR(256) NOT NULL,
        salt CHAR(256) NOT NULL,
        PRIMARY KEY(username))''')

open_and_create()



def signup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('user',
                       help = "Please insert your username (requires pwd).")
    parser.add_argument('pwd',
                       help = "Please insert yout password.")
    signup_args = parser.parse_args()
    return signup_args

signup_args()
signup_args = signup_args()



username = '{}'.format(signup_args.user)
password = '{}'.format(signup_args.pwd)



def save_new_user(username, password):
    global conn
    global cursor

    rows = cursor.execute("SELECT * FROM user WHERE username=?",[username])
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
        except:
            print("An error occured trying to add the new user.")
            conn.close()
            return
        conn.close()
        print("A new user has been added to the database. Try logging-in" \
              "with your credentials via log-in.py.")
        return

save_new_user(username, password)