import datetime
from datetime import date
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pip._vendor.distlib.compat import raw_input

scope = [ 'https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive' ]

credentials = ServiceAccountCredentials.from_json_keyfile_name('Projekat-73ef94dc4536.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Hospital")

wks1 = wks.worksheet("Pacijenti")

wks2 = gc.open("Hospital").get_worksheet(1)

wks3 = gc.open("Hospital").get_worksheet(2)

df = pd.DataFrame(wks1.get_all_records())
df1 = pd.DataFrame(wks2.get_all_records())
df2 = pd.DataFrame(wks3.get_all_records())
df3 = df1.get("IME")
df4 = df2.get("DIJAGNOZE")
df5 = df.get("IME I PREZIME")


# function for program menu
def hospital():
    print("Ako zelite da unesete podatke pritisnite 1")
    print("Ako zelite da pregledate podatke pritisnite 2")
    menu = raw_input("Unesite opciju koju zelite: ")

    while not menu.isdigit():
        print("Molimo vas unesite broj")
        menu = raw_input("Unesite opciju koju zelite: ")
        continue

    while int(menu) != 1 and int(menu) != 2:
        print("Unos je netacan! Pokusajte ponovo")
        menu = raw_input("Unesite opciju koju zelite: ")
        continue
    if int(menu) == 1:
        write()
    if int(menu) == 2:
        search()


# function for writing on google sheet
def write():
    in1 = input("Koliko pacijenata zelite da unesete?: ")

    while not in1.isdigit():
        print("Molimo vas da unesete broj!")
        in1 = input("Koliko pacijenata zelite da unesete?: ")
        continue
    while int(in1) == 0:
        print("Unesite broj veci od nule!")
        write()

    try:
        for i in range(int(in1)):
            # function for days
            def input_d(a):
                # test is input numeric
                while a.isalpha():
                    print("Niste unijeli broj!")
                    a = input("Unesite dan: ")
                    continue
                # can be maximum 32 days
                while int(a) < 1 or int(a) > 32:
                    print("Unos je netacan!")
                    a = input("Unesite dan: ")
                    continue

            # function for months
            def input_m(a):
                # test is input numeric
                while a.isalpha():
                    print("Niste unijeli broj!")
                    a = input("Unesite mjesec: ")
                    continue
                # can be maximum 12 months
                while int(a) < 1 or int(a) > 12:
                    print("Unos je netacan!")
                    a = input("Unesite mjesec: ")
                    continue

            # function for years
            def input_y(a):
                # test is input numeric
                while a.isalpha():
                    print("Niste unijeli broj!")
                    a = input("Unesite godinu: ")
                    continue
                # years cant be under the 1930 and above 2020
                while int(a) < 1900 or int(a) > 2025:
                    print("Unos je netacan!")
                    a = input("Unesite godinu: ")
                    continue

            # function for hours of start exam
            def hours1(a):
                # test is input numeric
                while a.isalpha():
                    print("Molimo vas da unesete broj!")
                    a = raw_input("Unesite vrijeme pocetka pregleda, format(0900): ")
                    continue
                # length of numbers cant be less then 4 and above 4
                while len(a) > 4 or len(a) < 4:
                    print("Unos je netacan, unesite 4 broja")
                    a = raw_input("Unesite vrijeme pocetka pregleda, format(0900): ")
                    continue

            # function for hours of end exam
            # same process like in the function above
            def hours2(a):
                while a.isalpha():
                    print("Molimo vas da unesete broj!")
                    a = raw_input("Unesite vrijeme kraja pregleda, format(0900): ")
                    continue
                while len(a) > 4 or len(a) < 4:
                    print("Unos je netacan, unesite 4 broja")
                    a = raw_input("Unesite vrijeme kraja pregleda, format(0900): ")
                    continue

            # list of patients names
            name_list = [ ]

            # appending patients names in to the name_list
            for elem in df5:
                name_list.append(elem)

            # inputs for patients name and surname
            name = raw_input("Unesite ime pacjenta: ").capitalize()

            # test for names, if in input more then two words return input to user
            while not name.isalpha():
                print("Niste unijeli slova!")
                name = raw_input("Unesite ime pacjenta: ").capitalize()
                continue

            surname = raw_input("Unesite prezime pacijenta: ").capitalize()

            # test for names, if in input more then two words return input to user
            while not surname.isalpha():
                print("Niste unijeli slova!")
                surname = raw_input("Unesite prezime pacijenta: ").capitalize()
                continue

            name_f = name + " " + surname

            # if patient is in the list print information of patient
            if name_f in name_list:
                print("Pdodaci o pacjentu:")
                print(df[ df[ "IME I PREZIME" ] == name_f ])
            else:
                pass

            # inputs about year of patient birth day
            print("Unesite datum rodjenja pacijenta")

            day = input("Unesite dan: ")
            input_d(day)
            month = input("Unesite mjesec: ")
            input_m(month)
            year = input("Unesite godinu: ")
            input_y(year)

            # inputs about date of exam
            print("Unesite datum pregleda pacijenta")
            day_1 = input("Unesite dan: ")
            input_d(day_1)
            month_1 = input("Unesite mjesec: ")
            input_m(month_1)
            year_1 = input("Unesite godinu: ")
            input_y(year_1)

            # datetime function to format patient date of birth
            d = datetime.date(int(year), int(month), int(day))
            form = d.strftime("%d.%m.%Y")

            # datetime function to format date of exam
            d1 = datetime.date(int(year_1), int(month_1), int(day_1))
            form2 = d1.strftime("%d.%m.%Y")

            # date of birth cant be greater of date of exam
            while d > d1:
                print("Unos je netacan. Pokusajte ponovo.")
                day = input("Unesite dan: ")
                input_d(day)
                month = input("Unesite mjesec: ")
                input_m(month)
                year = input("Unesite godinu: ")
                input_y(year)

                print("Unesite datum pregleda pacijenta")
                day_1 = input("Unesite dan: ")
                input_d(day_1)
                month_1 = input("Unesite mjesec: ")
                input_m(month_1)
                year_1 = input("Unesite godinu: ")
                input_y(year_1)
                continue

            # date of exam cant be lower of datetime_today
            while d1 < datetime.date.today():
                print("Unos je netacan. Unesite ponovo datum pregleda.")
                print("Unesite datum pregleda pacijenta")
                day_1 = input("Unesite dan: ")
                input_d(day_1)
                month_1 = input("Unesite mjesec: ")
                input_m(month_1)
                year_1 = input("Unesite godinu: ")
                input_y(year_1)
                continue

            # datetime function to calculate patient years
            days_in_year = 365.2425
            patient_year = int((date.today() - d).days / days_in_year)
            patient_year2 = str(patient_year)

            # raw_input for hours of exam start
            h = raw_input("Unesite vrijeme pocetka pregleda u formatu pr.(1230): ")
            hours1(h)

            # raw_input for hours of exam end
            h1 = raw_input("Unesite vrijeme kraja pregleda u formatu pr.(1230):")
            hours2(h1)

            d2 = datetime.time(hour=int(h[ 0:2 ]), minute=int(h[ 2:4 ]))

            d4 = datetime.time(hour=int(h1[ 0:2 ]), minute=int(h1[ 2:4 ]))

            # hours of start exam cant be greater of end exam
            while d2 > d4:
                print("Netacan unos! Pokrenite program ponovo!")
                write()

            # calculate time of exam
            d6 = str(datetime.timedelta(hours=(d4.hour - d2.hour), minutes=(d4.minute - d2.minute)))

            # row list for append on google sheet with index of row
            row = [ name_f, form, form2, patient_year2, str(d2)[ :-3 ], str(d4)[ :-3 ], str(d6)[ :-3 ] ]
            index = 2

            # list of doctors names
            doc_names = [ ]

            # input for name of the doctor
            doctors = input("Ime i prezime doktora: ").title()

            # append doctors from google sheet in the doc_names list
            for i in df3:
                doc_names.append(i)

            # append the name of doctor in row_list
            if doctors in doc_names:
                row.append(doctors)

            # test for names, if in input more then two words return input to user
            while len(doctors.split()) != 2:
                print("Niste pravilno unijeli ime i prezime")
                doctors = input("Ime i prezime doktora: ").title()
                continue

            while doctors.isdigit():
                print("Niste unijeli slova!")
                doctors = input("Unesite ime i prezime doktora: ").title()
                continue

            # if doctor name not write in google sheet, warning for user
            while doctors not in doc_names:
                print("Unos je netacan")
                doctors = input("Unesite ime i prezime doktora: ").title()
                continue

            # list of diagnosis
            diagnosis = [ ]

            diagn = input("Unesite dijagnozu pacijenta: ").capitalize()

            # append diagnosis from google sheet on the list of diagnosis
            for i in df4:
                diagnosis.append(i)

            # if diagnosis in the list append to row list
            if diagn in diagnosis:
                row.append(diagn)

            while diagn.isdigit():
                print("Niste unijeli slova!")
                diagn = input("Unesite dijagnozu pacijenta: ").capitalize()
                continue

            # while user input not in the diagnosis list, ask user to do input again
            while diagn not in diagnosis:
                print("Unos je netacan")
                diagn = input("Unesite dijagnozu pacijenta: ").capitalize()
                continue

            # insert all inputs from row_list to google sheet
            inputs = wks.insert_row(row, index)
    except ValueError:
        print("Desila se greska u programu.")
        print("Molimo vas da pokusate ponovo. Pazite na unos datuma i sati!")
        write()


# function for searching documentation
def search():
    # inputs for type of searching
    print("Za pretragu pacijenata koje ste imali u zadnji broj 'N' dana pritisnite 1")
    print("Za pretragu pacijenta kojeg zelite da pregledate po imenu i prezimenu pritisnite 2")
    print("Da pregledate sve pacijente na odredjen datum pritisnite 3")
    print("Da pregledate pacijente po dijagnozi pritisnite 4")

    ask1 = input("Kako zelite da pretrazite?: ")

    if int(ask1) == 1:
        by_numbers_of_days()
    if int(ask1) == 2:
        by_names()
    if int(ask1) == 3:
        try:
            by_date()
        except ValueError:
            print("Doslo je do greske!")
            print("Unesite pravilno datum!")
            by_date()
    if int(ask1) == 4:
        by_diagnosis()


# function for searching by days
def by_numbers_of_days():
    search1 = raw_input("Unesite podatke za pretragu: ")

    while not search1.isdigit():
        print("Molimo vas unesite broj.")
        search1 = raw_input("Unesite podatke za pretragu: ")
        continue

    n_numbers = df.sort_values(by="DATUM PREGLEDA", ascending=0)

    n_numbers2 = n_numbers.head(int(search1))

    print(n_numbers2)


# function for searching by names of patients
def by_names():
    search2 = raw_input("Unesite ime i prezime pacijenta: ").title()

    while len(search2.split()) != 2:
        print("Niste pravilno unijeli ime i prezime")
        search2 = input("Unesite ime i prezime pacijenta: ").title()
        continue

    while search2.isdigit():
        print("Niste unijeli slova!")
        search2 = input("Unesite ime i prezime pacijenta: ").title()
        continue

    patient_name = df[ "IME I PREZIME" ]

    pn = [ ]

    for i in patient_name:
        pn.append(i)

    while search2 not in pn:
        print("Pacijent se ne nalazi u arhivi.")
        print("Molimo vas pokusajte ponovo.")
        search2 = raw_input("Unesite ime i prezime pacijenta: ").title()
    else:
        print(df[ df[ "IME I PREZIME" ] == search2 ])


# function for searching by date of exam
def by_date():
    # function for days
    def input_d(a):
        # test is input numeric
        while a.isalpha():
            print("Niste unijeli broj!")
            a = input("Unesite dan: ")
            continue
        # can be maximum 32 days
        while int(a) < 1 or int(a) > 32:
            print("Unos nije u redu!")
            a = input("Unesite dan: ")
            continue

    # function for months
    def input_m(a):
        # test is input numeric
        while a.isalpha():
            print("Niste unijeli broj!")
            a = input("Unesite mjesec: ")
            continue
        # can be maximum 12 months
        while int(a) < 1 or int(a) > 12:
            print("Unos nije u redu!")
            a = input("Unesite mjesec: ")
            continue

    # function for years
    def input_y(a):
        # test is input numeric
        while a.isalpha():
            print("Niste unijeli broj!")
            a = input("Unesite godinu: ")
            continue
        # years cant be under the 1930 and above 2020
        while int(a) < 1900 or int(a) > 2020:
            print("Unos nije u redu!")
            a = input("Unesite godinu: ")
            continue

    print("Unesite datum pregleda pacijenta")
    day = input("Unesite dan: ")
    input_d(day)
    month = input("Unesite mjesec: ")
    input_m(month)
    year = input("Unesite godinu: ")
    input_y(year)

    exam_date = datetime.date(int(year), int(month), int(day))
    form = exam_date.strftime("%d.%m.%Y")

    print(df[ df[ "DATUM PREGLEDA" ] == str(form) ])


# function for searching by diagnosis
def by_diagnosis():
    search4 = raw_input("Unesite dijagnozu: ").capitalize()

    patients_diagnosis = df2[ "DIJAGNOZE" ]

    patients_diagnosis_list = [ ]

    for i in patients_diagnosis:
        patients_diagnosis_list.append(i)

    while search4.isdigit():
        print("Niste unijeli slova!")
        search4 = raw_input("Unesite dijagnozu: ").capitalize()
        continue

    while search4 not in patients_diagnosis_list:
        print("Unos je netacan")
        search4 = raw_input("Unesite dijagnozu: ").capitalize()
        continue

    if search4 in patients_diagnosis_list:
        print(df[ df[ "DIJAGNOZA" ] == search4 ])


hospital()
