# Menu-Driven program

import string
import random

# linking different python files into one.
from Part_1 import all_prime
from Part_2 import even_odd
from Part_3 import prime_composite
from Part_4 import vowel_consonant
from Part_5 import guess_game

while True:

    # Main-Menu Options.
    print('\nChoose your Option - ')
    print('0. Exit')
    print('1. Print Prime Numbers.')
    print('2. To Find whether Number is ODD or EVEN.')
    print('3. To Find whether Number is PRIME or COMPOSITE.')
    print('4. To Find whether Alphabet is VOWEL or NOT.')
    print('5. Guessing the Number Game')
    try:
        option = int(input('Enter - '))
    except:
        print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
        continue
    
    if (option < 0 or option > 5):
        print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
        continue
    
    if option == 0:
        # exit condtion
        print('\n\tARE YOU SURE TO TERMINATE THE PROGRAM - ')
        print('\t1. YES, CONFIRM.')
        print('\t2. NO, GO BACK.')
        try:
            terminate = int(input('Enter - '))
        except:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        if terminate > 2 or terminate < 1:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        if terminate == 2:
            continue
        print('\n\tTHANK YOU FOR JOINING US!')
        exit(0)
    elif option == 1:
        all_prime()
    elif option == 2:
        even_odd()
    elif option == 3:
        prime_composite()
    elif option == 4:
        vowel_consonant()
    elif option == 5:
        guess_game()
