#The Function
def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorian calendar period")
        return None
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


#Testdata
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

input_year = int(input("Enter a year: "))
print(is_year_leap(input_year))