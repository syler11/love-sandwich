import datetime as dt
from datetime import datetime

date_entry = input('Enter a date in YYYY-MM-DD format: ')
early_sunrise = "04:59:00"
late_sunrise = "07:33:00"
early_sunset = "16:08:00"
late_sunset = "20:49:00"


def get_date(date_entry):
    print("Please enter the date you would like to calculate sunrise and sunset for")
    print("Example: 2020, 10, 20\n")

    day, month, year = map(int, date_entry.split('-'))
    converted_date = dt.date(year, month, day)
 
    day_of_year = int(converted_date.strftime('%j'))
 
    if day_of_year >= 172 and day_of_year <355:
        x =  day_of_year -172
        return x
    elif day_of_year < 172:
        x = 355 - (365 + day_of_year)
        return x
    elif day_of_year >= 355:
        x = 355 - day_of_year
        return x

def daily_sunrise_diff():
    FMT = '%H:%M:%S'
    tdelta_rise = datetime.strptime(late_sunrise, FMT) - datetime.strptime(early_sunrise, FMT)
    avg_tdelta_rise = tdelta_rise / 172
    return avg_tdelta_rise
    
def daily_sunset_diff():
    FMT = '%H:%M:%S'
    tdelta_set = datetime.strptime(late_sunset, FMT) - datetime.strptime(str(early_sunset), FMT)
    avg_tdelta_set = tdelta_set / 172
    return avg_tdelta_set

def calculate_suntime(avg_sunset):
    FMT = '%H:%M:%S'
    new_sunrise = str((avg_sunset * day) + datetime.strptime(early_sunrise, FMT))
    slc = slice(11, 19)
    print(new_sunrise[slc])
    

day = get_date(date_entry)
avg_sunset = daily_sunrise_diff()
daily_sunset_diff()
calculate_suntime(avg_sunset)