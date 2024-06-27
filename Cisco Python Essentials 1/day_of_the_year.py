def is_leap_year(year):
    if year < 1582:
        return None
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def is_valid_date(year, month, day):
    if year < 1582 or month < 1 or month > 12 or day < 1:
        return False
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > days_in_month[month - 1]:
        return False
    return True

def day_of_year(year, month, day):
    if not is_valid_date(year, month, day):
        return None
    
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = sum(days_in_month[:month - 1]) + day
    return day_of_year

# Testing the function
print(day_of_year(2023, 1, 1))  # Output: 1
print(day_of_year(2023, 12, 31))  # Output: 365
print(day_of_year(2024, 12, 31))  # Output: 366 (2024 is a leap year)
print(day_of_year(2024, 2, 29))  # Output: 60 (2024 is a leap year)