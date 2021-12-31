import datetime

date_entry = input('Enter a date in YYYY-MM-DD format: ')
early_sunset = ""
early_sunrise = ""
late_sunrise = ""
late_sunset = ""
   
def get_date(date_entry):
    print("Please enter the date you would like to calculate sunrise and sunset for")
    print("Example: 2020, 10, 20\n")

    day, month, year = map(int, date_entry.split('-'))
    converted_date = datetime.date(year, month, day)
 
    day_of_year = int(converted_date.strftime('%j'))
 
    if day_of_year >= 172 and day_of_year <355:
        x =  day_of_year -172
        print(x)
    elif day_of_year < 172:
        x = 355 - (365 + day_of_year)
        print(x)
    elif day_of_year >= 355:
        x = 355 - day_of_year
        print(x)

def daily_time_difference
    


get_date(date_entry)