import pandas as pd
import datetime as dt
import random

data=pd.read_csv("birthdays.csv")

#Data in dictionary format
dict=data.to_dict(orient="records")

now=dt.datetime.now()
today_date=now.day
today_month=now.month


for person in dict:
    if person["day"]==today_date and person["month"]==today_month:
        random_letter_no=random.randint(1,3)
        
        with open(f"letter_templates/letter_{random_letter_no}.txt") as file:
            data=file.read()
        letter=data.replace("[NAME]",f"{person["name"]}")
        print(letter)