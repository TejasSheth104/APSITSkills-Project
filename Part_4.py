# Write a Python program to test whether a passed letter is a vowel or not.

import string

def vowel_consonant():
    vowels = 'aeiou'
    alphabets = string.ascii_letters

    while True:
        print('\nEnter \'-1\' to GO BACK.')
        letter = input('Enter a letter - ')
    
        if letter == '-1':
            # exit condition
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            break
        elif (len(letter) != 1) or (letter not in alphabets):
            # checks if Length of Input is 1.
            # and also, if the input is present in the alphabets variable.
            print('\t1 LETTER EXCEPTED\n\tTRY AGAIN.\n')
            continue
    
        # converted input into lower case letter
        letter = letter.lower()
        if letter in vowels:
            print('Letter', letter.upper(), '- is a VOWEL')
        else:
            print('Letter', letter.upper(), '- is CONSONANT')

# uncomment to run the code.
# vowel_consonant()
