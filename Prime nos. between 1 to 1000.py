#(1)Prime nos between 1 to 1000

Number = 1

while(Number <= 1000):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1





