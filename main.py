import pandas as pd
import datetime as dt

data=pd.read_csv("birthdays.csv")

#Data in dictionary format
dict=data.to_dict(orient="records")

now=dt.datetime.now()
today_date=now.day
today_month=now.month


for person in dict:
    if person["day"]==today_date and person["month"]==today_month:
        print(f"Happy Birthday {person["name"]}")
