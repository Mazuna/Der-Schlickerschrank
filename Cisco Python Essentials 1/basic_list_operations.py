my_list = [1, 2, 5, 4, 1, 4, 2, 6, 2, 9]
better_list = []

for digit in my_list:
    if digit not in better_list:
        better_list.append(digit)
        better_list.sort()

del my_list
del digit

print("The list with unique elements only:")
print(better_list)