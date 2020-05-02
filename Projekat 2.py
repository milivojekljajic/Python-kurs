import re
import random
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [ 'https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive' ]

credentials = ServiceAccountCredentials.from_json_keyfile_name('Projekat-73ef94dc4536.json', scope)

gc = gspread.authorize(credentials)

sh = gc.open("Log in")

wks = sh.worksheet("login")

df = pd.DataFrame(wks.get_all_records())

# email values from google sheet
email = wks.col_values(1)
# password values from google sheet
pw = wks.col_values(2)

# global inputs
in1 = ""
in2 = ""
in3 = ""

# making dictionary for email and password values
all_dict = dict(zip(email, pw))
del all_dict["Email"]
print(all_dict)


# menu function
def user():
    global in1
    in1 = input("Da li ste prijavljeni? y/n: ").lower()

    # crossroad for sigh_up function or log_in function
    while in1 != "n" and in1 != "y":
        print("Vas unos je pogresan!")
        in1 = input("Da li ste prijavljeni? y/n: ").lower()
        continue

    if in1 == "n":
        sigh_up()

    elif in1 == "y":
        log_in()


# sigh_up function for new user
def sigh_up():
    global in2
    in2 = input("Unesite vas email: ").lower()

    # find errors in email characters from input
    while not re.match(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", in2):
        print("Niste unijeli email")
        in2 = input("Unesite vas mail: ").lower()
        continue

    # checks if email from user input already in sheet
    while in2 in all_dict:
        print("Email je vec zauzet! Unesite novi email")
        in2 = input("Unesite vas mail: ").lower()
        continue

    # sampler and update for new email and password
    if in2 not in all_dict:
        # string for password sampler
        str = "kadkjaskjdkadjkajkkk126712717236237617"
        # length of password
        passlen = 8
        # random sample function
        p = "".join(random.sample(str, passlen))
        # row list and index of row
        row = [ in2, p ]
        index = 2
        # insert row on google sheet
        sh2 = wks.insert_row(row, index)
        # update email and password on dictionary
        d2 = {in2: p}
        a = all_dict.update(d2)
        # print dictionary
        print(a)
        # print row on sheet
        print(sh2)
        # shows password to new user
        print("Vas password je: ", p)


# log_in function for old user
def log_in():
    # making global inputs
    global in2
    global in3
    in2 = input("Unesite vas mail: ").lower()
    in3 = input("Unesite vas password: ").lower()

    # testing is email and password in dictionary/sheet
    while in2 not in all_dict and in3 not in all_dict:
        print("Niste unijeli validan email ili password!")
        in2 = input("Unesite vas mail: ").lower()
        in3 = input("Unesite vas password: ").lower()
        continue

    # if all in dictionary making var for check and print message for user
    while in2 in all_dict:
        data = all_dict[ in2 ]

        if in3 == data:
            print("Ulogovani ste")
            break

        while in3 != data:
            print("Niste unijeli validan email ili adresu")
            in2 = input("Unesite vas mail: ").lower()
            in3 = input("Unesite vas password: ").lower()


user()
