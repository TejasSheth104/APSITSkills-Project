#Prime nos. between 1 to 1000

for Number in range (1, 1000):
    count = 0

    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')