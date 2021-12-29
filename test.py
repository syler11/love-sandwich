from datetime import date
 

def get_date():
    """
    User input date to calculate and return reuquired sunrise and sunset data
    """
    print("Please enter the date you would like to calculate sunrise and sunset for")
    print("Example: 2020, 10, 20\n")

    date_str = input("Enter your date here: ")

    converted_date = date_str

    print(converted_date)


def calculate_day(user_data):
 
    day_of_year = user_data.strftime('%j')
 
    if day_of_year >= 172 and day_of_year <355:
        x =  day_of_year -172
        print(x)
    elif day_of_year < 172:
        x = 355 - (365 + day_of_year)
        print(x)
    elif day_of_year >= 355:
        x = 355 - day_of_year
        print(x)

user_data = get_date()
# calculate_day(user_data)

print(converted_date)