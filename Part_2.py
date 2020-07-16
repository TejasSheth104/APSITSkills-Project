# Write a Python program to find whether a given number (accept from the user) 
# is even or odd, print out an appropriate message to the user.

# even numbers = all those numbers that are completely divisble by 2, including 0. 

def even_odd():
    while True:
        print('\nEnter \'-1\' to QUIT.')
        number = input('Enter a Number - ')
        try:
            number = int(number)
        except:
            # if user enters anything other than an integer, the below message pops up
            print('\tINTERGER EXCEPTED\n\tTRY AGAIN.\n')
            continue
        if number == -1:
            # exit condition
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            break
        elif number < -1:
            # all negative numbers are not classified as odd or even
            print('Neither ODD nor EVEN\n')
        elif number % 2 == 0:
            print('Number', number, '- is EVEN\n')
        elif number % 2 == 1:
            print('Number', number, '- is ODD\n')

# uncomment to run the code.
# even_odd()
