# Write a Python program to find whether a given number (accept from the user) 
# is Prime or composite, print out an appropriate message to the user.

def prime_composite():
    while True:
        print('\nEnter \'-1\' to QUIT.')
        number = input('Enter a Number - ')
        try:
            number = int(number)
        except:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        if number == -1:
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            break
        elif number < 2:
            print('Number', number, 'is NEITHER Prime NOR Composite Number\n')
            continue
        for i in range(2, number):
            if number % i == 0:
                print('Number', number, 'is Composite Number\n')        
                break
        else:
            print('Number', number, 'is a Prime Number\n')

# uncomment to run the code.
# prime_composite()