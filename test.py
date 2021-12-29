from datetime import date
 
date_val = date(2007, 1, 1)
 
day_of_year = int(date_val.strftime('%j'))
 
if day_of_year >= 172 and day_of_year <355:
    x =  day_of_year -172
    print(x)
elif day_of_year < 172:
    x = 355 - (365 + day_of_year)
    print(x)
elif day_of_year >= 355:
    x = 355 - day_of_year
    print(x)