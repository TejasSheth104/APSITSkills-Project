#(3)PRIME OR COMPOSITE
number = int(input("Enter any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print('hello')
            print(number, "is a composite number")
            break
    else:
        print(number, "is a prime number")


else:
    print('less tan 1')
    print(number, "is a composite number")
    


