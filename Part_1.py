# Write a program to print all prime nos between 1 to 1000

# prime number = a number that is divisible by 1 and the number itself.

def all_prime():
    print()
    for num in range(1, 1000):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=' ')
    print()

# uncomment to run the code.
# all_prime()
