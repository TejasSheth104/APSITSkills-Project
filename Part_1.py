# Write a program to print all prime nos between 1 to 1000

# prime number = a number that is divisible by 1 and the number itself.

def all_prime():
    while True:
        print('\n\t1. Print Prime Numbers.')
        print('\nEnter \'-1\' to GO BACK.')
        try:
            start = int(input('Enter the Start Number - '))
            if start == -1:
                print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
                break
            end = int(input('Enter the End Number - '))
            if end == -1:
                print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
                break    
        except:
            # if user enters anything other than an integer, the below message pops up
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        
        if start >= end:
            # start value should be always less than the end value 
            print('\tSTART NUMBER SHOULD BE ALWAYS LESS THAN END NUMBER.\n\tTRY AGAIN.\n')
            continue
        for num in range(start, end + 1):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    print(num, end=' ')
        print()

# uncomment to run the code.
# all_prime()
