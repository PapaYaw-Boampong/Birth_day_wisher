import random
import smtplib
import datetime as dt
import pandas



# 1. Update the birthdays.csv
def new_birthday_entry(name, email, year, month, day):
    empty = False
    try:
        with open("birthdays.csv") as x:
            if x.read() == "":
                empty = True
        with open("birthdays.csv", mode="a") as b_data:
            if empty:
                b_data.write(f"name,email,year,month,day")
    except FileNotFoundError:
        with open("birthdays.csv", mode="a") as b_data:
            b_data.write(f"name,email,year,month,day")
    finally:
        b_data.write(f"\n{name},{email},{year},{month},{day}")


# Checking if today matches a birthday in the birthdays.cs
present = dt.datetime.now()
birthdays = []
with open("birthdays.csv") as data:
    for lines in data:
        line = (lines.strip()).split(",")
        if line[3] == str(present.month) and line[4] == str(present.day):
            birthdays.append(line)
            print("reached")


# Selects a random letter template

def letter():
    letters = ["./letter_templates/letter_1.txt ", "./letter_templates/letter_2.txt",
               "./letter_templates/letter_3.txt"]
    return random.choice(letters)


# Populate template with User info
if len(birthdays) > 0:
    for birthday in birthdays:
        with open(letter()) as a:
            text = "Subject: Happy BirthDay !!! \n\n" + a.read().replace("[NAME]", birthday[0])

            birthday.append(text)


# Send the letter generated to person's email address.
MY_EMAIL = "Sample email"
MY_PASSWORD = "Sample password"


# Uncomment the code below when sample user email and passcode have been entered
# for birthday in birthdays:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs=birthday[1], msg=birthday[-1])
