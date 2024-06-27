def liters_100km_to_miles_gallon(liters):
    mpg = 235.214583 / liters
    return mpg

def miles_gallon_to_liters_100km(mpg):
    liters_per_100km = 235.214583 / mpg
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))