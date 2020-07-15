# static
# Write a Python program to check whether a 
# specified value is contained in a group of values.

# 3 -> [1, 5, 8, 3] : True		-1 -> [1, 5, 8, 3] : False

def check_in_group():
    while True:
        test_case = [1, 5, 8, 3]
        print('\nEnter \'-1\' to QUIT.')
        value = input('Enter - ')
        try:
            value = int(value)
        except:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            exit(-1)
        if value == -1:
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            break
        print(True if value in test_case else False)


# in case needed.
def check_random():
    while True:
        test_case = [1, 5, 8, 3]
        print('\nEnter \'-1\' to QUIT.')
        value = input('Enter - ')
        try:
            value = int(value)
        except:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            exit(-1)
        if value == -1:
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            break
        print(True if value in test_case else False)
