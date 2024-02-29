#Monday Motivation Project
import smtplib, ssl
import datetime as dt
import random

# MY_EMAIL = "jaugustorc@gmail.com"
# MY_PASSWORD = "admuxuzbuxcljjgu"
# To_EMAIL="jaugustorc@gmail.com"
# SMTP="smtp.gmail.com"
# port = 587  # For SSL

# connection= smtplib.SMTP(SMTP.encode("UTF-8"), port=port)
# connection.starttls()
# connection.login(user=MY_EMAIL, password=MY_PASSWORD)
# connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs=To_EMAIL,
#         msg="Subject:Hellso"
#     )
# connection.close()

import smtplib
     
server = "smtp.gmail.com"
     
connection = smtplib.SMTP(server, 587)
connection.set_debuglevel(1)
connection.starttls()
connection.close()

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 2:
#     with open("Python---100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for-2022\\Day 32 Send e-mail\\Birthday Wisher (Day 32) start\\quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)

#     print(quote)
#     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as connection:
#         #connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg=f"Subject:Monday Motivation\n\n{quote}"
#         )




## Working with date and time in Python
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)
