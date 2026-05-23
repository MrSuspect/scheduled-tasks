# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import random
import smtplib
import datetime as dt
import os
import pandas

letter_files = [
    "letter_1.txt",
    "letter_2.txt",
    "letter_3.txt"
]

# Secret values from environment variables
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

# Current date
now = dt.datetime.now()
month = now.month
day = now.day

# Read CSV
birthdays = pandas.read_csv("birthdays.csv")

# Check birthdays
for index, row in birthdays.iterrows():

    if row["month"] == month and row["day"] == day:

        # Pick random template
        chosen_file = random.choice(letter_files)

        # Read template
        with open(f"letter_templates/{chosen_file}") as letter_file:
            letter_text = letter_file.read()

        # Replace placeholder
        final_letter = letter_text.replace("[NAME]", row["name"])

        # Send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday!\n\n{final_letter}"
            )
