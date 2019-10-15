input("This Program Calculates The Number Of Days \n Since You Were Born \n'Press Enter to Continue'")
from datetime import date 
import time
  
def numOfDays(date1, date2): 
    return (date2-date1).days 

current_day = int(time.strftime("%d"))
current_month = int(time.strftime("%m"))
current_year = int(time.strftime("%y"))+2000

while True:
    user_raw_input = input("Please Enter Your Date Of Birth In \n>>>Format DD/MM/YYYY\n : ")
    split = user_raw_input.split("/")

    dobdate = int(split[0])
    dobmonth = int(split[1])
    dobyear = int(split[2])


    date1 = date(dobyear, dobmonth, dobdate) 
    date2 = date(current_year,current_month,current_day)
    print("Its Been ",numOfDays(date1, date2), "days Since You Were Born \n  ", "OR" ,(numOfDays(date1, date2))*24 , "Hours\n")  
