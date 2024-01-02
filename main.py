import pandas as pd
import datetime as dt
import random
import smtplib

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
        
        my_email="YOUR EMAIL HERE"
        #Refer the link on how to generate an app password https://www.youtube.com/watch?v=hXiPshHn9Pw
        password="YOUR APP PASSWORD HERE"
        
        #Gmail: smtp.gmail.com , Hotmail: smtp.live.com, Outlook: outlook.office365.com, Yahoo: smtp.mail.yahoo.com
        smtp_address="SMTP ADDRESS AS ABOVE"


        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=person["email"],msg=f"Subject:Happy Birthday\n\n{letter}")