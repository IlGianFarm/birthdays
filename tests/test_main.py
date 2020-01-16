import unittest
import os
import sys
import tempfile
import sqlite3
import hashlib
import csv

sys.path.append('../')
sys.path.append('../pypackage')
sys.path.append('../scripts')

from pypackage import csv_reader

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


datalist = []
names = []
dates = []


def csv_reader_for_tests():
    # Reads "Birthdays.csv" and stores data in dictionary 'dataset'.
    with open("../pypackage/Birthdays.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        # Fill datalist with contents of 'Birthdays.csv'.
        for row in csv_reader:
            datalist.append(row[0])
            datalist.append(row[1])

        # Fill 'names' list with names from 'datalist' list.
        i = 0
        while i < len(datalist):
            names.append(datalist[i])
            i += 2

        # Fill 'dates' list with names from 'datalist' list.
        j = 1
        while j < len(datalist):
            dates.append(datalist[j])
            j += 2


test_dict = {}


def dictcreater_for_tests():
    # Reads "Birthdays.csv" and stores data in dictionary 'dataset'.
    with open("../pypackage/Birthdays.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            test_dict[row[0]] = row[1]


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


def attempts(name1, name2):
    # Checks whether name1's birthday is saved in the dictionary 'test_dict'.
    # If it is, it returns name1's birthday.
    # Otherwise it prints that it doesn't know it.
    count = 0
    for key, val in test_dict.items():
        if key != name1:
            continue
        elif key == name1:
            count += 1
            return key + "\'s birthday is " + val + "."
    if count == 0:
        return "Sadly, we don\'t have " + name1 + "\'s birthday."

    # Checks whether name2's birthday is saved in the dictionary 'test_dict'.
    # If it is it returns name2's birthday.
    # Otherwise it prints that it doesn't know it.
    counting = 0
    for key, val in test_dict.items():
        if key != name2:
            continue
        elif key == name2:
            counting += 1
            return key + "\'s birthday is " + val + "."
    if counting == 0:
        return "Sadly, we don\'t have " + name2 + "\'s birthday."


class TestMain(unittest.TestCase):

    def setUp(self):
        # Create the temporary file.
        self.temp_db = tempfile.NamedTemporaryFile(mode="w+t", delete="True")

        # Fill the temporary file with data from the database.
        self.temp_db.writelines(str(users))

        # Create the temporary csv.
        self.temp_csv = tempfile.NamedTemporaryFile(mode="w+t", delete="True")

        # Fill the csv with names and dates from the 'names' and 'dates' lists
        for i in names, dates:
            self.temp_csv.writelines(str(i))

    def test_db(self):
        db = self.temp_db

        self.assertTrue(db)

    def test_csv(self):
        csv = self.temp_csv

        self.assertTrue(csv)

    def test_full_db(self):
        count = 0
        self.temp_db.seek(0)
        data = self.temp_db.read()

        # Count elements within the file.
        for i in data.split():
            count += 1

        self.assertTrue(count > 0)

    def test_full_csv(self):
        count = 0
        self.temp_csv.seek(0)
        data = self.temp_csv.read()

        # Count elements within the file.
        for a in data.split():
            count += 1

        self.assertTrue(count > 0)

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

    def test_birthdays(self):
        global test_dict

        # Both individuals' birthdays are in the csv.
        name1 = "Albert Einstein"
        name2 = "Donald Trump"
        result1_1 = attempts(name1, name2)
        result1_2 = attempts(name2, name1)
        self.assertEqual("Albert Einstein's birthday is 03/14/1879.",
                         result1_1)
        self.assertEqual("Donald Trump's birthday is 06/14/1946.",
                         result1_2)

        # Only name1's birthday is in the csv.
        name3 = "Benjamin Franklin"
        name4 = "Valentino Rossi"
        result2_1 = attempts(name3, name4)
        result2_2 = attempts(name4, name3)
        self.assertEqual("Benjamin Franklin's birthday is 01/17/1706.",
                         result2_1)
        self.assertEqual("Sadly, we don't have Valentino Rossi's birthday.",
                         result2_2)

        # Only name2's birthday is in the csv.
        name5 = "Lewis Hamilton"
        name6 = "Ada Lovelace"
        result3_1 = attempts(name5, name6)
        result3_2 = attempts(name6, name5)
        self.assertEqual("Sadly, we don't have Lewis Hamilton's birthday.",
                         result3_1)
        self.assertEqual("Ada Lovelace's birthday is 12/10/1815.",
                         result3_2)

        # Neither individuals' birthdays are in the csv.
        name7 = "Sebastian Vettel"
        name8 = "Charles Leclerc"
        result4_1 = attempts(name7, name8)
        result4_2 = attempts(name8, name7)
        self.assertEqual("Sadly, we don't have Sebastian Vettel's birthday.",
                         result4_1)
        self.assertEqual("Sadly, we don't have Charles Leclerc's birthday.",
                         result4_2)

    def tearDown(self):
        self.temp_db.close()
        self.temp_csv.close()


if __name__ == "__main__":
    print('\n', "Printing lists produced to check for a correct structure...")
    database_reader()
    print("users ->", users)
    csv_reader_for_tests()
    print('\n', "datalist ->", datalist)
    print("names ->", names)
    print("dates ->", dates, '\n')
    print('\n', "Printing dictionary produced to check correct structure...")
    dictcreater_for_tests()
    print("test_dict ->", test_dict, '\n')
    unittest.main()
