import datetime

   
def get_date():
    print("Please enter the date you would like to calculate sunrise and sunset for")
    print("Example: 2020, 10, 20\n")

    date1 = datetime.datetime(2021, 10, 21)
 
    day_of_year = int(date1.strftime('%j'))

    print(day_of_year)
 
    if day_of_year >= 172 and day_of_year <355:
        x =  day_of_year -172
        print(x)
    elif day_of_year < 172:
        x = 355 - (365 + day_of_year)
        print(x)
    elif day_of_year >= 355:
        x = 355 - day_of_year
        # print(x)
        print(type(x))

get_date()