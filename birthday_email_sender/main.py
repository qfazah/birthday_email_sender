import smtplib
import datetime as dt


now_month = dt.datetime.now().month
now_date = dt.datetime.now().date()
with open("birthdays.csv") as birthday_file :
    for i in birthday_file :
        print(i)
`