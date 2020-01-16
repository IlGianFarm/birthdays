# Hello and welcome to ROROPD's Birthday Repository.

Members of the group are:
- IlGianFarm/Ubuntu = Gianluca Schiavon
- alemusca = Alessandro Muscarà
- LucaBrigo = Luca Brigo

In this repository, you can find a file named ```main.py``` whose main purpose is to return the birthdays of two people that the user specifies.
Currently the only birthdays known are those of:
- Albert Einstein
- Benjamin Franklin
- Ada Lovelace
- Donald Trump
- Rowan Atkinson

**Note:** In order to run, this project requires the following modules to be installed: *argparse, csv, hashlib, os, random, sqlite3, sys, tempfile* and *unittest*.

If you wish to understand the ins-and-outs of various modules, **documentation** can be found in the directory ```documentation```.


# Step 1: Run Tests
Tests can be found in the ```tests``` folder.
Please navigate to it using this command:
```
$ cd tests
```
and run ```test_main.py``` like this:
```
$ python3 test_main.py
```


# Step 2: Sign-Up
We ask that you **sign-up** to our user database.
Please navigate to the folder ```scripts``` like this:
```
$ cd ../scripts
```
and run ```sign_up.py```.
When running it make sure to insert your **USERNAME** and **PASSWORD** that you wish to sign-up with.

E.g.
```
$ python sign_up.py abc 123
```
> **Note:** in this example username = "abc" and password = "123".

If inputs are **new**, output should look like this:
```
$ python3 sign_up.py abc 123
A new user has been added to the database. Try logging-in
with your credentials via main.py. 
```

If the user is **already present** in the database, output should look like this:
```
$ python3 sign_up.py abc 123
User already exists, please provide different credentials.
```


# Step 3: Run Main
After having successfully signed-up you may now run ```main.py```.

To run ```main.py``` navigate back out of the ```scripts``` folder like so:
```
$ cd ..
```
and execute ```main.py``` like this:
```
$ python3 main.py -credentials abc 123 -names "Albert Einstein" "Ada Lovelace"
```
> **Note:** in this example we took the username and password from the previous example ("abc" "123") and used the names of two individuals present in the known birthdays list.

Initially, the code will wish to verify whether the user is registered to the database.
> Parameter ```-credentials``` asks for a *username* and a *password* (we suggest you insert the ones used during sign-up).

If the user is verified the code will return the birthdays of two individuals.
> Parameter ```-names``` asks for the *name* and *surname* of **two** individuals that the user wants to know the birthdays of (we suggest choosing names of people listed at the beginning of the README).

If user is present and names are recognized, output should look like this:
```
$ python3 main.py -credentials abc 123 -names "Albert Einstein" "Ada Lovelace"
User is present, password is valid, you may now
 proceed with main.py.
Albert Einstein's birthday is 03/14/1879.
Ada Lovelace's birthday is 12/10/1815.
```
> **Note:** using username "abc" and password "123" will not ensure that this ouptut will be shown as these username and password are not registered in the user database.
