pedometer = int(0)
while True:
    try:
        c0 = int(input("Enter a non-negative and non-zero integer number\n"))
        if c0 > 0:
            break
        else:
            print("The number must be non-negative and non-zero. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid Integer.")
        
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
        pedometer += 1
    else:
        c0 = 3*c0+1
        print(c0)
        pedometer += 1
print("steps=" + str(pedometer))