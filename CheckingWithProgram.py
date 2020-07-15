# Menu-Driven program

import string

# just for reference purposes.
from Part_1 import all_prime
from Part_2 import even_odd
from Part_3 import prime_composite
from Part_4 import vowel_consonant
from Part_5 import check_in_group

while True:
    print('\nChoose your Option - ')
    print('0. Exit')
    print('1. Print Prime Numbers between 1 to 1000.')
    print('2. To Find whether Number is ODD or EVEN.')
    print('3. To Find whether Number is PRIME or COMPOSITE.')
    print('4. To Find whether Alphabet is VOWEL or NOT.')
    print('5. To Check specified Value  n Group of Values')
    option = input('Enter - ')
    try:
        option = int(option)
    except:
        print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
        continue
    
    if (option < 0 or option > 5):
        print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
        continue
    
    if option == 0:
        print('\n\tTHANK YOU FOR JOINING US!')
        exit(-1)
    elif option == 1:
        all_prime()
    elif option == 2:
        even_odd()
    elif option == 3:
        prime_composite()
    elif option == 4:
        vowel_consonant()
    elif option == 5:
        check_in_group()
