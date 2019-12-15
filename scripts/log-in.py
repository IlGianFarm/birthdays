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



def login_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('user',
                       help = "Please insert your username (requires pwd).")
    parser.add_argument('pwd',
                       help = "Please insert yout password.")
    login_args = parser.parse_args()
    return login_args

login_args()
login_args=login_args()



username = '{}'.format(login_args.user)
password = '{}'.format(login_args.pwd)



def check_user(username, password):
    global conn
    global cursor
    
    try:
        salt = cursor.execute("SELECT salt FROM user WHERE username=?",
        [username]).fetchall()[0][0]
        conn.commit()
    except:
        print("Username or password are invalid, please retry.")
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
            print("User is present, password is valid, you may now " \
                "execute main.py.")
            conn.close()
            return results
        else:
            print("Username or password are invalid, please retry.")
            conn.close()
            return


check_user(username, password)