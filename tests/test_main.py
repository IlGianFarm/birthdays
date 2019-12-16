import unittest
import os
import sys
import tempfile
import sqlite3
import hashlib

sys.path.append('../')
sys.path.append('../scripts')

conn = sqlite3.connect("../scripts/user_database.db")
cursor = conn.cursor()

users = []


def database_reader():
    global conn
    global cursor

    # Select the data from the database to be placed in the 'users' list.
    query = cursor.execute("SELECT * FROM user")

    for i in query.fetchall():
        users.append(i)


def check_user(username, password):
    # Checks whether the users' credentials are registered in the temp file.
    counts = 0
    for i in range(len(users)):
        if users[i][0] != username:
            continue
        elif users[i][0] == username:
            counts += 1
            salt = users[i][2]
            digest = salt + password
            for i in range(1000000):
                digest = hashlib.sha256(digest.encode("utf-8")).hexdigest()
    if counts == 0:
        return "Username and/or password are invalid, please retry"

    count = 0
    for i in range(len(users)):
        if users[i][0] != username:
            continue
        elif users[i][0] == username:
            count += 1
            if users[i][1] != digest:
                continue
            elif users[i][1] == digest:
                count += 1
                if users[i][2] != salt:
                    continue
                elif users[i][2] == salt:
                    count += 1
                    return '''User is present, password is valid,
 you may now proceed with main.py.'''
    if count <= 1:
        return "Username and/or password are invalid, please retry"


class TestMain(unittest.TestCase):

    def setUp(self):
        # Create the temporary file.
        self.temp_db = tempfile.NamedTemporaryFile(mode="w+t", delete="True")

        # Fill the temporary file with data from the database.
        self.temp_db.writelines(str(users))

    def test_no_db(self):
        db = self.temp_db

        self.assertFalse(db)
        self.assertTrue(db)

    def test_no_csv(self):
        u, r = parse_allowed_repos(datafile="/tmp/nonexistentcsv")
        self.assertFalse(u)
        self.assertFalse(r)

    def test_empty_db(self):
        count = 0
        self.temp_db.seek(0)
        data = self.temp_db.read()
        print(data)

        # Count elements within the file.
        for i in data.split():
            count += 1

        self.assertEqual(count, 0)

    def test_empty_csv(self):
        u, r = parse_allowed_repos(datafile=self.temporary_file)
        self.assertFalse(u)
        self.assertFalse(r)

    def test_log_in(self):
        # Correct username and password
        username = "expeldior"
        password = "levissima"
        result1 = check_user(username, password)
        self.assertEqual('''User is present, password is valid,
 you may now proceed with main.py.''', result1)

        # Correct username and password
        username = "IlGian"
        password = "Gianluchino"
        result2 = check_user(username, password)
        self.assertEqual('''User is present, password is valid,
 you may now proceed with main.py.''', result2)

        # Correct username and password
        username = "alemusca"
        password = "alessandrino"
        result3 = check_user(username, password)
        self.assertEqual('''User is present, password is valid,
 you may now proceed with main.py.''', result3)

        # Wrong username, correct password
        username = "expeldio"
        password = "levissima"
        result4 = check_user(username, password)
        self.assertEqual("Username and/or password are invalid, please retry",
                         result4)

        # Correct username, wrong password
        username = "expeldior"
        password = "levissim"
        result5 = check_user(username, password)
        self.assertEqual("Username and/or password are invalid, please retry",
                         result5)

        # Incorrect username and password
        username = "expeldio"
        password = "levissim"
        result6 = check_user(username, password)
        self.assertEqual("Username and/or password are invalid, please retry",
                         result6)

    def tearDown(self):
        self.temp_db.close()

if __name__ == "__main__":
    print('\n', "Printing list produced to check for a correct structure...")
    database_reader()
    print("users ->", users)
    unittest.main()
