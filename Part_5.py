# Write a Python program to check whether a 
# specified value is contained in a group of values.

# 3 -> [1, 5, 8, 3] : True		-1 -> [1, 5, 8, 3] : False

import random

def check_in_group():
    while True:
        test_case = [1, 5, 8, 3]
        print('\nEnter \'-1\' to QUIT.')
        value = input('Enter - ')
        try:
            value = int(value)
        except:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        if value == -1:
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            break
        if value in test_case:
            print('True')
            break
        else:
            print('False')
            continue

# check_in_group()

# in case needed.
def check_random():
    while True:
        test_case = list()
        length = input('\nEnter Length of the test_case - ')
        try:
            length = int(length)
        except:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        for _ in range(length):
            test_case.append(random.choice(range(10)))
        break
#     print(test_case)
    while True:
        print('\nEnter \'-1\' to QUIT.')
        value = input('Enter - ')
        try:
            value = int(value)
        except:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        if value == -1:
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            break
        if value in test_case:
            print('True')
            break
        else:
            print('False')
            continue

# check_random()
